# Release Checklist

Before creating a release:

- [ ] CI pipeline is green on `main`
- [ ] Container images are published to GHCR
- [ ] Argo CD application is `Synced` and `Healthy`
- [ ] CHANGELOG updated
- [ ] Version number chosen (SemVer)
- [ ] Git tag created
- [ ] GitHub Release published

## Rollback strategy

- Revert Argo CD to a previous Git tag
- Images are immutable and reproducible
