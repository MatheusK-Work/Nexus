import os
import openai

class OpenAIAugmentedLLM:
    def __init__(self, model="gpt-4o", allow_functions=True, response_timeout=30):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
        self.allow_functions = allow_functions
        self.timeout = response_timeout

    async def generate(self, prompt):
        resp = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=[{"role": "system", "content": prompt}],
            timeout=self.timeout
        )
        return resp.choices[0].message.content
