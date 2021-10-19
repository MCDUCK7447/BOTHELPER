# --- Подключаем необходимые библиотеки, импортируем модули: ---
# Импортируем Бота, типы обрабатываемой информации
from aiogram import Bot, types
# Импортируем Dispatcher (нужен для создания handler'ов ('держателей' сообщения))
from aiogram.dispatcher import Dispatcher
# Импортируем машину состояний (FSM)
from aiogram.dispatcher import FSMContext
# Импортируем Класс StatesGroup и экземпляры Класса State
from aiogram.dispatcher.filters.state import State, StatesGroup
# Импортируем хранилище состояний в оперативной памяти
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# Импортируем executor нужен для постоянной работы бота (Поллинга))
from aiogram.utils import executor
# Импортируем из библиотеки Pillow модуль Image (для создания и работы с изображениями)
from PIL import Image

# --- Подключаем встроенные модули: ---
# random - для генерации псевдослучайных чисел
import random
# io - для бинарного вывода
import io

# --- Импортируем содержимое других файлов (Структуризация проекта): ---
# Импортируем словарь для хранения данных о пользователе, как "UD"
from UserData import User_Data as UD
# Импортируем Клавиатуры
import markups as marks
# Импортируем словари с Вопросами и ответами
from SubjectFormulas import dict_physics, dict_chem
# Импортируем Токен (В качестве минимальных мер безопасности
# Лучше хранить Токен в другом файле или в качестве Виртуальной переменной)
from settings import TOKEN

# --- Присваивание переменной объекта хранилища ---
storage = MemoryStorage()

# --- Добавление Бота: ---
# Присваиваем Боту наш Токен
bot = Bot(token=TOKEN)
# Передаём Бота, объект хранилища в параметр storage
dp = Dispatcher(bot, storage=storage)

# --- Класс Машины состояний: ---
class FSM_subject(StatesGroup):
    answer = State()
    # Присваиваем переменной экземпляр Класса State

# --- Генерация Главного Меню: ---
def get_Main_Menu():
    # Присваиваем переменной клавиатуру Главного Меню
    Main_Menu = marks.Inline_Main_Menu
    # Возвращаем переменную
    return Main_Menu

# --- Генерация Меню "Прочее": ---
def get_Other_Menu():
    # Присваиваем переменной клавиатуру Меню "Прочее"
    Other_Menu = marks.Inline_Other_Menu
    # Возвращаем переменную
    return Other_Menu

# --- Генерация Меню Выбора Предмета: ---
def get_Choose_Subject_Menu():
    # Присваиваем переменной клавиатуру Меню Выбора Предмета
    Subject_Menu = marks.Inline_Choose_Subject_Menu
    # Возвращаем переменную
    return Subject_Menu

