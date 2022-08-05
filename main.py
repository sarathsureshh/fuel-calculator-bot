from cgitb import text
from email.policy import default
from imaplib import Commands
from sqlalchemy import null
import telebot
import os

API_KEY = os.getenv("API_KEY")
mileage = 0
distance = 0
per_liter_cost = 0

bot = telebot.TeleBot("5484499326:AAH2S4eEqmKACIh4v2adQU9gRhf3MLyfxhw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):    
	bot.reply_to(message, "Howdy, how are you doing?, Say /Calculate to start calculating!")

@bot.message_handler(commands=['Calculate'])
def send_welcome(message):    
	bot.reply_to(message, "What is your vehicle's mileage")

def getMileage(message):
    mileage = message.text
    print("Mileage is "+mileage)
    if(mileage!=0):
        bot.reply_to(message, "Please Enter the total travel distance (In Kilometers)")
        return True
    else:
        return False    

def getDistance(message1):
    distance = message1.text
    print("Distance is "+distance)
    if(distance!=0):
        bot.reply_to(message1, "What is the cost per liter of fuel?")
        return True
    else:
        return False
    
@bot.message_handler(func=getDistance)
def echo_message(message1):
    distance = message1.text
    user_name = message1.from_user.first_name



@bot.message_handler(func=getMileage)
def echo_message(message):
    distance = message.text
    user_name = message.from_user.first_name

bot.infinity_polling()