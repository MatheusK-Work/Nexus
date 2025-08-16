import os
import asyncio
import logging
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.llm.augmented_llm_openai import OpenAIAugmentedLLM

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    logger.error("OPENAI_API_KEY não definida.")
    exit(1)

async def run_agent():
    app = MCPApp(name="mcp_ai_agent_improved")

    async with app.run() as mcp:
        agent = Agent(
            name="multi_tool_agent",
            instruction=("Você pode usar ferramentas como mapas e filesystem "
                         "para responder perguntas."),
            server_names=["maps", "filesystem", "fetch"]
        )
        llm = OpenAIAugmentedLLM(
            model="gpt-4o",
            allow_functions=True,
            response_timeout=60
        )
        app.register_agent(agent, llm)

        while True:
            pergunta = input("\nPergunta (ou 'exit'): ").strip()
            if pergunta.lower() in ("exit", "sair"):
                print("Encerrando...")
                break
            try:
                resposta = await agent.handle_message(pergunta, context=mcp.get_context())
                print("\n👉 Resposta:\n", resposta)
            except Exception:
                logger.exception("Erro no processamento:")

if __name__ == "__main__":
    try:
        asyncio.run(run_agent())
    except KeyboardInterrupt:
        logger.info("Interrompido pelo usuário.")
