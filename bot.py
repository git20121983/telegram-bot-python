from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from lardi_parser import fetch_cargo
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚚 Lardi бот запущен\n\nКоманды:\n/cargo — последние грузы"
    )

async def cargo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        cargos = fetch_cargo()
        if not cargos:
            await update.message.reply_text("❌ Грузы не найдены")
            return

        text = "📦 Последние грузы:\n\n"
        for c in cargos:
            text += (
                f"📍 {c['from']} → {c['to']}\n"
                f"📦 {c['cargo']}\n"
                f"💰 {c['price']}\n\n"
            )

        await update.message.reply_text(text)

    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("cargo", cargo))
    app.run_polling()

if __name__ == "__main__":
    main()
