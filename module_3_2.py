

def send_email(message, recipient, *, sender='university.help@gmail.com'):
    rec = list(recipient)
    for i in rec:
        if rec[i] == '@':
            break
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

#    if recipient == sender:
#    print('Нельзя отправить письмо самому себе!')


#    print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

# recipient = 'asdf'
# print(list(recipient))
