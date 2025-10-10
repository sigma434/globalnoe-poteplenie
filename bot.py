import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.handler_backends import ContinueHandling
from telebot import types
from commands import parsing
bot = telebot.TeleBot("7817058953:AAHE8Goy-3RBC99C9Q3jsegvBWh2dCBtux8")


bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("info", "sending you a text about ecology"),
        telebot.types.BotCommand("start","greets you"),
        telebot.types.BotCommand("pars","парсит сайт с актуальными новостями про глобальное потепление и скидывает тебе результат")
        ])

#Каюсь пришлось воспользоваться нейронкой, тк парсинг не робил
@bot.message_handler(commands=["pars"])
def pars(message):
    try:
        infos=parsing()
        response = "📰 **Свежие новости о климате:**\n\n"
        for i, (title, link) in enumerate(zip(infos['title'], infos['link']), 1):
            if i > 5:  # Ограничиваем 5 новостями
                break
            response += f"{i}. {title}\n🔗 {link}\n\n"
        
        bot.send_message(message.chat.id, response)
    except:
        bot.send_message(message.chat.id, "Произошли технические шоколадки")



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который связан с проблемами глобального потепления.")


@bot.message_handler(commands=["info"])
def text(message):
    text=open("text.txt" ,"r",encoding="utf-8")
    f=text.read()
    bot.send_message(message.chat.id , f )
    text.close()
 

bot.infinity_polling()