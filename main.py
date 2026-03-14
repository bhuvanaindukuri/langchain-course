from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from urllib3 import response

load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
    Swami Vivekananda [a] (12 January 1863 – 4 July 1902), born Narendranath Datta,[b] was an Indian Hindu monk, philosopher, author, religious teacher, and the chief disciple of the Indian mystic Ramakrishna.[4][5] Vivekananda was a major figure in the introduction of Vedanta and Yoga to the Western world,[6][7][8] and is credited with raising interfaith awareness and elevating Hinduism to the status of a major world religion.[
    """
    # print(os.environ.get("OPENAI_API_KEY"))
    summary_template = f"""
    given the information {information} about a person I want you to create:
    1) A short summary
    2) two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
