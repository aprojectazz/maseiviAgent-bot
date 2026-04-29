import telebot
from telebot import types
from flask import Flask, request

# التوكن الجديد الخاص بك
TOKEN = "8704677505:AAG42msKUP_yiiHe_8kdZcSdvL6A7Ko9ShY"
bot = telebot.TeleBot(TOKEN)

# هذا هو السطر الذي يطلبه Vercel
app = Flask(_name_)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('🚀 سحب فرص مصرفي')
    btn2 = types.KeyboardButton('💳 شحن (بنكيلي/مصرفي)')
    btn3 = types.KeyboardButton('💰 سحب أرباح')
    btn4 = types.KeyboardButton('📞 تواصل مع الوكيل')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "🇲🇷 مرحباً بك في بوت وكيل مصرفي المعتمد.", reply_markup=markup)

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Error", 403

@app.route('/', methods=['GET'])
def index():
    return "Bot is running...", 200

# تأكد أن اسم المتغير هنا هو app ليتعرف عليه Vercel
application = app
