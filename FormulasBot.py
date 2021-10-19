#Подключаем необходимые библиотеки
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from PIL import Image
import urllib
from urllib.request import urlopen


import random
import io
from io import BytesIO

from UserData import User_Data as UD
import markups as marks
from SubjectFormulas import dict_physics, dict_chem
from settings import TOKEN

storage = MemoryStorage()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

# --- Класс FSM ФИЗИКА ---
class FSM_subject_phys(StatesGroup):
    answer_phys = State()

# --- Класс FSM ХИМИЯ ---
class FSM_subject_chem(StatesGroup):
    answer_chem = State()

# --- Генерация Основного Меню ---
def get_Main_Menu():
    Main_Menu = marks.Inline_Main_Menu
    return Main_Menu

# --- Генерация Прочего ---
def get_Other_Menu():
    Other_Menu = marks.Inline_Other_Menu
    return Other_Menu

# --- Генерация Меню выбора Предмета ---
def get_Choose_Subject_Menu():
    Subject_Menu = marks.Inline_Choose_Subject_Menu
    return Subject_Menu

# --- Функция генерации картинки по ФИЗИКЕ ---
def get_physics_picture(call):
    # --- Создаём список позиций формул по оси Ординат ---
    list_y_pos = [100, 350, 550, 790]
    # --- Перемешиваем его случайным образом ---
    random.shuffle(list_y_pos)

    # --- Добавляем к id пользователя номер его верного ответа ---
    if list_y_pos[0] == 100:
        UD[call.from_user.id] = 1
    elif list_y_pos[0] == 350:
        UD[call.from_user.id] = 2
    elif list_y_pos[0] == 550:
        UD[call.from_user.id] = 3
    elif list_y_pos[0] == 790:
        UD[call.from_user.id] = 4
    print(UD)
    # --- Создаём фоновое изображение ---
    image = Image.new(mode='RGB', size=(1000, 1000), color=(255, 255, 255))
    # --- Создаём список из ключей (Вопросов) словаря ---
    list_dict_physics = list(dict_physics)

    global caption

    # --- Caption - вопрос из списка ---
    caption = list_dict_physics[random.randint(0, len(dict_physics) - 1)]
    formula_correct_answer = Image.open(dict_physics.get(caption))
    image.paste(formula_correct_answer, (150, list_y_pos[0]), formula_correct_answer)

    caption_2 = list_dict_physics.pop(list_dict_physics.index(caption))
    caption_2 = list_dict_physics[random.randint(0, len(dict_physics) - 2)]
    formula_2 = Image.open(dict_physics.get(caption_2))
    image.paste(formula_2, (150, list_y_pos[1]), formula_2)

    caption_3 = list_dict_physics.pop(list_dict_physics.index(caption_2), )
    caption_3 = list_dict_physics[random.randint(0, len(dict_physics) - 3)]
    formula_3 = Image.open(dict_physics.get(caption_3))
    image.paste(formula_3, (150, list_y_pos[2]), formula_3)

    caption_4 = list_dict_physics.pop(list_dict_physics.index(caption_3))
    caption_4 = list_dict_physics[random.randint(0, len(dict_physics) - 4)]
    formula_4 = Image.open(dict_physics.get(caption_4))
    image.paste(formula_4, (150, list_y_pos[3]), formula_4)

    picture = io.BytesIO()
    image.save(picture, format='PNG')
    global photo_png
    photo_png = picture.getvalue()

# --- Функция генерации картинки по ХИМИИ ---
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
    formula_4 = Image.open(dict_chem.get(caption_4))
    image.paste(formula_4, (150, list_y_pos[3]), formula_4)

    picture = io.BytesIO()
    image.save(picture, format='PNG')
    global photo_png
    photo_png = picture.getvalue()

