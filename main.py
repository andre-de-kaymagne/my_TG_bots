from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.client.default import DefaultBotProperties

BOT_TOKEN = '7654302347:AAEHgc6nykQ4EOmJ8qin2NsPULE1k5aSUBg'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
# Создаем объекты инлайн-кнопок
url_button_1 = InlineKeyboardButton(
    text='Наша страница на Яндекс Картах', url="https://yandex.ru/maps/org/klinika_nuriyevykh/12426919696/reviews/?ll=49.199797%2C55.756041&z=14"
)

url_button_2 = InlineKeyboardButton(
    text='Наша страница на Дубль Гис', url="https://2gis.ru/kazan/firm/2956015536454655/tab/reviews"
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2]]
)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        'Здравствуйте, недавно Вы посетили нашу компанию!\n\n' 
        'Ваше мнение очень важно для нас. Оцените, пожалуйста, нашу работу от 1 до 5'
        ' (<b>5</b> - очень хорошо, <b>1</b> - очень плохо).\n\n'
        'Чтобы посмотреть дополнительные опции '
        '- введите команду /help'
        )
    
@dp.message(lambda x: x.text and x.text.isdigit())
async def process_numbers_answer(message: Message):
    if int(message.text) < 4:
        await message.answer(
                'Спасибо за вашу честную оценку! Нам очень жаль и мы готовы усердно работать над ошибками!\n\n'
                'Расскажите, пожалуйста, подробнее, что Вам не понравилось? Что омрачило ваше посещение?'
            )
    elif 5 >= int(message.text) >= 4:
        await message.answer(
                'Нам очень приятно за вашу высокую оценку! '
                'С нетерпением ждем новой встречи с Вами!\n\n'
                'Будем благодарны вашему отзыву на геосервисах:\n\n',
                reply_markup=keyboard
            )

if __name__ == '__main__':
    dp.run_polling(bot)