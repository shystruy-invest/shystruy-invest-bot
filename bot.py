import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "8553202091:AAH8_4sS5HaeUjMsC6djI-by1zMhExaCoeI"
CHANNEL_ID = "@shystruy_invest_bot"

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await bot.send_message(
        CHANNEL_ID,
        "📊 ТЕСТОВИЙ СИГНАЛ\n\n"
        "SHYSTRUY INVEST бот успішно запущений ✅"
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
