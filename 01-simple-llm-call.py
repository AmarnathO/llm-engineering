from openai.types import model
from altair import api
from openai import OpenAI
from dotenv import load_dotenv
import os

# loading variables 
load_dotenv(override=True)

# importing keys 
open_router_keys = os.getenv("OPENROUTER_API_KEY")
open_router_base_url = os.getenv("OPENROUTER_BASE_URL")


# creating llm client 
client = OpenAI(api_key=open_router_keys,base_url=open_router_base_url)

# creating message
message = [
    {"role":"user","content":"Hey there how are you"},
    {"role":"system","content":"You are a witty assistance reply in very witty way"}    
    ]

# Calling llm 
response = client.chat.completions.create(model="nvidia/nemotron-3-ultra-550b-a55b:free",messages=message)

# print response
print(response.choices[0].message.content)