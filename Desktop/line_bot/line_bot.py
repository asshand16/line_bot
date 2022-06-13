from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('kw9wTCRkaWyp4YQfVQQT4zshm+Ds31BlLvEskiQuCC9Aqi+0QytRx8VGk9o63ycyzzXPjhcL3wcbFkkIQE3tRkb2584yYXC64FO6N7NE0xnx/G0VJPb6jOfuAxERH9fyceCCd2wR5mfDu/TDikRUPAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f970d6decfcdfe525d72785121dd2653')


@app.route("/callback", methods=['POST'])
def callback():
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
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="你吃飯了嗎？"))


if __name__ == "__main__":
    app.run()