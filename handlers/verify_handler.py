import secrets
from datetime import datetime, timezone
from telegram import Update
from telegram.ext import ContextTypes
from database.mongo import collection

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = update.effective_chat.username or f"user_{chat_id}"
    captcha = secrets.token_hex(4)

    try:
        collection.update_one(
            {"username": username},
            {
                "$set": {
                    "chat_id": chat_id,
                    "username": username,
                    "code": captcha,
                    "created_at": datetime.now(timezone.utc)
                }
            },
            upsert=True
        )
    except Exception as e:
        await update.message.reply_text(f"⚠️ Database error: {e}")
        return

    await update.message.reply_text(
        f"🔑 **Your verification code is:**\n\n`{captcha}`\n\n"
        f"📌 Your username: `{username}`\n"
        "Enter these in your PC application to complete verification.",
        parse_mode="Markdown"
    )
