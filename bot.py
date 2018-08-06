#-*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Teste')

bot.set_trainer(ListTrainer)

for speaks in os.listdir('speaks'):
    chats = open('speaks/' + speaks, 'r').readlines()
    bot.train(chats)

while True:
    resq = input('Você: ')

    resp = bot.get_response(resq)
    
    if float(resp.confidence) > 0.5:
        print('Robô: ' + str(resp))  
    else:
        print('Robô: Não entendi o que você quis dizer.')