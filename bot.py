import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from config import BOT_TOKEN
from lardi import search_lardi

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🚚 TransEuroLogistics Cargo Bot\n\n"
        "Пример запроса:\n"
        "Киев Львов 20т 86м3 сегодня"
    )


@dp.message()
async def handle_text(message: types.Message):
    text = message.text.lower()

    try:
        cargos = search_lardi(text)
    except Exception as e:
        await message.answer(f"❌ Ошибка поиска: {e}")
        return

    if not cargos:
        await message.answer("❌ Ничего не найдено")
        return

    for c in cargos:
        await message.answer(
            f"📦 {c['from']} → {c['to']}\n"
            f"⚖️ {c['weight']} т | 📐 {c['volume']} м³\n"
            f"📅 {c['date']}\n"
            f"📞 {c['phone']}"
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
