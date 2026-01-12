# Intialize MCP Server

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather_server")
```

# Use of 'async' Keyword in Python

```python
async def fetch_weather_data(url: str) -> dict[str, Any] | None:
```
- **async** is used to write non-blocking (asynchronous) code.  
- It allows Python to handle/run multiple waiting tasks/funtions efficiently without blocking the program.

# Use of 'with' Keyword in Python

```python
async with httpx.AsyncClient() as client:
```
- It opens a resource, lets you use it, and closes it automatically — even if an error occurs.
- You must manually close resources if we not use the 'with'

**Other Real Uses of 'with':**
```python
with lock:                  # thread locks
with database_connection:   # DB connections
with requests.Session():   # HTTP session
with httpx.Client():       # HTTP client
```
# Use of '@mcp.tool()' Keyword in Python

```python
@mcp.tool() 
async def weather_service() -> str | None:
```
- @mcp.tool() registers a Python function as a callable tool that an LLM can use through the MCP server.
1. The function weather_service is NOT executed in python, instead of it passes weather_service into mcp.tool()
2. MCP stores metadata (dict) of weather_service function. This metadata called as MCP tool schema
3. When MCP connects to an LLM, MCP sends tool schema. Now LLM knows this function exists.
4. The LLM uses the function’s docstring to understand the tool’s purpose and behavior.
