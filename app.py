import openai
import re
from flask import Flask, request, jsonify, abort
from dotenv import dotenv_values
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

config = dotenv_values("env.txt")
app = Flask(__name__)
openai.organization = config["ORG_KEY"]
openai.api_key = config["OPENAI_API_KEY"]
line_bot_api = LineBotApi(config["LINE_ACCESS_TOKEN"])
handler = WebhookHandler(config["CHANNEL_SECRET"])

@app.route("/", methods=["GET"])
def welcome():
    args = request.args
    print(args)
    if not "name" in args:
        return "hello, stranger"
    return "hello " + args["name"]



@app.route("/webhook", methods=["POST"])
def webhook():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text = text_completion(event.message.text)))

@app.route("/text_completion", methods=["POST"])
def text_completion(prompt):
    # Extract the prompt from the request body
    # Define the parameters for the API request
    model_engine = "text-davinci-002"
    max_tokens = 50
    temperature = 0.7

    # Call the OpenAI API to get the text completion
    completion = openai.Completion.create(
        engine=model_engine,
        prompt = "I am a smart student.\n Q: " + prompt + "\nA:",
        max_tokens=100,
        temperature=temperature,
        stop = ["\n"]
    )

    # Extract the completed text from the API
    # Extract the completed text from the API response
    result = completion.choices[0].text.strip()
    # Return the completed text in JSON format
    print(result)
    return result

if __name__ == '__main__':
    app.run()
