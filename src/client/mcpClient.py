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
        prompt = await client.list_prompts()
        resourses = await client.list_resources()
        resourses_template = await client.list_resource_templates()

        print(f"Available tools: {[tool.name for tool in tools]}")
        print(f"Available prompts: {[p.name for p in prompt]}")
        print(f"Available resources: {[r.name for r in resourses]}")
        print(f"Available resource templates: {[rt.name for rt in resourses_template]}")

        # Call a tool (example: calling 'add' tool)
        if tools:
            result = await client.call_tool("get_weather", {"location": "India"})
            print(f"Result of get_weather: {result}")
        # Call a prompt (example: calling 'summarize_weatherCondition' prompt)
        if prompt:
            result = await client.get_prompt(
                "summarize_weatherCondition", {"location": "India"}
            )
            print(f"Result of summarize_weatherCondition: {result}")
        # Call a resource (example: calling 'gov://India/ndrf' resource)
        if resourses_template:
            result = await client.read_resource("gov://India/ndrf")
            print(f"Result of gov://India/ndrf: {result}")


if __name__ == "__main__":
    asyncio.run(main())


# from fastmcp import Client

# config = {
#     "mcpServers": {
#         "remote-service": {
#             "url": "https://api.example.com/mcp",
#             "headers": {
#                 "Authorization": "Bearer YOUR_TOKEN"
#             }
#         }
#     }
# }

# async def run_complex_client():
#     client = Client(config)
#     async with client:
#         # Note: In multi-server mode, tool names are prefixed: 'servername_toolname'
#         result = await client.call_tool("remote-service_get_data", {"query": "test"})
#         print(result)
