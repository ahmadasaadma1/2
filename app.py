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
