# Импортируем необходимые классы.
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler

BOT_TOKEN = "TOKEN"


# Определяем функцию-обработчик сообщений.
# У неё два параметра, updater, принявший сообщение и контекст - дополнительная информация о сообщении.
async def echo(update, context):
    s = update.message.text
    ans = ""
    # цитаты из СМЕШАРИКОВ АХХАХХААХАХ как я до этого додумался ХХАХАХАХ
    if "погода" in s:
        ans += "Погода норм. "
    if any(word in s for word in ["бабочка", "лось"]):
        ans += "Я просто выгляжу как лось, а в душе я бабочка. "
    if any(word in s for word in ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c",
        "v", "b", "n", "m"]):
        ans += "ООООООООООУ CANADA! "
    if "бутерброд" in s:
        ans += "Наверное, никого нельзя насильно заставить измениться, даже если он сам об этом просит. В конце концов, если ты созрел, то сможешь измениться и без посторонней помощи, сам. "
    if "чемодан" in s:
        ans += "Очень трудно жить, думая о каждой ошибке, которую ты совершил, поэтому всё плохое забываешь, " \
               "а помнишь только хорошее — очень удобно, но от себя не уйдёшь.Очень трудно жить, думая о каждой " \
               "ошибке, которую ты совершил, поэтому всё плохое забываешь, а помнишь только хорошее — очень удобно, " \
               "но от себя не уйдёшь."
    if "баласт" in s:
        ans += "Вот так всегда: для кого-то балласт, а для кого-то сокровище. "
    if "новости" in s:
        ans += "— Самый полезный опыт, это познать не свой характер, а характер своего друга, и вовремя сделать выводы. \n— Или ноги. "
    if "торжество" in s:
        ans += "В вопросах дружбы размер не имеет значения. "
    if "смерть" in s:
        ans += "УБЕЙТЕ МЕНЯ! я ненавижу СВОЕГО СОЗДАТЕЛЯ! "
    ans += "ок"
    await update.message.reply_text(ans)

async def start(update, context):
    """Отправляет сообщение когда получена команда /start"""
    await update.message.reply_text(
        "Привет ! Не пиши мне >_< ")

async def help_command(update, context):
    """Отправляет сообщение когда получена команда /help"""
    await update.message.reply_text("Я ничего не умею, не задавайте мне лишних вопросов ")

def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    # Регистрируем обработчик в приложении.
    application.add_handler(MessageHandler(filters.TEXT, echo))

    # Запускаем приложение.
    application.run_polling()


if __name__ == '__main__':
    main()
