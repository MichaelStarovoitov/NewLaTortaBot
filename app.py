import asyncio
from Bot.bot import teleBot
from data.userDb import userData
from gpt.assistant import gptAssistant
from data.productDb import productsData

from data.config import usersFile, productsFile, nameBot, propt

if __name__ == '__main__':
   productsList = productsData(productsFile)
   neiro = gptAssistant(nameBot, propt, productsList)
   usersList = userData(usersFile)
   bot = teleBot(neiro,usersList)
   asyncio.run(bot.runBot())