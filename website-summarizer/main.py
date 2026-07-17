from openai.types import model
from openai.types.responses import response
from httpcore import request
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup


load_dotenv(override=True)

# importing keys 
open_router_key = os.getenv("OPENROUTER_API_KEY")
open_router_base_url = os.getenv("OPENROUTER_BASE_URL")

# creating client 
client = OpenAI(api_key=open_router_key,base_url=open_router_base_url)

url = "https://kubernetes.io/blog/2026/07/14/custom-metrics-exporter-kubernetes/"

# function to take url and return summary 
def summarize_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    title = soup.title.text if soup.title else None
    for irrelevantTag in soup.body(["script","style","nav","footer","header","aside","form"]):
        irrelevantTag.decompose()
    text = soup.get_text(separator="\n",strip=True)
    return title + " " + text


message = [{
    "role":"system",
    "content":"You are a helpful assistent that summarize the give text details by user."
},
{
    "role":"user",
    "content":f"Please can you summarise this text +  {summarize_url(url)}"
}]


response = client.chat.completions.create(
    model="nvidia/nemotron-3-ultra-550b-a55b:free",
    messages= message 
) 

print(response.choices[0].message.content)