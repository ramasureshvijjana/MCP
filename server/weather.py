from typing import Any
from mcp.server.fastmcp import FastMCP
import httpx

# Step -1 :Intialize the FastMCP server.
## "weather_server" is the server name.
mcp = FastMCP("weather_server")


# Step 2: Weather API values.
"""
NWS_API_BASE → Where to get weather data from.
USER_AGENT → Who is requesting the weather data.
"""
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather_app_example/1.0"

# Step 3: Create a function to fetch weather data from the NWS API.
async def fetch_weather_data(url: str) -> dict[str, Any] | None:
    """
    Fetch active weather alerts in Json format for California from the NWS API.

    Perameters: url (str) → The NWS API endpoint URL.
    Returns: dict[str, Any] | None → The weather data in JSON format or None if the request fails.
    """
    # API Headers
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json", # Tells the server what response format you want : [application/geo+json = GeoJSON]
        
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, timeout=30.0)
        if response.status_code == 200:
            return response.json()
        else:
            return None

# Step 4: Create a MCP tool to get weather details for a specific area.
@mcp.tool() 
async def weather_service() -> str | None:
    """
    This tool calls the fetch_weather_data function to get active weather alerts for Californiafrom the NWS API.
    
    Perameters: None
    Returns: str | None
    """
    url =f"{NWS_API_BASE}/alerts/active/area/CA"
    data = await fetch_weather_data(url)

    if not data or "features" not in data:
        return "Unable to get the weather details"    
    if not data['features']:
        return "No active weather details"    
    
    print(f"Weather data : {data}")