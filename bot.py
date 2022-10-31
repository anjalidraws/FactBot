import telebot, requests

bot = telebot.TeleBot("bot_token")

@bot.message_handler(commands=["fact"])
def fact(message):
    headers = {"User-Agent":"Google bot 1.0"}
    response = requests.get("https://catfact.ninja/fact").json()
    bot.send_message(message.chat.id, response["fact"])

bot.polling()
