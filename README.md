# adkgcstoolsets
This repo teaches before_tool_call + GCS tool scoping, not a full production agent.
====================
Key structure choices for clarity:
====================
- Opens with a one-line "what problem does this solve" statement
- Quick-reference table pointing to the exact file for each concept
- Explains why before_tool_call matters before showing code
- Explicitly explains the None vs. dict return semantics, since that's the trickiest part for newcomers
- "Extending This Pattern" section signals what's intentionally left out (caching, per-user scoping, after_tool_call) so readers know it's a focused example, not a gap
