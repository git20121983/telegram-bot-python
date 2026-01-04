import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message

from lardy import search_lardi


# ================== НАСТРОЙКИ ==================

BOT_TOKEN = "8133529792:AAGfz8tC8JhGQe7kMBVi1j_DeBZpeo4wlGk"

MAX_RESULTS = 5

# если нет cookies — оставь {}
LARDI_COOKIES = {
    # пример:
    # "PHPSESSID": "xxxxxx"
}

# ===============================================

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# ---------- START ----------
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🤖 TransEuroLogistics AI\n\n"
        "Напиши любой текст — я попробую найти актуальные грузы с Lardi."
    )


# ---------- ПОИСК ГРУЗОВ ----------
@dp.message()
async def find_cargo(message: Message):
    await message.answer("🔍 Ищу грузы, подожди...")

    cargos = search_lardi(
        limit=MAX_RESULTS,
        cookies=LARDI_COOKIES
    )

    if not cargos:
        await message.answer("❌ Грузы не найдены")
        return

    text = "📦 Найденные грузы:\n\n"

    for i, cargo in enumerate(cargos, start=1):
        text += f"#{i}\n{cargo['title']}\n"
        text += "──────────────\n"

    await message.answer(text)


# ---------- MAIN ----------
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
