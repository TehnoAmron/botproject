import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin
from model import get_class  # Импортируем функции из bot_logic

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("8723508225:AAGJ5HqJt8yC3lkqXu2f0t-qIsanmNehTZU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    message.photo
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]


    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file: 
        new_file.write(downloaded_file)
    result = get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=file_name)
    bot.send_message(message.chat.id,result)

# Запускаем бота
bot.polling()


#Наземный транспорт
#Легковые авто: Главные загрязнители воздуха в городах (выхлопные газы). Плюс микропластик от стирающихся шин и токсичные жидкости.
#Грузовики: Сжигают огромное количество дизеля, выбрасывая сажу и оксиды азота. Сильно разрушают дорожное покрытие.
#Автобусы: Вред тот же, что и у грузовиков, но в пересчете на одного пассажира они экологичнее машин.
#Мотоциклы: Часто лишены мощных фильтров, поэтому выбрасывают больше несгоравших веществ, чем современные авто. И, конечно, сильный шумовой вред.
#Велосипед: Прямого вреда при езде нет. Косвенный вред — только при производстве (добыча металла, химия для резины) и утилизации.
#Рельсовый транспорт
#Трамваи и Метро: Считаются чистыми, но всё зависит от того, как добыто электричество (если на угольной ТЭС — вред есть). Метро создает вибрации, которые могут портить фундаменты зданий.
#Поезда: Электрички экологичны, тепловозы же дымят не хуже заводов. Также это серьезное шумовое загрязнение для лесов и поселков.
#Водный транспорт
#Обычная лодка (моторная): Разливы топлива и масла прямо в воду, шум пугает рыбу, а винты могут травмировать водных животных.
#Подводная лодка: Главный риск — ядерные реакторы (у атомных) и сонары, которые сводят с ума китов и дельфинов, сбивая их навигацию.
#Воздушный транспорт
#Самолеты: Огромные выбросы углекислого газа прямо в верхние слои атмосферы, что ускоряет глобальное потепление.
#Вертолеты: Очень неэкономичны (тратят много топлива на малый вес) и создают экстремальный уровень шума.