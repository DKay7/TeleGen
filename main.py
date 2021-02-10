import telebot
from model import Model
from user import User
from config import token

model = Model()
bot = telebot.TeleBot(token)
users_dict = dict()


@bot.message_handler(commands=['start'])
def start(message):
    user = User(message.from_user.id)
    users_dict[message.from_user.id] = user

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}.\n'
                                      f'Я бот, умеющий генерировать небольшие научные новости.\n\n'
                                      f'Введите начальный текст (несколько или одно слово, или буква),'
                                      f'чтобы начать генерацию')

    bot.register_next_step_handler(message, generate_text)


def generate_text(message):
    bot.send_message(message.chat.id, 'Начинаю работу!')
    result = model.generate(message.text)
    bot.send_message(message.chat.id, 'Закончил')
    bot.send_message(message.chat.id, result)
    bot.send_message(message.chat.id, 'Введите /start, чтобы сгенерировать что-то еще')


bot.polling()
