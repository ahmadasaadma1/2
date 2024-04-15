import telebot
from telebot.types import Message

bot = telebot.TeleBot("6782521207:AAGojdYUCbSzfGjVBVF87xTrpJZqWbjbX7Q")

myName = None


@bot.message_handler()
def Myfunc(message: telebot.types.Message):
  global MyLast_id, myName
  MyLast_id = message.from_user.id
  txt = message.text
  mid = message.chat.id
  WhatIsMyName(message)
  if txt == "/sname":
    bot.send_message(mid, "الان, اكتب اسمك")
    bot.register_next_step_handler(message, Save_name)
    WhatIsMyName(message)
  else:
    bot.send_message(mid, "ارسل /sname")


def WhatIsMyName(message: Message):
  txt = message.text
  mid = message.chat.id
  if txt == "/name":
    if myName:
      bot.send_message(mid, f"اسمك: {myName}")
    else:
      bot.send_message(mid, f"لا اعرف اسمك, اكتب /sname ليتم حفظ اسمك.")


def Save_name(message: Message):
  global myName
  txt = message.text
  mid = message.chat.id
  if message.from_user.id == MyLast_id:
    myName = txt
    bot.send_message(mid, "تم حفظ الاسم, ارسل '/name '")
  else:
    bot.register_next_step_handler(message, Save_name)


print("Bot Is Running")
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return "<b> hello</b>"


@app.route('/user_mes')
def user_mes():
  return "<b> hello user_mes</b>"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

bot.infinity_polling(skip_pending=True)
