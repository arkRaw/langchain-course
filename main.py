import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()


def main():
    print("Hello from langchain-course!")
    print(os.getenv("OPENAI_API_KEY"))
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    print(llm.invoke("What is the capital of France?"))

    # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    # print(llm.invoke("What is the capital of France?"))


if __name__ == "__main__":
    main()
