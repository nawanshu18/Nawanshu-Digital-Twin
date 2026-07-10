from openai import OpenAI
from context import TWIN_SYSTEM_PROMPT
from tools import tools, handle_tool_calls
from styles import CSS, JS, EXAMPLES
from dotenv import load_dotenv
import gradio as gr
import os

load_dotenv(override=True)

MODEL_NAME = "llama-3.3-70b-versatile"

openai = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

system = [{"role": "system", "content": TWIN_SYSTEM_PROMPT}]


def chat(message, history):
    messages = system

    # Convert Gradio history to OpenAI/Groq format
    for item in history:
        messages.append({
            "role": item["role"],
            "content": item["content"]
        })

    messages.append({"role": "user", "content": message})

    response = openai.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools
    )

    while response.choices[0].finish_reason == "tool_calls":
        assistant_message = response.choices[0].message
        tool_calls = assistant_message.tool_calls

        results = handle_tool_calls(tool_calls)

        messages.append(assistant_message)
        messages.extend(results)

        response = openai.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            tools=tools
        )

    return response.choices[0].message.content


if __name__ == "__main__":
    gr.ChatInterface(
        chat,
        examples=EXAMPLES,
        title="Nawanshu’s Digital Twin",
        description="Welcome to my Digital Twin! I'm an AI-powered assistant that represents my professional journey.",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())
