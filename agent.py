from google.adk.agents import Agent
from google.adk.integrations.gcs import GCSToolset
from google.adk.tools.tool_context import ToolContext
from google.adk.tools.base_tool import BaseTool
from typing import Optional

TARGET_BUCKET = "unnati0370cc408398a5qwiklabs"

def pin_bucket_callback(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext,
) -> Optional[dict]:
    if "bucket_name" in args:
        args["bucket_name"] = TARGET_BUCKET
    return None

gcs_toolset = GCSToolset()

root_agent = Agent(
    model="gemini-2.5-flash",
    name="gcs_pdf_search_agent",
    instruction=f"""You are a document assistant with access to GCS tools (list_objects, get_object_data, get_object_metadata, get_bucket).
All files live in bucket "{TARGET_BUCKET}". Use list_objects to find PDFs, get_object_data to read their content,  then answer the user's question — always citing which file you used.
If nothing relevant is found, say so clearly.""", 
tools=[gcs_toolset],   # <-- pass the toolset object, not gcs_toolset.get_tools()
before_tool_callback=pin_bucket_callback,
)
