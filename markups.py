# --- Импортируем кнопки и клавиатуры: ---
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# --- Inline клавиатуры и кнопки: ---
# Кнопка Главного Меню
inline_btn_back_to_the_Main_Menu = InlineKeyboardButton('Главное меню',
                                                        callback_data='Главное меню'
                                                        )


# Кнопки Главного Меню
inline_btn_choose_subject = InlineKeyboardButton('Выбрать предмет',
                                                 callback_data='Выбрать предмет'
                                                 )
inline_btn_other_menu = InlineKeyboardButton('Прочее',
                                             callback_data='Прочее'
                                             )
# Клавиатура Главного Меню
Inline_Main_Menu = InlineKeyboardMarkup(row_width=1).add(inline_btn_choose_subject,
                                                         inline_btn_other_menu
                                                         )


# Кнопка Предмета Физики
inline_btn_choose_physics = InlineKeyboardButton('Физика',
                                                 callback_data='Физика'
                                                 )
# Кнопка Предмета Химии
inline_btn_choose_math = InlineKeyboardButton('Химия',
                                              callback_data='Химия'
                                              )
# Клавиатура Меню Выбора Предметов
Inline_Choose_Subject_Menu = InlineKeyboardMarkup(row_width=1).add(inline_btn_choose_physics,
                                                                   inline_btn_choose_math,
                                                                   inline_btn_back_to_the_Main_Menu
                                                                   )


# Кнопки Вариантов развития (Физика)
inline_btn_cancel = InlineKeyboardButton('Отмена',
                                         callback_data='Отмена'
                                         )
inline_btn_more_physics = InlineKeyboardButton('Ещё картинку!',
                                               callback_data='Физика'
                                               )
# Клавиатура Вариантов развития (Физика)
Inline_after_answer_phys = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_more_physics).add(inline_btn_cancel)


# Кнопки Вариантов развития (Химия)
inline_btn_more_chem = InlineKeyboardButton('Ещё картинку!',
                                            callback_data='Химия'
                                            )

# Клавиатура Вариантов развития (Химия)
Inline_after_answer_chem = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_more_chem).add(inline_btn_cancel)


# Кнопка Меню "Прочее"
inline_write_dev = InlineKeyboardButton('Связь с разработчиком',
                                        url='https://vk.com/mcduck74'
                                        )
# Клавиатура Меню "Прочее"
Inline_Other_Menu = InlineKeyboardMarkup(row_width=1).add(inline_write_dev,
                                                          inline_btn_back_to_the_Main_Menu
                                                          )


# --- Reply клавиатуры и кнопки: ---
# Кнопки Reply клавиатуры
btn_answer_1 = KeyboardButton('1️⃣')
btn_answer_2 = KeyboardButton('2️⃣')
btn_answer_3 = KeyboardButton('3️⃣')
btn_answer_4 = KeyboardButton('4️⃣')
btn_cancel = KeyboardButton('Отмена')
btn_show_correct_answer = KeyboardButton('Показать ответ')
# Reply Клавиатура Ответов
Answers_choose = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(btn_answer_1,
                                                                                       btn_answer_2,
                                                                                       btn_answer_3,
                                                                                       btn_answer_4
                                                                                       ).add(btn_cancel).add(btn_show_correct_answer)













