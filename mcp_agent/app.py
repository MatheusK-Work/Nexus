import asyncio
from contextlib import asynccontextmanager

class MCPApp:
    def __init__(self, name: str):
        self.name = name
        self._agents = []

    def register_agent(self, agent, llm):
        self._agents.append((agent, llm))

    @asynccontextmanager
    async def run(self):
        print(f"[{self.name}] Inicializando...")
        await asyncio.sleep(0.1)
        class Context:
            def get_context(self_inner):
                return {}
        yield Context()
        print(f"[{self.name}] Finalizado.")
