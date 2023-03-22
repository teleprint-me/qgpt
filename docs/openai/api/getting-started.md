# Getting Started With OpenAI GPT (GPT 3.5 Model) API In Python

-   Date: Mar 2, 2023
-   Tags: OpenAI, Python
-   Source: [Learn Data Analysis](https://learndataanalysis.org/getting-started-with-openai-gpt-gpt-3-5-model-api-in-python/)

In this tutorial, we will learn how to use OpenAI ChatGPT (GPT 3.5) API in Python.

If you have never heard of OpenAI before, OpenAI is the company that developed ChatGPT, and OpenAI API is the service that allows developers to access the AI models that creates ChatGPT through REST API.

## Install and setup

### Step 1: Create an OpenAI account

    The first step to getting started with OpenAI GPT API is to create an account on the OpenAI website. Go to https://openai.com/api/ and sign up for an account.

### Step 2: Generate OpenAI API key

    To connect to OpenAI API endpoint, we need to first create a secret key. Click on your user name, then click on View API keys. Click Create new secret key button to generate an API key.

### Step 3: Install the OpenAI API package

    The OpenAI API package can be installed using the pip package manager in Python. Open a terminal and type the following command to install the package:

```sh
pip install openai
```

### Step 4: Connect to OpenAI In Python

    To connect to OpenAI endpoint, we will import the openai modle and attach the API key

```py
import openai

API_KEY = '<openAI API key>'
openai.api_key = API_KEY
Python
```

## Example Source Code:

```py
import openai

openai.api_key = '<API_KEY>'
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    # api_usage = response['usage']
    # print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    # print(response['choices'][0].finish_reason)
    # print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

conversation = []
conversation.append({'role': 'system', 'content': 'How may I help you?'})
conversation = ChatGPT_conversation(conversation)
print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

while True:
    prompt = input('User:')
    conversation.append({'role': 'user', 'content': prompt})
    conversation = ChatGPT_conversation(conversation)
    print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))
```
