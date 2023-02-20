import json
import os

import openai
from dotenv import load_dotenv
load_dotenv()

### Input text for ChatGPT in a file called prompt.txt
# prompt = "Create a SQL query to count the total number of forms signed in 2022 and 2023 and filter for demographics_verified"

dir = os.getcwd() + "/Desktop/prompt.txt"
prompt = open(dir, "r").read()

### Get API key
openai.api_key = os.getenv("OPENAI_API_KEY")

### Call OpenAI ###
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.3,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)