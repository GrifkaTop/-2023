# Импортируем необходимые классы.
import datetime
import re
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler, ConversationHandler
from datetime import datetime

BOT_TOKEN = "TOKEN"


async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я ничего не умею, не задавайте мне лишних вопросов ")


async def time_command(update, context):
    now = datetime.now()
    now_time = now.strftime("%H:%M")
    await update.message.reply_text(f"время сейчас: {now_time}")


async def data_command(update, context):
    now = datetime.now()
    now_data = now.strftime("%A, %d %B %Y")
    await update.message.reply_text(f"время сейчас: {now_data}")


async def day_of_week_command(update, context):
    await update.message.reply_text(f"скинь дату в формате ДД.ММ.ГГГГ ")
    return 1


async def day_of_week_1_response(update, context):
    data = update.message.text
    try:
        date_obj = datetime.strptime(data, '%d.%m.%Y')
        day_of_week = date_obj.strftime("%A")
        await update.message.reply_text(day_of_week)
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text("НЕПРАВИЛЬНЫЙ ФОРМАТ ЕЩЕ РАЗ! ДД.ММ.ГГГГ")
        return 1


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("time", time_command))
    application.add_handler(CommandHandler("data", data_command))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('day_of_week', day_of_week_command)],
        states={
            1: [MessageHandler(filters.TEXT & ~filters.COMMAND, day_of_week_1_response)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )
    application.add_handler(conv_handler)

    application.run_polling()


if __name__ == '__main__':
    main()
