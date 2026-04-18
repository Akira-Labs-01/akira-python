# Changelog

## 0.1.0 (2026-04-18)

Full Changelog: [v0.0.2...v0.1.0](https://github.com/Akira-Labs-01/akira-python/compare/v0.0.2...v0.1.0)

### Features

* **internal:** implement indices array format for query and form serialization ([dc79c75](https://github.com/Akira-Labs-01/akira-python/commit/dc79c75a3875a249a23d820dcc19a5538ec1228a))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([d2ee154](https://github.com/Akira-Labs-01/akira-python/commit/d2ee154d4faea736c2788334fc09fc5bc1384e82))
* **deps:** bump minimum typing-extensions version ([064713b](https://github.com/Akira-Labs-01/akira-python/commit/064713be80426366f13f8b21c42d784eb14f7117))
* ensure file data are only sent as 1 parameter ([93aa175](https://github.com/Akira-Labs-01/akira-python/commit/93aa1756139a0fd44b281d876d41f5a68856731f))
* **pydantic:** do not pass `by_alias` unless set ([a6f8138](https://github.com/Akira-Labs-01/akira-python/commit/a6f81383c8ac2f32ce30a341c4fee7dd24395496))
* sanitize endpoint path params ([501cb1d](https://github.com/Akira-Labs-01/akira-python/commit/501cb1d25b5e3ad1fcad46d904d3f25eafddb5b4))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([a7f13b4](https://github.com/Akira-Labs-01/akira-python/commit/a7f13b47ce5831a5dd3679d52f217f6a2bd8faf4))


### Chores

* **ci:** bump uv version ([4768fab](https://github.com/Akira-Labs-01/akira-python/commit/4768fab8b658cdd4ac9f3fa7fd0d6d89cb9d04ae))
* **ci:** skip lint on metadata-only changes ([dc37e5f](https://github.com/Akira-Labs-01/akira-python/commit/dc37e5fc6a8642c5a0679943385ee6f19b10a1f2))
* **ci:** skip uploading artifacts on stainless-internal branches ([a1d989c](https://github.com/Akira-Labs-01/akira-python/commit/a1d989c353d2049d8f3f5ee41bcbf3e7926b330f))
* **internal:** add request options to SSE classes ([3cc543a](https://github.com/Akira-Labs-01/akira-python/commit/3cc543ad1c60be29dfb35670dae51f639f7ae22f))
* **internal:** make `test_proxy_environment_variables` more resilient ([8d928f3](https://github.com/Akira-Labs-01/akira-python/commit/8d928f396769fe6583e09833297461f67962998f))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([b3b353c](https://github.com/Akira-Labs-01/akira-python/commit/b3b353ca2f49f8438707c255cee742ecc72456ee))
* **internal:** refactor authentication internals ([6cbcb9b](https://github.com/Akira-Labs-01/akira-python/commit/6cbcb9b9d73f2d756ea311e01fb0e962f94c2330))
* **internal:** tweak CI branches ([5ad61fc](https://github.com/Akira-Labs-01/akira-python/commit/5ad61fcdbca0c28c215ebb7f5219ce4adb4c449d))
* **internal:** update gitignore ([93c9f5f](https://github.com/Akira-Labs-01/akira-python/commit/93c9f5ff252ed3ffa61b4caaf6fb1fa03d550e3d))
* **internal:** update jsonl tests ([400fee3](https://github.com/Akira-Labs-01/akira-python/commit/400fee3c929086fdf0e8dc12cdfcd9c9a72a72b3))
* update SDK settings ([fe06676](https://github.com/Akira-Labs-01/akira-python/commit/fe066760f87a4c67c279def7842677f4636d1364))
* update SDK settings ([8e38e5c](https://github.com/Akira-Labs-01/akira-python/commit/8e38e5cddfb4a33409ef3e7e712a7ac9ae22d0e8))

## 0.0.2 (2026-02-20)

Full Changelog: [v0.0.1...v0.0.2](https://github.com/Akira-Labs-01/akira-python/compare/v0.0.1...v0.0.2)

### Chores

* configure new SDK language ([f364f25](https://github.com/Akira-Labs-01/akira-python/commit/f364f250d711b8bfa8b103dfb730491e69c5ed76))
* update SDK settings ([d899603](https://github.com/Akira-Labs-01/akira-python/commit/d899603bffef2fb1c09bd4d8322692c93c6cfc5a))
