import asyncio
from aiogram import Router, F
from aiogram.types import Message
from aiogram import Bot, Dispatcher

from data.config import TOKEN

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
        try:
            if self.usersList.returnUserById(message.chat.id):
                idTread = self.usersList.returnUserById(message.chat.id)['idThread']
            else:
                idTread = self.neiro.create_thread() 
                self.usersList.appendUser({'idChat':message.chat.id, 'idThread': idTread})
            await message.answer(self.neiro.sendMessage(idTread, message.text), parse_mode="Markdown")
        except Exception as ex:
            await message.answer(f'Помилка: забагато запитів у хвилину')
            print(f'error: {ex}')

    async def workWithMessageEr(self, message):
        print(message.text)
        if self.usersList.returnUserById(message.chat.id):
            idTread = self.usersList.returnUserById(message.chat.id)['idThread']
        else:
            idTread = self.neiro.create_thread() 
            self.usersList.appendUser({'idChat':message.chat.id, 'idThread': idTread})
        await message.answer(f'{self.neiro.sendMessage(idTread, message.text)}', parse_mode="MarkdownV2")
            

   
      