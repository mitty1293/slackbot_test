# _*_ coding: utf-8 _*_
from slackbot.bot import respond_to
from slackbot.bot import listen_to

# メンションでの「こんにちは」に反応する
@respond_to('こんにちは')
def hello(message):
    # 応答メッセージとしてメンションで返す
    message.reply('こんにちはー')

# メッセージに「おはよう」があると反応する
@listen_to('おはよう')
def help(message):
    # 通常のメッセージとして送信する
    message.send('おはようございます')