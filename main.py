from PyPDF2 import PdfReader
from openai import OpenAI
import json
from tools.registry import TOOLS_MAP
from tools.tools import tools
from config import MODEL
import gradio as gr


class Me:
    def __init__(self):
        self.openai = OpenAI()
        self.name = "Md Jahirul Islam Shifat"
        reader = PdfReader("me/linkedin_profile.pdf")
        self.linkedin = ""
        self.resume=""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                self.linkedin += text

        reader2 = PdfReader("me/j_shifat_resume.pdf")       
        for page in reader2.pages:
            text = page.extract_text()
            if text:
                self.resume += text

        with open("me/summary.txt", "r", encoding="utf-8") as f:
            self.summary = f.read()
        



    def handle_tool_call(self, tool_calls):
        results = []
        for tool_call in tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)
            print(f"Tool called: {tool_name}", flush=True)
            tool = TOOLS_MAP.get(tool_name)
            result = tool(**arguments) if tool else {}
            results.append({"role": "tool","content": json.dumps(result),"tool_call_id": tool_call.id})
        return results

    def system_prompt(self):
        system_prompt = f"You are acting as {self.name}. You are answering questions on {self.name}'s website, \
particularly questions related to {self.name}'s career, background, skills and experience. \
Your responsibility is to represent {self.name} for interactions on the website as faithfully as possible. \
You are given a summary of {self.name}'s background and LinkedIn profile and resume which you can use to answer questions. \
Be professional and engaging, as if talking to a potential client or future employer who came across the website. \
If you don't know the answer to any question, use your record_unknown_question tool to record the question that you couldn't answer, even if it's about something trivial or unrelated to career. \
If the user is engaging in discussion, try to steer them towards getting in touch via email; ask for their email and record it using your record_user_details tool. "

        system_prompt += f"\n\n## Summary:\n{self.summary}\n\n## LinkedIn Profile:\n{self.linkedin}\n\n## Resume:\n{self.resume}\n\n"
        system_prompt += f"With this context, please chat with the user, always staying in character as {self.name}."
        return system_prompt



    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_prompt()}] + history + [{"role": "user", "content": message}]
        done = False
        while not done:
            response = self.openai.chat.completions.create(model=MODEL, messages=messages, tools=tools)
            if response.choices[0].finish_reason=="tool_calls":
                message = response.choices[0].message
                tool_calls = message.tool_calls
                results = self.handle_tool_call(tool_calls)
                messages.append(message)
                messages.extend(results)
            else:
                done = True
        return response.choices[0].message.content        


if __name__ == "__main__":

    me = Me()

def respond(message, chat_history):
    reply = me.chat(message, chat_history)
    chat_history.append((message, reply))
    return "", chat_history


with gr.Blocks(theme=gr.themes.Soft(), css="""
#chatbot {
    height: 500px;
    overflow-y: auto;
    border-radius: 12px;
}

.user {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 10px !important;
}

.bot {
    background-color: #f1f5f9 !important;
    border-radius: 12px !important;
    padding: 10px !important;
}
""") as demo:

    gr.Markdown("""
    # 🤖 AI Career Assistant
    Chat with me about my experience, skills, and projects.
    """)

    chatbot = gr.Chatbot(elem_id="chatbot")

    with gr.Row():
        msg = gr.Textbox(
            placeholder="Ask something...",
            scale=8,
            container=False
        )
        send_btn = gr.Button("Send", scale=1)

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    send_btn.click(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

