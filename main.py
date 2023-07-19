import os
import openai
from flask import Flask, render_template, request
import json

openai.api_key = os.getenv("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")
openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]
@app.route('/dialogue', methods=['POST'])
def dialogue():
    user_input = request.json['user_input']
    ai_response = generate_ai_response(user_input, messages)
    messages.append({"role": "user", "content": user_input})  # 添加用户输入到对话历史
    messages.append({"role": "assistant", "content": ai_response})  # 添加助手回复到对话历史
    return {
        'ai_response': ai_response
    }


def generate_ai_response(user_input, messages):
    messages.append({"role": "user", "content": user_input})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    ai_message = completion.choices[0].message
    ai_response = ai_message.get("content").strip()
    return ai_response


if __name__ == '__main__':
    app.run()
