from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🖥️💡 **PC LOGIN ALERT** 💡🖥️\n\n"
        "🔐 *Welcome!* We help you find out **who is using your PC** 👀\n\n"
        "⚡ To get your unique verification code (UID) and secure your system, "
        "please type:\n\n"
        "👉 `/verify`\n\n"
        "🛡️ Stay safe. Stay in control!"
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")
