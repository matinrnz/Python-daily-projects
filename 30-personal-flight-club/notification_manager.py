import os
from telegram import Update
from telegram.ext import *

TOKEN = os.environ.get("TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    pass


# Send each flight as a separate message via Telegram.
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I send you the best flight deals.")


async def flights_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for flight in flights:
        await update.message.reply_text(flight)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update: {update} caused error {context.error}")


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('flights', flights_command))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
