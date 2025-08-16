import asyncio

async def maps_handler(query: str):
    await asyncio.sleep(0.1)
    return {"tool": "maps", "result": f"Simulação de mapa para '{query}'"}
