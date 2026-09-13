from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    object = "condom"

    my_template = """
        Explain the properties of {object}
        in a funny way. Keep the answer short.
"""

    prompt_template = PromptTemplate(input_variables=["object"], template=my_template)
    llm = ChatOllama(temperature=1, model="qwen3.6:35b")
    chain = prompt_template | llm
    response = chain.invoke(input={"object": object})
    print(response.content)

if __name__ == "__main__":
    main()