# --- Генерация изображения по ФИЗИКЕ (передаём аргумент Inline кнопки) (*): ---
def get_physics_picture(call):
    # Создаём список позиций формул по оси Ординат
    list_y_pos = [100, 350, 550, 790]
    # Перемешиваем его случайным образом
    random.shuffle(list_y_pos)

    # Добавляем к id пользователя (Ключ словаря UD) номер его верного ответа (Значение ключа)
    if list_y_pos[0] == 100:
        UD[call.from_user.id] = 1
    elif list_y_pos[0] == 350:
        UD[call.from_user.id] = 2
    elif list_y_pos[0] == 550:
        UD[call.from_user.id] = 3
    elif list_y_pos[0] == 790:
        UD[call.from_user.id] = 4

    # Выводим словарь (Для наглядности)
    print(UD)

    # Создаём фоновое изображение:
    # Присваиваем переменной созданное изображение (Формат: RGB, Размер: 1000x1000 пикс., Цвет: Чёрный)
    image = Image.new(mode='RGB', size=(1000, 1000), color=(255, 255, 255))

    # Создаём список из ключей (Вопросов) словаря
    list_dict_physics = list(dict_physics)

    # Объявляем переменную Глобальной, для возможности использования во всём коде
    global caption

    # Присваиваем переменной Caption вопрос из списка
    caption = list_dict_physics[random.randint(0, len(dict_physics) - 1)]
    # Присваиваем переменной изображение формулы
    formula_correct_answer = Image.open(dict_physics.get(caption))
    # Накладываем изображение поверх фона
    image.paste(formula_correct_answer, (150, list_y_pos[0]), formula_correct_answer)

    # (**):
    # Присваиваем переменной вопрос из списка (Метод pop удаляет из списка вопросов ранее использованный вопрос)
    caption_2 = list_dict_physics.pop(list_dict_physics.index(caption))
    # Присваиваем переменной вопрос из списка
    caption_2 = list_dict_physics[random.randint(0, len(dict_physics) - 2)]
    # Присваиваем переменной изображение формулы
    formula_2 = Image.open(dict_physics.get(caption_2))
    # Накладываем изображение поверх фона
    image.paste(formula_2, (150, list_y_pos[1]), formula_2)

    # Аналогично (**)
    caption_3 = list_dict_physics.pop(list_dict_physics.index(caption_2), )
    caption_3 = list_dict_physics[random.randint(0, len(dict_physics) - 3)]
    formula_3 = Image.open(dict_physics.get(caption_3))
    image.paste(formula_3, (150, list_y_pos[2]), formula_3)

    # Аналогично (**)
    caption_4 = list_dict_physics.pop(list_dict_physics.index(caption_3))
    caption_4 = list_dict_physics[random.randint(0, len(dict_physics) - 4)]
    formula_4 = Image.open(dict_physics.get(caption_4))
    image.paste(formula_4, (150, list_y_pos[3]), formula_4)

    # Присваиваем переменной бинарный вид
    picture = io.BytesIO()
    # Сохраняем конечное изображение
    image.save(picture, format='PNG')
    # Объявляем переменную Глобальной, для возможности использования во всём коде
    global photo_png
    # Присваиваем переменной декодерированный бинарный код
    photo_png = picture.getvalue()

# --- Аналогично (*): ---
# Генерация изображения по ХИМИИ (передаём аргумент Inline кнопки)
def get_chem_picture(call):
    # --- Создаём список позиций формул по оси Ординат ---
    list_y_pos = [100, 350, 550, 790]
    # --- Перемешиваем его случайным образом ---
    random.shuffle(list_y_pos)

    # --- Добавляем к id пользователя позицию его верного ответа ---
    if list_y_pos[0] == 100:
        UD[call.from_user.id] = 1
    elif list_y_pos[0] == 350:
        UD[call.from_user.id] = 2
    elif list_y_pos[0] == 550:
        UD[call.from_user.id] = 3
    elif list_y_pos[0] == 790:
        UD[call.from_user.id] = 3
    print(UD)
    # --- Создаём фоновое изображение ---
    image = Image.new(mode='RGB', size=(1000, 1000), color=(255, 255, 255))
    # --- Создаём список из ключей (Вопросов) словаря ---
    list_dict_chem = list(dict_chem)

    global caption

    # --- Caption - вопрос из списка ---
    caption = list_dict_chem[random.randint(0, len(list_dict_chem) - 1)]
    formula_correct_answer = Image.open(dict_chem.get(caption))
    image.paste(formula_correct_answer, (150, list_y_pos[0]), formula_correct_answer)

    caption_2 = list_dict_chem.pop(list_dict_chem.index(caption))
    caption_2 = list_dict_chem[random.randint(0, len(dict_chem) - 2)]
    formula_2 = Image.open(dict_chem.get(caption_2))
    image.paste(formula_2, (150, list_y_pos[1]), formula_2)

    caption_3 = list_dict_chem.pop(list_dict_chem.index(caption_2), )
    caption_3 = list_dict_chem[random.randint(0, len(dict_chem) - 3)]
    formula_3 = Image.open(dict_chem.get(caption_3))
    image.paste(formula_3, (150, list_y_pos[2]), formula_3)

    caption_4 = list_dict_chem.pop(list_dict_chem.index(caption_3))
    caption_4 = list_dict_chem[random.randint(0, len(dict_chem) - 4)]
    formula_4 = Image.opendict_chem.get(caption_4))
    image.paste(formula_4, (150, list_y_pos[3]), formula_4)

    picture = io.BytesIO()
    image.save(picture, format='PNG')
    global photo_png
    photo_png = picture.getvalue()