# --- Проверка ответа по ФИЗИКЕ ---
@dp.message_handler(state=FSM_subject_phys.answer_phys)
async def check_answers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_phys'] = message.text
        if data['answer_phys'] == '1️⃣':
            y = 1
        elif data['answer_phys'] == '2️⃣':
            y = 2
        elif data['answer_phys'] == '3️⃣':
            y = 3
        elif data['answer_phys'] == '4️⃣':
            y = 4
        elif data['answer_phys'] == 'Отмена':
            y = 'Отмена'
        elif data['answer_phys'] == 'Показать ответ':
            y = 'Показать ответ'
    if y == UD.get(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Правильно!', reply_markup=marks.Inline_after_answer_phys
                               )
    elif y == 'Отмена':
        await bot.send_message(message.from_user.id, 'Отменил действие', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(message.from_user.id, 'Выберите предмет:', reply_markup=get_Choose_Subject_Menu())
    elif y == 'Показать ответ':
        await bot.send_message(message.from_user.id, 'Верный ответ: '+str(UD.get(message.from_user.id)))
        await bot.send_message(message.from_user.id, 'Чего желаете?', reply_markup=marks.Inline_after_answer_phys)
    else:
        await bot.send_message(message.from_user.id, 'Неправильно!\nВерный ответ: '+str(UD.get(message.from_user.id)), reply_markup=marks.Inline_after_answer_phys)

    await state.finish()

# --- Проверка ответа по ХИМИИ ---
@dp.message_handler(state=FSM_subject_chem.answer_chem)
async def check_answers(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer_chem'] = message.text
        if data['answer_chem'] == '1️⃣':
            y = 1
        elif data['answer_chem'] == '2️⃣':
            y = 2
        elif data['answer_chem'] == '3️⃣':
            y = 3
        elif data['answer_chem'] == '4️⃣':
            y = 4
        elif data['answer_chem'] == 'Отмена':
            y = 'Отмена'
        elif data['answer_chem'] == 'Показать ответ':
            y = 'Показать ответ'
    if y == UD.get(message.from_user.id):
        await bot.send_message(message.from_user.id,
                               'Правильно!',
                               reply_markup=marks.Inline_after_answer_chem
                               )

    elif y == 'Отмена':
        await bot.send_message(message.from_user.id,
                               'Отменил действие', reply_markup=types.ReplyKeyboardRemove()
                               )
        await bot.send_message(message.from_user.id,
                               'Выберите предмет:',
                               reply_markup=get_Choose_Subject_Menu()
                               )

    elif y == 'Показать ответ':
        await bot.send_message(message.from_user.id,
                               'Верный ответ: '+str(UD.get(message.from_user.id))
                               )
        await bot.send_message(message.from_user.id,
                               'Чего желаете?',
                               reply_markup=marks.Inline_after_answer_chem
                               )
    else:
        await bot.send_message(message.from_user.id,
                               'Неправильно!\nВерный ответ: '+str(UD.get(message.from_user.id)),
                               reply_markup=marks.Inline_after_answer_chem
                               )
    await state.finish()

# --- Обработчик команд ---
@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    if message.text == '/start':
        await message.answer('Приветствую!\nЭтот бот проверяет знание формул!\nСкорее пробуй!',
                           reply_markup=get_Main_Menu()
                        )
    elif message.text == '/help':
        await message.answer('Нажми ==> /start'
                             )

# --- Выход из режима FSM ---
@dp.message_handler(content_types = 'Отмена', state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    await state.finish()

# --- Обработчик Inline Меню ---
@dp.callback_query_handler()
async def Menu_commands(call: types.callback_query):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == 'Главное меню':
        await bot.send_message(call.from_user.id, 'Кликайте, не стесняйтесь :)', reply_markup=get_Main_Menu())
    elif call.data == 'Выбрать предмет':
        await bot.send_message(call.from_user.id, 'Выберите предмет:', reply_markup=get_Choose_Subject_Menu())
    elif call.data == 'Прочее':
        await bot.send_message(call.from_user.id, 'Чего желаете?', reply_markup=get_Other_Menu())
    elif call.data == 'Отмена':
        await bot.send_message(call.from_user.id, 'Действие отменено', reply_markup=types.ReplyKeyboardRemove())
        await bot.send_message(call.from_user.id, 'Выберите предмет:', reply_markup=get_Choose_Subject_Menu())
    elif call.data == "Физика":
        get_physics_picture(call)

        await FSM_subject_phys.answer_phys.set()
        await call.message.answer('Выберите вариант ответа')

        await bot.send_photo(call.from_user.id, photo_png, caption, reply_markup=marks.Answers_choose)
        await bot.delete_message(call.from_user.id, call.message.message_id)

    elif call.data == 'Химия':
        get_chem_picture(call)

        await FSM_subject_chem.answer_chem.set()
        await call.message.answer('Выберите вариант ответа')

        await bot.send_photo(call.from_user.id, photo_png, caption, reply_markup=marks.Answers_choose)
        await bot.delete_message(call.from_user.id, call.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


