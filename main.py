from langchain import PromptTemplate
from langchain.utilities import SerpAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import load_tools, AgentType
import os

template = """
Provide company information for {company}, including description, founders, funding rounds, location and website
"""

# we prompt the prompt fromt the terminal
company = str(input("Enter a company name: ") or "Prematch GmbH")
prompt = PromptTemplate(
    input_variables=["company"],
    template=template
)

open_ai_api_key = os.environ.get("OPENAI_API_KEY")
llm = OpenAI(openai_api_key=open_ai_api_key,temperature=0, model_name="text-davinci-003")


serp_api_key = os.environ.get("SERPAPI_API_KEY")
search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
search_tool = [Tool(
    name="Intermediate Answer",
    func=search.run,
    description="Searches for an answer to the question"
)]

self_ask_with_search = initialize_agent(
    search_tool,
    llm,
    agent=AgentType.SELF_ASK_WITH_SEARCH,
    verbose=True
)
print(prompt.format(company=company))
self_ask_with_search.run(prompt.format(company=company))
