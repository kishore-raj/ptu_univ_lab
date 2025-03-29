import argparse
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_google_genai import ChatGoogleGenerativeAI



MY_GEMINI_API_KEY = "<YOUR_GOOGLE_APIKEY>"


BASIC_PROMPT_TEMPLATE = """
    {question}
"""


PROMPT_TEMPLATE_FULL = """
System Message:
	Persona: You are a helpful AI assistant, answers my question based on following context
	context:
		{context}
---
User Message: {question} 
"""

context_text = """ """



def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_LLM(query_text)


def query_LLM(query_text: str):
    prompt_template = ChatPromptTemplate.from_template(BASIC_PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model_client = Ollama(model="llama3.2:1b")
    # model_client = ChatGoogleGenerativeAI(
    # model="gemini-1.5-flash",
    # api_key=MY_GEMINI_API_KEY,
    # temperature=0,
    # max_tokens=None,
    # timeout=None,
    # max_retries=2,
	# )
    
    response_text = model_client.invoke(prompt)

    formatted_response = f"""
    ===============LLM Response================== 
    REPLY:
    	
     {response_text}

    ===============LLM Response==================
    """
    print(formatted_response)
    return response_text


if __name__ == "__main__":
    main()