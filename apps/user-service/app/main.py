import time
import uuid
import logging
from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="user-service")

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("user-service")

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

@app.middleware("http")
async def request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.time()

    response: Response = await call_next(request)

    latency = round((time.time() - start_time) * 1000, 2)

    logger.info(
        {
            "service": "user-service",
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "latency_ms": latency,
        }
    )

    REQUEST_COUNT.labels(
        method=request.method,
        path=request.url.path,
        status=response.status_code
    ).inc()

    REQUEST_LATENCY.labels(path=request.url.path).observe(latency / 1000)

    response.headers["X-Request-ID"] = request_id
    return response

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/readyz")
async def readyz():
    return {"status": "ready"}

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Test User"
    }