# --- Проверка ответа по ФИЗИКЕ: (***) ---
# Декоратор текстовых сообщений (Вызывается лишь из полученного состояния)
@dp.message_handler(state=FSM_subject.answer)
# Асинхронная функция (message - аргумент текстовых сообщений, state - указанное состояние)
async def check_answers(message: types.Message, state: FSMContext):
    # Асинхронная функция для проверки словаря состояния
    async with state.proxy() as data:
        # Присваиваем ключу словаря значение текстового сообщения
        data['answer'] = message.text
        # Присваиваем переменной значение текстового сообщения (Проверка словаря)
        if data['answer'] == '1️⃣':
            y = 1
        elif data['answer'] == '2️⃣':
            y = 2
        elif data['answer'] == '3️⃣':
            y = 3
        elif data['answer'] == '4️⃣':
            y = 4
        elif data['answer'] == 'Отмена❌':
            y = 'Отмена❌'
        elif data['answer'] == 'Показать ответ✅':
            y = 'Показать ответ✅'
    if y == UD.get(message.from_user.id):
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура)
        await bot.send_message(message.from_user.id,
                               'Правильно✅',
                               reply_markup=marks.Inline_after_answer_phys
                               )
    elif y == 'Отмена❌':
        # Отправляем текстовое сообщение (Кому, Текст, убираем Reply клавиатуру)
        await bot.send_message(message.from_user.id,
                               'Отменил действие🙅‍♂️',
                               reply_markup=types.ReplyKeyboardRemove()
                              )
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура)
        await bot.send_message(message.from_user.id,
                               'Выберите предмет:',
                               reply_markup=get_Choose_Subject_Menu()
                              )
    elif y == 'Показать ответ✅':
        # Отправляем текстовое сообщение (Кому, Текст (значение словаря по ключу id), Inline клавиатура)
        await bot.send_message(message.from_user.id,
                               'Верный ответ: '+str(UD.get(message.from_user.id))
                              )
        await bot.send_message(message.from_user.id,
                               'Чего желаете❓',
                               reply_markup=marks.Inline_after_answer_phys
                              )
    else:
        # Отправляем текстовое сообщение (Кому, Текст (значение словаря по ключу id), Inline клавиатура)
        await bot.send_message(message.from_user.id,
                               'Неправильно❌\nВерный ответ: '+str(UD.get(message.from_user.id)),
                               reply_markup=marks.Inline_after_answer_phys
                              )
    # Выходим из режима FSM (+Очищение словаря)
    await state.finish()

# --- Проверка ответа по ХИМИИ: Аналогично (***) ---
@dp.message_handler(state=FSM_subject.answer)
async def check_answers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text
        if data['answer'] == '1️⃣':
            y = 1
        elif data['answer'] == '2️⃣':
            y = 2
        elif data['answer'] == '3️⃣':
            y = 3
        elif data['answer'] == '4️⃣':
            y = 4
        elif data['answer'] == 'Отмена❌':
            y = 'Отмена❌'
        elif data['answer'] == 'Показать ответ✅':
            y = 'Показать ответ✅'
            
    if y == UD.get(message.from_user.id):
        await bot.send_message(message.from_user.id,
                               'Правильно✅',
                               reply_markup=marks.Inline_after_answer_chem
                               )
    elif y == 'Отмена❌':
        await bot.send_message(message.from_user.id,
                               'Отменил действие🙅‍♂️',
                               reply_markup=types.ReplyKeyboardRemove()
                               )
        await bot.send_message(message.from_user.id,
                               'Выберите предмет:',
                               reply_markup=get_Choose_Subject_Menu()
                               )
    elif y == 'Показать ответ✅':
        await bot.send_message(message.from_user.id,
                               'Верный ответ: '+str(UD.get(message.from_user.id))
                               )
        await bot.send_message(message.from_user.id,
                               'Чего желаете❓',
                               reply_markup=marks.Inline_after_answer_chem
                               )
    else:
        await bot.send_message(message.from_user.id,
                               'Неправильно❌\nВерный ответ: '+str(UD.get(message.from_user.id)),
                               reply_markup=marks.Inline_after_answer_chem
                               )
    await state.finish()

