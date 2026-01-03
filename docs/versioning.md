# Versioning Strategy

This project follows **Semantic Versioning (SemVer)**:


## Version meanings

- **MAJOR** – Breaking API or infrastructure changes
- **MINOR** – Backward-compatible feature additions
- **PATCH** – Bug fixes and internal improvements

## Examples

- `1.0.0` – Stable public release
- `0.2.0` – New features
- `0.1.1` – Bug fixes

## GitOps alignment

- Git tags are immutable
- Container images are tagged with Git SHA
- Releases map directly to Git commits
