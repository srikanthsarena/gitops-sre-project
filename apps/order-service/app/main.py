import time
import uuid
import logging
import requests
from fastapi import FastAPI, Request, HTTPException
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from tenacity import retry, stop_after_attempt, wait_fixed

USER_SERVICE_URL = "http://localhost:8000"

app = FastAPI(title="order-service")

# -------------------------
# Logging
# -------------------------
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("order-service")

# -------------------------
# Metrics
# -------------------------
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "path", "status"]
)

REQUEST_LATENCY = Histogram(
    "http_request_latency_seconds",
    "HTTP request latency",
    ["path"]
)

# -------------------------
# Retry wrapper
# -------------------------
@retry(stop=stop_after_attempt(2), wait=wait_fixed(0.5))
def fetch_user(user_id: int):
    response = requests.get(
        f"{USER_SERVICE_URL}/users/{user_id}",
        timeout=1.5
    )
    response.raise_for_status()
    return response.json()

# -------------------------
# Middleware
# -------------------------
@app.middleware("http")
async def middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    try:
        response = await call_next(request)
        status = response.status_code
    except Exception as e:
        status = 500
        raise e
    finally:
        latency = round((time.time() - start_time) * 1000, 2)

        logger.info({
            "service": "order-service",
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": status,
            "latency_ms": latency,
        })

        REQUEST_COUNT.labels(
            method=request.method,
            path=request.url.path,
            status=status
        ).inc()

        REQUEST_LATENCY.labels(path=request.url.path).observe(latency / 1000)

    return response

# -------------------------
# API
# -------------------------
@app.get("/orders/{order_id}")
async def get_order(order_id: int):
    try:
        user = fetch_user(order_id)
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="User service unavailable"
        )

    return {
        "order_id": order_id,
        "item": "laptop",
        "price": 1200,
        "user": user
    }

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/metrics")
async def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
