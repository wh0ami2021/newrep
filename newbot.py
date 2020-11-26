#-*-coding: utf-8-*-

import telebot
import sys
import settings
import menu
import config
import time

def start_bot():

    bot = telebot.TeleBot(config.bot_token)

    @bot.message_handler(commands=['start'])
    def start_message(message):
     bot.send_message(message.chat.id, settings.start_text.format(firstname = message.chat.first_name))
     bot.send_message(message.chat.id, "⬇️Выберите город⬇️", reply_markup=menu.cities_menu)
     print ("Бота запустил пользователь",message.chat.username)

    @bot.message_handler(content_types=["text"])
    def next_menu(message):
         userid = message.chat.id
         if message.text in menu.rayon_list:
            settings.rayondict[userid] = message.text
            bot.send_message(message.chat.id, "📢Ознакомтесь со всей информацией о кладах 📢", reply_markup=menu.help_menu)
            print("Пользователь",message.chat.username, "выбрал район")
         if message.text in menu.tovar_list:
             print("Пользователь",message.chat.username, "выбрал товар и находится в меню оплаты")
             settings.tovardict[userid] = message.text
             settings.pricedict[userid] = menu.tovar_list[message.text]
             buy_text = "➖➖➖➖➖➖➖➖➖➖\n" \
               "Вы выбрали: \n" \
               f"Город: {settings.citydict[userid]} \n" \
               f"Район:{settings.rayondict[userid]}\n" \
               f"Товар: {settings.tovardict[userid]}\n" \
               "➖➖➖➖➖➖➖➖➖➖\n" \
               "Вы зарезервировали товар \n" \
               "на 30⌛ минут, ранее \n" \
               "зарезервированные заказы сняты с резерва.\n" \
               "Чтобы получить координаты/фото " \
               "товара - Совершите платёж на QIWI.\n" \
               "➖➖➖➖➖➖➖➖➖➖\n" \
               f"🏷️QIWI кошелек: {config.qiwi_number} \n" \
               f"💲Сумма к оплате: {settings.pricedict[userid]} рублей\n" \
               "💬Комментарий к платежу: 40257 \n" \
               "➖➖➖➖➖➖➖➖➖➖ \n" \
               "Сумма платежа должна быть "  \
               "равна указаной выше или больше.\n" \
               "Разрешается оплата частями с указанием " \
               "вашего комментария к платежу.\n" \
               "Платежи обрабатывает робот каждые 3-5 минут.\n" \
               "➖➖➖➖➖➖➖➖➖➖ \n" \
               f"Если вы хотите оплатить с Помощью BITCOIN, то переведите сумму эквивалентную {settings.pricedict[userid]} рублям на зарезервированный для вас BITCOIN адрес:\n" \
               f"{config.bitcoin_adress}"
             bot.send_message(message.chat.id, buy_text, reply_markup=menu.buy_menu)
         if message.text == "📢 Информация":
             bot.send_message(message.chat.id, settings.info_text, reply_markup=menu.help_menu)
         if message.text == "❓ Помощь":
              bot.send_message(message.chat.id, settings.help_text, reply_markup=menu.help_menu)
         if message.text == "Вернутся к выбору города":
              bot.send_message(message.chat.id, "⬇️Выберите город⬇️", reply_markup=menu.cities_menu)   
         if message.text == "Перейти к выбору товара":
              bot.send_message(message.chat.id, "⬇️Выберите товар⬇️", reply_markup=menu.drugs_menu)
              #cities
         if message.text == "♦️ Сертолово":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.moscow_menu)
              settings.citydict[userid] = "♦️Сертолово"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Санкт-Петербург":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.spb_menu)
              settings.citydict[userid] = "♦️ Санкт-Петербург"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Тула":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.tula_menu)
              settings.citydict[userid] = "♦️ Тула"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Екатеринбург":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.ekb_menu)
              settings.citydict[userid] = "♦️ Екатеринбург"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Барнаул":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.barnaul_menu)
              settings.citydict[userid] = "♦️ Барнаул"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Томск":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.tomsk_menu)
              settings.citydict[userid] = "♦️ Томск"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Тюмень":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.tumen_menu)
              settings.citydict[userid] = "♦️ Тюмень"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Нижний Новгород":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.nn_menu)
              settings.citydict[userid] = "♦️ Нижний Новгород"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Самара":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.samara_menu)
              settings.citydict[userid] = "♦️ Самара"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Омск":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.omsk_menu)
              settings.citydict[userid] = "♦️ Омск"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Саратов":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.saratov_menu)
              settings.citydict[userid] = "♦️ Саратов"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Краснодар":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.krasnodar_menu)
              settings.citydict[userid] = "♦️ Краснодар"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Воронеж":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.voronej_menu)
              settings.citydict[userid] = "♦️ Воронеж"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Казань":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.kasan_menu)
              settings.citydict[userid] = "♦️ Казань"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Пермь":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.perm_menu)
              settings.citydict[userid] = "♦️ Пермь"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Новосибирск":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.ns_menu)
              settings.citydict[userid] = "♦️ Новосибирск"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "♦️ Челябинск":
              bot.send_message(message.chat.id, "⬇️Выберите район⬇️", reply_markup=menu.chel_menu)
              settings.citydict[userid] = "♦️ Челябинск"
              print("Пользователь",message.chat.username, "выбрал город")
         if message.text == "✅Я оплатил товар!":
              time.sleep(3)
              bot.send_message(message.chat.id, "❌Платеж не найден. Попробуйте ещё раз через несколько минут", reply_markup=menu.buy_menu)
              print("Пользователь",message.chat.username, "подтвердил оплату")

           #random text
         if message.text not in menu.all_list:
               start_text = "💥 Duck Drug 💥 \n" \
                      "💥Telegram24💥\n" \
                      "➖➖➖➖➖➖\n" \
                      f"{message.chat.first_name} привет!💥\n" \
                      "Тут ты можешь совершить покупку и получить \n" \
                      "свой товар в автоматическом режиме сразу после оплаты.\n" \
                      "Выдача адресов круглосуточно без участия оператора!\n" \
                      "Быстро, удобно и безопасно.🔒\n" \
                      "Приятного отдыха \n"  \
                      "➖➖➖➖➖\n" \
                      "Внимательней проверяйте адрес телеграмм, много фейков.\n" \
                      "➖➖➖➖➖➖\n" \
                      "В случае проблем - работает поддержка:\n" \
                      "@DuckSup\n"  \
                      "Поддержка не занимается продажами.\n" \
                      "Так же требуются сотрудники, залог от 10к.\n" \
                      "Желательно с опытом. \n" \
                      "➖➖➖➖➖➖\n"
               bot.send_message(message.chat.id, settings.start_text.format(firstname = message.chat.first_name))
               bot.send_message(message.chat.id, "⬇️Выберите город⬇️", reply_markup=menu.cities_menu)

    bot.polling(none_stop=True)

start_bot()