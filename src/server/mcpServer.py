from typing import Any
from fastmcp import FastMCP


mcp = FastMCP(
    name="mcp_server_s1",
    instructions="this is simple weather mcp server",
)


@mcp.tool()
def get_weather(location: str) -> dict[str, Any]:
    """Get weather information for a location"""
    # Dummy weather data for demonstration purposes
    weather_data = {
        "location": location,
        "temperature": "22°C",
        "condition": "Sunny",
        "humidity": "45%",
    }
    return weather_data


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8080)
