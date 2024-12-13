# Домашняя работа по уроку ""Способы вызова функции"
# Задача "Рассылка писем":

def send_email(message: str,
               recipient: str,
               *,
               sender: str = "university.help@gmail.com") -> str:
    """
    Функция send_email принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и
    1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com"
    :param message: строка
    :param recipient: строка
    :param sender: строка
    :return: строка
    """

    full_name_recipient = '@' in recipient and (
            not (not recipient.endswith('.com') and not recipient.endswith('.ru')) or recipient.endswith('.net'))
    full_name_sender = '@' in sender and (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))
    if full_name_recipient and full_name_sender:
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            else:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
