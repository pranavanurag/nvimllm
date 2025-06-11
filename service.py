#!/usr/bin/env python3
from flask import Flask, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('text', '')

    try:
        response = client.responses.create(
            model="gpt-4.1",
            instructions="""
            You will be given a programming question. Your response will contain the least number of tokens, while meeting the following requirements:
            - A short explanation of the solution
            - Explanation is followed by the fewest lines of code required
            - Plaintext only, no markdown
            """,
            input=f"{question}"
        )
        return response.output_text

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='localhost', port=7777, debug=True)
