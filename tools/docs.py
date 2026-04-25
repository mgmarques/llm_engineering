from openai import OpenAI
from IPython.display import Markdown, display


client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")

docs_prompt = '''
Provide the docs for all the functions/methods:
 * Including general description and sections on each function/method.
 * Do not add of fix the code.
 * Respond with the documentation in the code block with def function_name(...) -> something: followed by the docs.
 * Below is a skeleton to reference your answere, not to be used:

def x_function(y: str):
    """
    Provide a brief description in a single sentence.

    Next, a summary with steps and results in bullet points, like:

    The results are combined into a single Markdown-formatted string, where:
    - One thingh
    - Each relevant other

    Args:
        y (str): The y of the landing paradise.

    Returns:
        str: A formatted Markdown-formatted containing:
            - Paradise content
            - The content of each relevant information

    Raises:
        None explicitly. 
         - Any request-related errors from fetching data. 
         - Errors from fetching data may propagate

    Side Effects:
        - Prints progress messages to stdout.
        
    """
'''


class Docs():

    def __init__(
        self,
        openai_client: OpenAI = client,
        llm_model: str = "gemma3:4b"
    ):
        self._openai_client = openai_client
        self._llm_model = llm_model
        

    def docs_it(self, code: str, assinature:str = ""):
        print(f"# Start Docs: {assinature}")
        response = self._openai_client.chat.completions.create(
            model=self._llm_model, # "llama3.2:1b"
            messages=[
                {"role": "system", "content": docs_prompt},
                {"role": "user", "content": f"{assinature}\n{code}"}
                ]
            )

        result = response.choices[0].message.content
        display(Markdown(result))
        print("-"*60)

