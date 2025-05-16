import telebot
from telebot import types

TOKEN = '7608914046:AAFe2n9kwq1Mkd6WGwqDq6vmYTPIJ-FPPIY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    if not user_name:
        user_name = "друг"  # Запасной вариант, если имя не указано

    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(
        text="OPEN",
        web_app=types.WebAppInfo(url="https://speech-pro.ru")
    )
    markup.add(button)

    bot.send_photo(
        chat_id=message.chat.id,
        photo=open('123.jpg', 'rb'),
        caption=f"""
        Привет, {user_name}! Я Спикс! 
На связи SpeechPro — твой ИИ-помощник по публичным выступлениям и прокачке коммуникаций🎤
    
Хочешь говорить уверенно, ярко и убедительно? 🌟
Мы поможем прокачать навыки твоего ораторского искусства на основе видеоанализа.
        
📸 Запиши или загрузи видео
📈 Получи разбор речи и невербальных сигналов
🦉 Получи практические рекомендации
        
Готов стать первоклассным оратором? Присылай видео и вперёд! 🔥
        """,
        reply_markup=markup
    )

bot.pollin