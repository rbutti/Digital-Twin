from random import choices
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display
import gradio as gr
import json
import os
from styles import *
from context import TWIN_SYSTEM_PROMPT, EXAMPLES
from tools import tools, handle_tool_calls

load_dotenv(override=True)

MODEL_NAME = "openrouter/free"
BASE_URL = "https://openrouter.ai/api/v1"

client = OpenAI(base_url=BASE_URL, api_key=os.getenv("OPENROUTER_API_KEY"))
system_prompt = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]

def chat(message,history=[]):
    messages = system_prompt + history + [{"role": "user", "content": message}]
    response = client.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    while response.choices[0].finish_reason == "tool_calls":
        message = response.choices[0].message
        tool_calls = message.tool_calls
        result = handle_tool_calls(tool_calls)
        messages.append(message)
        messages.extend(result)
        response = client.chat.completions.create(model=MODEL_NAME, messages=messages, tools=tools)
    return response.choices[0].message.content

if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples= EXAMPLES,
        title="Agentic professional Twin",
        description="Talk to my AI twin about my career",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(
        theme=gr.themes.Monochrome(
            primary_hue="purple",
            secondary_hue="blue",
            neutral_hue="gray",
        ),
        css=css,
    )
