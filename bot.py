import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from parser import parse_query
from lardi_auth import login_lardi, search_lardi

BOT_TOKEN = "8133529792:AAGfz8tC8JhGQe7kMBVi1j_DeBZpeo4wlGk"

# 🔐 ДАННЫЕ LARDI (лучше отдельный аккаунт)
LARDI_EMAIL = "email@lardi.com"
LARDI_PASSWORD = "password"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# 🔑 логинимся один раз при старте
lardi_session = login_lardi(LARDI_EMAIL, LARDI_PASSWORD)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "🚛 TransEuroLogistics Cargo Bot\n\n"
        "Пример:\nКиев Львов 20 тонн сегодня"
    )

@dp.message()
async def text_handler(message: types.Message):
    q = parse_query(message.text)

    if not q["from"] or not q["to"]:
        await message.answer("❗ Укажи маршрут: Киев Львов")
        return

    await message.answer("🔍 Ищу грузы на Lardi (авторизованно)...")

    cargos = search_lardi(lardi_session, q["from"], q["to"])

    if not cargos:
        await message.answer("❌ Грузы не найдены")
        return

    text = "🚛 Найденные грузы:\n\n"
    for c in cargos[:5]:
        text += (
            f"{c['from']} → {c['to']}\n"
            f"Вес: {c['weight']}\n"
            f"Цена: {c['price']}\n"
            f"☎️ {c['phone']}\n\n"
        )

    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    