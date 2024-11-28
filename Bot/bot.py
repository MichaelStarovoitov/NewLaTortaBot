import asyncio
from aiogram import Router, F
from aiogram.types import Message
from aiogram import Bot, Dispatcher

from data.config import TOKEN, resultQestionPath
from common.fileWork import write_text_file

class parentBot:
    def __init__(self):
        self.router = Router()
        self.dp = Dispatcher()
        self.bot = Bot(token=TOKEN)
        self.dp.include_router(self.router)
        self.is_polling_active =False

    async def shutdown(self):
        if self.is_polling_active:
            await self.dp.stop_polling()
        await self.bot.session.close()
        await self.dp.storage.close()
    async def processBot(self):
        try:
            self.is_polling_active = True
            await self.dp.start_polling(self.bot)
        except asyncio.CancelledError:
            print("Polling has been cancelled.")
        except (KeyboardInterrupt, SystemExit):
            print("Bot is shutting down...")
        finally:
            self.is_polling_active = False
            await self.shutdown()
    async def runBot(self):
        try:
            print("Start Bot")
            await self.processBot()
        except KeyboardInterrupt:
            print("Program interrupted by user.")

class teleBot(parentBot):
    def __init__(self, neiro, usersList):
        super().__init__()
        self.usersList = usersList
        self.neiro = neiro
        self.register_handlers()
    
    def register_handlers(self):
        @self.router.message(F.text)
        async def echo(message: Message):
            print("=========== start =======================")
            await self.workWithMessage(message)
            # await self.workWithMessageEr(message)
            print("=========== done  =======================")

    async def workWithMessage(self, message):
        print(message.text)
        resultMessage = ''
        try:
            if self.usersList.returnUserById(message.chat.id):
                idTread = self.usersList.returnUserById(message.chat.id)['idThread']
            else:
                idTread = self.neiro.create_thread() 
                self.usersList.appendUser({'idChat':message.chat.id, 'idThread': idTread})
            resultMessage = self.neiro.sendMessage(idTread, message.text)
            # resultMessage= "hello"
        except Exception as ex:
            resultMessage = f'Помилка: забагато запитів у хвилину'
            print(f'error: {ex}')
        write_text_file(resultQestionPath, f'\n==========text==========\n{message.text}\n=======answer======\n{resultMessage}\n')
        await message.answer(resultMessage, parse_mode="Markdown")

    async def workWithMessageEr(self, message):
        print(message.text)
        if self.usersList.returnUserById(message.chat.id):
            idTread = self.usersList.returnUserById(message.chat.id)['idThread']
        else:
            idTread = self.neiro.create_thread() 
            self.usersList.appendUser({'idChat':message.chat.id, 'idThread': idTread})
        resultMessage = self.neiro.sendMessage(idTread, message.text)
        await message.answer(f'{resultMessage}', parse_mode="MarkdownV2")
            

   
      