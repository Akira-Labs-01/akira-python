# Sandboxes

Types:

```python
from akira.types import (
    Sandbox,
    SandboxCreateResponse,
    SandboxListResponse,
    SandboxDeleteResponse,
    SandboxCloneResponse,
    SandboxDeleteAllResponse,
    SandboxExecuteResponse,
    SandboxExecuteAsyncResponse,
    SandboxLogsResponse,
    SandboxSnapshotResponse,
    SandboxStatusResponse,
    SandboxUploadResponse,
)
```

Methods:

- <code title="post /v1/sandboxes/create">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">create</a>(\*\*<a href="src/akira/types/sandbox_create_params.py">params</a>) -> <a href="./src/akira/types/sandbox_create_response.py">SandboxCreateResponse</a></code>
- <code title="get /v1/sandboxes/list">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">list</a>(\*\*<a href="src/akira/types/sandbox_list_params.py">params</a>) -> <a href="./src/akira/types/sandbox_list_response.py">SandboxListResponse</a></code>
- <code title="delete /v1/sandboxes/{id}/delete">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">delete</a>(id, \*\*<a href="src/akira/types/sandbox_delete_params.py">params</a>) -> <a href="./src/akira/types/sandbox_delete_response.py">SandboxDeleteResponse</a></code>
- <code title="post /v1/sandboxes/{id}/clone">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">clone</a>(id, \*\*<a href="src/akira/types/sandbox_clone_params.py">params</a>) -> <a href="./src/akira/types/sandbox_clone_response.py">SandboxCloneResponse</a></code>
- <code title="delete /v1/sandboxes/delete-all">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">delete_all</a>() -> <a href="./src/akira/types/sandbox_delete_all_response.py">SandboxDeleteAllResponse</a></code>
- <code title="get /v1/sandboxes/{id}/download">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">download</a>(id, \*\*<a href="src/akira/types/sandbox_download_params.py">params</a>) -> BinaryAPIResponse</code>
- <code title="post /v1/sandboxes/{id}/execute">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">execute</a>(id, \*\*<a href="src/akira/types/sandbox_execute_params.py">params</a>) -> <a href="./src/akira/types/sandbox_execute_response.py">SandboxExecuteResponse</a></code>
- <code title="post /v1/sandboxes/{id}/execute_async">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">execute_async</a>(id, \*\*<a href="src/akira/types/sandbox_execute_async_params.py">params</a>) -> <a href="./src/akira/types/sandbox_execute_async_response.py">JSONLDecoder[SandboxExecuteAsyncResponse]</a></code>
- <code title="get /v1/sandboxes/logs">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">logs</a>(\*\*<a href="src/akira/types/sandbox_logs_params.py">params</a>) -> <a href="./src/akira/types/sandbox_logs_response.py">SandboxLogsResponse</a></code>
- <code title="post /v1/sandboxes/{id}/snapshot">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">snapshot</a>(id, \*\*<a href="src/akira/types/sandbox_snapshot_params.py">params</a>) -> <a href="./src/akira/types/sandbox_snapshot_response.py">SandboxSnapshotResponse</a></code>
- <code title="get /v1/sandboxes/{id}/status">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">status</a>(id, \*\*<a href="src/akira/types/sandbox_status_params.py">params</a>) -> <a href="./src/akira/types/sandbox_status_response.py">SandboxStatusResponse</a></code>
- <code title="post /v1/sandboxes/{id}/upload">client.sandboxes.<a href="./src/akira/resources/sandboxes.py">upload</a>(id, \*\*<a href="src/akira/types/sandbox_upload_params.py">params</a>) -> <a href="./src/akira/types/sandbox_upload_response.py">SandboxUploadResponse</a></code>

# Snapshots

Types:

```python
from akira.types import (
    SnapshotListResponse,
    SnapshotDeleteResponse,
    SnapshotDeleteAllResponse,
    SnapshotRestoreResponse,
)
```

Methods:

- <code title="get /v1/snapshots/list">client.snapshots.<a href="./src/akira/resources/snapshots.py">list</a>(\*\*<a href="src/akira/types/snapshot_list_params.py">params</a>) -> <a href="./src/akira/types/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="delete /v1/snapshots/{id}">client.snapshots.<a href="./src/akira/resources/snapshots.py">delete</a>(id) -> <a href="./src/akira/types/snapshot_delete_response.py">SnapshotDeleteResponse</a></code>
- <code title="delete /v1/snapshots/delete-all">client.snapshots.<a href="./src/akira/resources/snapshots.py">delete_all</a>() -> <a href="./src/akira/types/snapshot_delete_all_response.py">SnapshotDeleteAllResponse</a></code>
- <code title="post /v1/snapshots/{id}/restore">client.snapshots.<a href="./src/akira/resources/snapshots.py">restore</a>(id, \*\*<a href="src/akira/types/snapshot_restore_params.py">params</a>) -> <a href="./src/akira/types/snapshot_restore_response.py">SnapshotRestoreResponse</a></code>
