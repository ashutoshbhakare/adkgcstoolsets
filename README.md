# adkgcstoolsets
# GcsToolset is a custom toolset I wrote implementing ADK's BaseToolset interface — ADK doesn't ship a pre-built GCS search toolset natively, so this wraps the google-cloud-storage SDK into search_bucket and read_object tools.

before_tool_call callback enforces bucket/prefix scoping, query validation, and logging — the pattern shown is the standard ADK callback signature (tool, args, tool_context) that can inspect or override any tool call before it executes.

Everything's designed to plug into the deployment patterns from your earlier guides (Cloud Run, GKE with externalized sessions).
