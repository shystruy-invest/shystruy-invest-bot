import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = "8553202091:AAH8_4sS5HaeUjMsC6djI-by1zMhExaCoeI"
CHANNEL_ID = "@shystruy_invest_bot"

def start(update, context):
    update.message.reply_text("Бот SHYSTRUY INVEST працює ✅")

def send_signal(context):
    context.bot.send_message(
        chat_id=CHANNEL_ID,
        text="📊 EURUSD OTC\n🟢 BUY\n⏰ Сигнал згенеровано"
    )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

job_queue = updater.job_queue
job_queue.run_repeating(send_signal, interval=300, first=10)

updater.start_polling()
updater.idle()