# --- Декоратор команд (Вызывается при отправке /start, /help): ---
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.text == '/start':
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура)
        await message.answer('Приветствую❗️\nЭтот Бот проверяет знание школьного материала\nСкорее пробуй🤖',
                           reply_markup=get_Main_Menu()
                        )
    elif message.text == '/help':
        # Отправляем текстовое сообщение (Кому, Текст)
        await message.answer('Нажми ➡️ /start'
                             )

# --- Декоратор выхода из режима FSM при отправке "Отмена": ---
# Аргументы: Конкретное текстовое сообщение, * выход из любого состояния
# В коде всего одно состояние, но это необходимо для дальнейшей реализации проекта
@dp.message_handler(content_types = 'Отмена❌', state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()

# --- Декоратор callback ответов (При нажатии Inline кнопки): ---
@dp.callback_query_handler()
# Асинхронная функция (call - аргумент полученных ответов при нажатии Inline кнопки)
async def Menu_commands(call: types.callback_query):
    # Удаление сообщений, связанными с Inline кнопками)
    await bot.delete_message(call.from_user.id, call.message.message_id)

    # Проверка полученного аргумента (.data)
    if call.data == 'Главное меню':
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура Главного Меню)
        await bot.send_message(call.from_user.id,
                               'Кликайте, не стесняйтесь 🤖',
                               reply_markup=get_Main_Menu()
                              )
    elif call.data == 'Выбрать предмет':
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура Меню Выбора Предмета)
        await bot.send_message(call.from_user.id,
                               'Выберите предмет:',
                               reply_markup=get_Choose_Subject_Menu()
                              )
    elif call.data == 'Прочее':
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура Меню "Прочее")
        await bot.send_message(call.from_user.id,
                               'Чего желаете❓',
                               reply_markup=get_Other_Menu()
                              )
    elif call.data == 'Отмена':
        # Отправляем текстовое сообщение (Кому, Текст, убираем Reply клавиатуру)
        await bot.send_message(call.from_user.id,
                               'Действие отменено🙅‍♂️',
                               reply_markup=types.ReplyKeyboardRemove()
                              )
        
        # Отправляем текстовое сообщение (Кому, Текст, Inline клавиатура Меню Выбора Предмета)
        await bot.send_message(call.from_user.id,
                               'Выберите предмет:',
                               reply_markup=get_Choose_Subject_Menu()
                              )
        
    # Запрос вопроса по ФИЗИКЕ (****)
    elif call.data == "Физика":
        # Генерируем изображение, передавая аргумент call
        get_physics_picture(call)

        # Входим в FSM режим
        await FSM_subject.answer.set()
        await call.message.answer('Выберите вариант ответа')

        # Отправляем изображение с подписью и Reply клавиатурой
        await bot.send_photo(call.from_user.id,
                             photo_png,
                             caption,
                             reply_markup=marks.Answers_choose
                            )
        await bot.delete_message(call.from_user.id,
                                 call.message.message_id)
        
    # Запрос вопроса по ХИМИИ Аналогично (****)
    elif call.data == 'Химия':
        get_chem_picture(call)

        await FSM_subject.answer.set()
        await call.message.answer('Выберите вариант ответа')

        await bot.send_photo(call.from_user.id,
                             photo_png, caption,
                             reply_markup=marks.Answers_choose
                            )
        await bot.delete_message(call.from_user.id,
                                 call.message.message_id
                                )

# --- Запускаем принятие сообщений: ---
# Если код находится внутри исполняемого файла, то
# Запускаем постоянный опрос сервера Telegram на наличие обновлений
if __name__ == '__main__':
    # skip_updater=True позволяет "проигнорировать накопившиеся необработанные сообщения
    # Наприме, при перезагрузке Бота
    executor.start_polling(dp, skip_updates=True)


