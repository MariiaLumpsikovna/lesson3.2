def send_email(message, recipient, *, sender='university.help@gmail.com'):
    letter = 'Невозможно отправить письмо с адреса ' + sender + " на адрес " + recipient
    if '@' not in recipient or '@' not in sender:
        letter = letter
    elif '.com' not in sender and '.ru' not in sender and '.net' not in sender:
        letter = letter
    elif '.com' not in recipient and '.ru' not in recipient and '.net' not in recipient:
        letter = letter
    elif sender == recipient:
        letter = 'Нельзя отправить письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        letter = 'Письмо успешно отправлено с адреса ' + sender + ' на адрес ' + recipient
    else:
        letter = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ' + sender + ' на адрес ' + recipient
    return print(letter)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
