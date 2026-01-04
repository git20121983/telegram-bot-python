import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config import BOT_TOKEN, LARDI_EMAIL, LARDI_PASSWORD, MAX_RESULTS
from parser import parse_query
from lardi_client import LardiClient

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

lardi = LardiClient(LARDI_EMAIL, LARDI_PASSWORD)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "🚛 TransEuroLogistics Cargo Bot\n\n"
        "Пример запроса:\n"
        "Киев Львов 20 тонн 86 кубов сегодня"
    )

@dp.message()
async def handle_text(message: types.Message):
    q = parse_query(message.text)

    if not q["from"] or not q["to"]:
        await message.answer("❗ Формат: Киев Львов 20 тонн")
        return

    await message.answer(
        f"🔍 Поиск грузов:\n"
        f"{q['from'].title()} → {q['to'].title()}\n"
        f"Дата: {q['date']}"
    )

    cargos = lardi.search(q["from"], q["to"])

    if not cargos:
        await message.answer("❌ Грузы не найдены")
        return

    reply = "🚛 Найденные грузы:\n\n"

    for c in cargos[:MAX_RESULTS]:
        reply += (
            f"{c['from']} → {c['to']}\n"
            f"Вес: {c['weight']}\n"
            f"Цена: {c['price']}\n"
            f"☎️ {c['phone']}\n\n"
        )

    await message.answer(reply)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
