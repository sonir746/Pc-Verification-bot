import os
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start_handler import start
from handlers.verify_handler import verify


BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Missing BOT_TOKEN in .env file")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("verify", verify))
    app.run_polling()

if __name__ == "__main__":
    main()
