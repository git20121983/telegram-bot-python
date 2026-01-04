# bot.py
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN, LARDI_COOKIES, MAX_RESULTS
from lardy import search_lardi

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🚛 TransEuroLogistics Cargo Bot\n\n"
        "Пример запроса:\n"
        "Киев Львов"
    )

@dp.message()
async def text_handler(message: types.Message):
    await message.answer("🔍 Ищу грузы на Lardi...")

    cargos = search_lardi(
        from_city="",
        to_city="",
        limit=5,
        cookies=LARDI_COOKIES
    )

    if not cargos:
        await message.answer("❌ Грузы не найдены")
        return

    text = "📦 Найденные грузы:\n\n"

    for i, c in enumerate(cargos, 1):
        text += (
            f"#{i}\n"
            f"{c['title']}\n"
            f"──────────────\n"
        )

    await message.answer(text)


if __name__ == "__main__":
    asyncio.run(main())
