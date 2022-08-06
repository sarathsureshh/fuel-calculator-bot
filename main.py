import os
from array import array
from email.policy import default
from imaplib import Commands
from mimetypes import types_map
from typing import Counter
from unittest import result

import telebot
from sqlalchemy import null

user_dict = {}
class user:
    def __init__(self, mileage):
        self.mileage = mileage
        self.distance = None
        self.costPerLitre = None

APIKEY = "5484499326:AAH2S4eEqmKACIh4v2adQU9gRhf3MLyfxhw"
bot = telebot.TeleBot(APIKEY)

@bot.message_handler(commands=['start'])
def commandStart(message):    
	 bot.send_message(message.chat.id, "Hi " + message.from_user.first_name+ " , I'm Fuel Calc Bot\n"
                                        "Say /calculate to start calculating!\n"
                                        "Say /help to see all the commands")


                
@bot.message_handler(commands=['info'])
def commandInfo(message):    
	bot.send_message(message.chat.id, "Hi, I'm Fuel Calc Bot born as a result of boredom to my creator. I can get inputs and calculate the amount of money that you need to fill fuel to travel to a place. If you want to get in touch with my creator, message him at @thesarathsuresh 😉 ")

@bot.message_handler(commands=['help'])
def commandHelp(message):    
	bot.send_message(message.chat.id, "Hi " + message.from_user.first_name+ " , Use the following commands to get started?\n"
                                        "Say /start to activate me\n"
                                        "Say /calculate to start calculating!\n"
                                        "Say /info to view information about me\n"
                                        "Say /stop to stop me")
    
@bot.message_handler(commands=['stop'])
def commandStop(message):    
	bot.send_message(message.chat.id, "Thanks for using me, Bye 😉")


@bot.message_handler(commands=['calculate'])
def commandCalculate(message):
    msg = bot.send_message(message.chat.id, """\
        Alright lets calculate the amount that you need to travel!\n
What is your vehicle's mileage?
""")
    bot.register_next_step_handler(msg, processMileage)


def processMileage(message):
    try:
        chat_id = message.chat.id
        mileageTxt = message.text
        mileage = user(mileageTxt)
        user_dict[chat_id] = mileage
        msg = bot.send_message(message.chat.id, 'What is the distance that you are travelling?')
        bot.register_next_step_handler(msg, processDistance)
    except Exception as e:
        bot.reply_to(message, 'Oooops, something went wrong 😕')
   
def processDistance(message):
    try:
        chat_id = message.chat.id
        distanceTxt = message.text
        user = user_dict[chat_id]
        user.distance = distanceTxt
        msg = bot.send_message(message.chat.id, 'What is the cost of fuel per litre?')
        bot.register_next_step_handler(msg, processCostPerLitre)
        
    except Exception as e:
        bot.reply_to(message, 'Oooops, something went wrong 😕')

def processCostPerLitre(message):
    try:
        chat_id = message.chat.id
        costPerLitTxt = message.text
        user = user_dict[chat_id]
        user.costPerLit = costPerLitTxt

        #Calculation of the required fuel 
        floatedMileage = float(user.mileage)
        floatedDistance = float(user.distance)
        floatedCost = float(user.costPerLit)
        costPerKm = floatedCost/floatedMileage
        FinalResult = costPerKm*floatedDistance
        RoundedOffNumber = int(FinalResult)

        bot.send_message(chat_id, 'You will have to fill up Rs. '+str(RoundedOffNumber)+' worth of fuel!\nHappy journey 😄')
                
    except Exception as e:
        bot.reply_to(message, 'Oooops, something went wrong 😕')

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.infinity_polling()
