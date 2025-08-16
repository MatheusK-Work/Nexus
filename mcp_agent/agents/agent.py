class Agent:
    def __init__(self, name, instruction, server_names):
        self.name = name
        self.instruction = instruction
        self.server_names = server_names

    async def handle_message(self, message, context):
        response = f"(Simulação) [{self.name}] recebeu: {message}"
        return response
