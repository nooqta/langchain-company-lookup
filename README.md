# LangChain Company Information Retrieval Tool

This Python script prompts the user to input a company name and retrieves information about the company using OpenAI and SerpAPIWrapper.

## Requirements

- Python 3.7 or higher

Additionally, you need to set the following environment variables with your API keys:

- `OPENAI_API_KEY`: Your OpenAI API key
- `SERPAPI_API_KEY`: Your SerpAPIWrapper API key

```
export OPENAI_API_KEY=your_openai_api_key
export SERPAPI_API_KEY=your_serpapi_api_key
```

## Getting Started

1. Clone the project
2. Install dependencies

```
pip install -r requirements.txt
```

## Usage

1. Open a terminal and navigate to the directory where the script is located.
2. Run the script with the command `python main.py`.
3. When prompted, enter the name of the company you want to retrieve information for. If you do not enter anything, the default value is `Prematch GmbH` as in the Linkedin original post.
4. The script will then use the LangChain library to retrieve the following information about the company:
   - Description
   - Founders
   - Funding rounds
   - Location
   - Website
5. The script will print out the retrieved information.

## Code Description

The `readme.md` file provides a brief overview of how to use the script. Here is a more detailed description of what the script does:

1. The script imports the necessary modules from the `langchain` package, as well as the `os` module.
2. A prompt template is defined using a string. The template includes a placeholder for the company name.
3. The user is prompted to input a company name using the `input` function. If the user does not enter anything, the default value is `Prematch GmbH`.
4. A `PromptTemplate` object is created using the `template` string and the `input_variables` parameter. The `input_variables` parameter specifies that the `company` variable will be used in the `template`.
5. The OpenAI API key and the SerpAPIWrapper API key are retrieved from environment variables using the `os.environ.get` function.
6. An `OpenAI` object is created using the retrieved API key, a temperature of 0, and the `text-davinci-003` model.
7. A `SerpAPIWrapper` object is created using the retrieved API key.
8. A `Tool` object is created using the `search.run` method from the `SerpAPIWrapper` object, along with a name, description, and function.
9. An `Agent` object is created using the `initialize_agent` function from the `langchain.agents` module. The `Agent` object uses the `search_tool` and `llm` objects, and specifies that it is an `AgentType.SELF_ASK_WITH_SEARCH` agent.
10. The prompt string is formatted with the `company` variable using the `format` method, and is printed to the console.
11. The `run` method of the `Agent` object is called with the formatted prompt string as an argument. The `run` method retrieves the requested information from OpenAI and SerpAPIWrapper and prints it to the console.

## Resources
- [OpenAI](https://platform.openai.com/docs/introduction)
- [Langchain](https://python.langchain.com/en/latest/)
- [SERPAPI](https://serpapi.com/)

## Credit
The idea of the project originated from a Linkedin post by [Dries Faems](https://www.linkedin.com/in/dries-faems-0371569/)
