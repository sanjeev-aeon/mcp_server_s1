import asyncio
from fastmcp import Client


async def main():
    # FastMCP automatically infers 'streamable-http' transport for URLs
    client = Client("http://localhost:8080/mcp")

    # Use 'async with' to manage the connection lifecycle automatically
    async with client:
        print(f"Connected to: {client.initialize_result.serverInfo}")

        # List tools provided by the server
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")

        # Call a tool (example: calling 'add' tool)
        if tools:
            result = await client.call_tool("get_weather", {"location": "India"})
            print(f"Result of get_weather: {result}")


if __name__ == "__main__":
    asyncio.run(main())
