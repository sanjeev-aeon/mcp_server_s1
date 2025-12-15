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


@mcp.resource("gov://{location}/ndrf")
def ndrf_resource(location: str) -> dict[str, Any]:
    """Fetch NDRF resource information for a location"""
    # Dummy resource data for demonstration purposes
    resource_data = {
        "location": location,
        "resources": [
            {"type": "Food", "quantity": "1000 packs"},
            {"type": "Water", "quantity": "5000 liters"},
            {"type": "Medical Supplies", "quantity": "200 kits"},
        ],
    }
    return resource_data


@mcp.prompt("summarize_weatherCondition")
def summarize(location: str) -> str:
    """Summarize weather and resource information for a location"""
    summary = f"summarize the weather condition of {location}:\n"
    return summary


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=8080)
