# bot.py
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN, LARDI_COOKIES, MAX_RESULTS
from lardi import search_lardi

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
    parts = message.text.split()
    if len(parts) < 2:
        await message.answer("❗ Введите: Откуда Куда")
        return

    from_city, to_city = parts[0], parts[1]

    await message.answer("🔍 Ищу грузы на Lardi...")

    try:
        cargos = search_lardi(
            from_city,
            to_city,
            limit=MAX_RESULTS,
            cookies=LARDI_COOKIES
        )

        if not cargos:
            await message.answer("❌ Грузы не найдены")
            return

        text = f"📦 Найдено грузов: {len(cargos)}\n\n"
        for c in cargos:
            text += f"▪ {c['title']}\n☎ {c['phone']}\n\n"

        await message.answer(text)

    except Exception as e:
        await message.answer(f"⚠ Ошибка поиска: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
