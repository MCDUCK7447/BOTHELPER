from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

'''# --- Back to the Main Menu ---
btn_Main_Menu = KeyboardButton('Главное меню')

# --- Main Menu Buttons ---
btn_choose_subject = KeyboardButton('Выбрать предмет')
btn_other_menu = KeyboardButton('Другое')

Main_Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_choose_subject).add(btn_other_menu)

# --- Other Menu Buttons ---
btn_how_answer = KeyboardButton('Как пользоваться?')
btn_write_dev = KeyboardButton('Связь с разработчиком')

Other_Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_how_answer).row(btn_write_dev, btn_Main_Menu)

# --- Choose Subject Buttons Menu ---
btn_choose_physics = KeyboardButton('Физика')
btn_choose_math = KeyboardButton('Математика')

Choose_subject = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_choose_physics, btn_choose_math).add(btn_Main_Menu)'''

# --- Back to the Main Menu ---
inline_btn_back_to_the_Main_Menu = InlineKeyboardButton('Главное меню', callback_data='Главное меню')

# --- Main Menu Inline Buttons ---
inline_btn_choose_subject = InlineKeyboardButton('Выбрать предмет', callback_data='Выбрать предмет')
inline_btn_other_menu = InlineKeyboardButton('Прочее', callback_data='Прочее')

Inline_Main_Menu = InlineKeyboardMarkup(row_width=1).add(inline_btn_choose_subject,
                                                         inline_btn_other_menu
                                                         )

# --- Other Menu Inline Buttons ---
# inline_how_answer = InlineKeyboardButton('Как пользоваться?',
#                                          callback_data='Как пользоваться?'
#                                          )
inline_write_dev = InlineKeyboardButton('Связь с разработчиком',
                                        url='https://vk.com/mcduck74'
                                        )

Inline_Other_Menu = InlineKeyboardMarkup(row_width=1).add(inline_write_dev,
                                                          inline_btn_back_to_the_Main_Menu
                                                          )

# --- Choose Subject Inline Buttons Menu ---
inline_btn_choose_physics = InlineKeyboardButton('Физика',
                                                 callback_data='Физика'
                                                 )
inline_btn_choose_math = InlineKeyboardButton('Химия',
                                              callback_data='Химия'
                                              )


Inline_Choose_Subject_Menu = InlineKeyboardMarkup(row_width=1).add(inline_btn_choose_physics,
                                                                   inline_btn_choose_math,
                                                                   inline_btn_back_to_the_Main_Menu
                                                                   )

# --- Кнопки выбора ответа ---
btn_answer_1 = KeyboardButton('1️⃣')
btn_answer_2 = KeyboardButton('2️⃣')
btn_answer_3 = KeyboardButton('3️⃣')
btn_answer_4 = KeyboardButton('4️⃣')
btn_cancel = KeyboardButton('Отмена')
btn_show_correct_answer = KeyboardButton('Показать ответ')
Answers_choose = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(btn_answer_1, btn_answer_2, btn_answer_3, btn_answer_4).add(btn_cancel).add(btn_show_correct_answer)


inline_btn_cancel = InlineKeyboardButton('Отмена', callback_data='Отмена')

inline_btn_more_physics = InlineKeyboardButton('Ещё картинку!',
                                                 callback_data='Физика')
Inline_after_answer_phys = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_more_physics).add(inline_btn_cancel)


inline_btn_more_chem = InlineKeyboardButton('Ещё картинку!',
                                                 callback_data='Химия')
Inline_after_answer_chem = InlineKeyboardMarkup(resize_keyboard=True).add(inline_btn_more_chem).add(inline_btn_cancel)













