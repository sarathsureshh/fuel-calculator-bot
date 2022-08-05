import os
import types
from email.policy import default
from imaplib import Commands
from mimetypes import types_map
from unittest import result

import telebot
from sqlalchemy import null

API_KEY = os.getenv("API_KEY")


bot = telebot.TeleBot("5484499326:AAH2S4eEqmKACIh4v2adQU9gRhf3MLyfxhw")

@bot.message_handler(commands=['start'])
def commandStart(message):    
	 bot.send_message(message.chat.id, "Hi " + message.from_user.first_name+ " , I'm Fuel Calc Bot\n"
                                        "Say /calculate to start calculating!\n"
                                        "Say /help to see all the commands")

@bot.message_handler(commands=['calculate'])
def commandCalculate(message):
    bot.send_message(message.chat.id, "This feature is under construction, will be live soon 😉")
	# bot.send_message(message.chat.id, "Alright lets calculate the amount that you need to travel!\n"
    #                                   "What is your vehicle's mileage?")
                
@bot.message_handler(commands=['info'])
def commandInfo(message):    
	bot.send_message(message.chat.id, "Hi, I'm Fuel Calc Bot born as a result of boredom to my creator. I can Get inputs and calculate the amount of money that you need to fill fuel to travel to a place. If you want to get in touch with my creator, message him at @thesarathsuresh 😉 ")

@bot.message_handler(commands=['help'])
def commandHelp(message):    
	bot.send_message(message.chat.id, "Hi " + message.from_user.first_name+ " , Use the following commands to get started?\n"
                                        "Say /start to activate me\n"
                                        "Say /calculate to start calculating!\n"
                                        "Say /info to view information about me\n"
                                        "Say /stop to stop the me")
    
@bot.message_handler(commands=['stop'])
def commandStop(message):    
	bot.send_message(message.chat.id, "Thanks for using me, Bye 😉")
        

   
@bot.message_handler(func=lambda query: True)
def returnMessage(message):      
    bot.send_message(message.chat.id, "Well, I'm working on myself to understand you, will learn sooner 😉")


bot.infinity_polling()
