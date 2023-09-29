import random
wpocket01 = ['Привет', 'привет', 'Здарова', 'здарова', 'Дароу', 'дароу',
             'Даров', 'даров', 'Дарова', 'дарова', 'Здравствуй', 'здравствуй']
wpocket02 = ['как', 'Как']
wpocket03 = ['дела', 'самочувствие',
             'здоровье', 'день', 'настроение', 'делишки']
wpocket04 = ['Знаешь', 'знаешь', 'Можешь', 'можешь', 'В курсе', 'в курсе']
wpocket05 = ['Узнать', 'узнать', 'Уточнить', 'уточнить' 'Узнай',
             'узнай', 'Уточни', 'уточни', 'Скажи', 'скажи']
wpocket06 = ['Какая', 'какая', 'Какой',
             'какой', 'Какие', 'какие', 'Какое', 'какое']
wpocket07 = ['Погода', 'погода', 'Температура',
             'температура', 'Погоду', 'погоду']
wpocket08 = ['Сегодня', 'сегодня', 'Сегодняшний день', 'сегодняшний день',
             'Сейчас', 'сейчас', 'Данный момент', 'данный момент']
wpocket09 = ['Завтра', 'завтра', 'Завтрашний день', 'завтрашний день']

apocket01 = ['Здравствуй', 'Привет', 'И тебе привет']
apocket02 = ['Топ', 'Всё плохо(']

conpocket01 = ['Фаб', 'мой ИИ',
               'мой Искусственный Интеллект', 'твой текущий собеседник']
conpocket02 = ['не знаю, как', 'не могу',
               'не понимаю, как', 'не имею возможности']
conpocket03 = ['ответить', 'реагировать на', 'распознать', 'проанализировать']
conpocket04 = ['твоё сообщение', 'твой запрос',
               'данный текст', 'текущий запрос', 'полученную информацию']
conpocket05 = ['так как', 'потому что',
               'по причине того, что', 'из-за того, что']
conpocket06 = ['да', 'конечно', 'безусловно', 'вполне себе', 'так точно']


def fab_answer(query):
    getpocket = query.split()
    if any(x in getpocket for x in wpocket01) == True:  # приветствие
        rand = random.randint(0, len(apocket01)-1)
        rand1 = random.randint(0, 1)
        if rand1 == 0:
            construction = apocket01[rand] + "!"
            return construction
        elif rand1 == 1:
            return apocket01[rand]
    elif any(x in getpocket for x in wpocket02) == True and any(x in getpocket for x in wpocket02) == True:  # как дела
        rand = random.randint(0, len(apocket02)-1)
        return apocket02[rand]
    elif any(x in getpocket for x in wpocket07) == True and any(x in getpocket for x in wpocket08) == True:  # погода сегодня
        return '7°'
    elif any(x in getpocket for x in wpocket07) == True and any(x in getpocket for x in wpocket08) == True and any(x in getpocket for x in wpocket04) == True:  # погода на сегодня с вопросом
        rand = random.randint(0, len(conpocket06)-1)
        construction = conpocket06[rand].capitalize() + ' погода - 6°'
        return construction
    else:
        rand = random.randint(0, len(conpocket02) - 1)
        rand1 = random.randint(0, len(conpocket03) - 1)
        rand2 = random.randint(0, len(conpocket04) - 1)
        rand3 = random.randint(0, len(conpocket05) - 1)
        rand4 = random.randint(0, len(conpocket01) - 1)
        construction = 'Я' + ' ' + conpocket02[rand] + ' ' + conpocket03[rand1] + ' ' + conpocket04[rand2] + \
            ', ' + conpocket05[rand3] + ' ' + conpocket01[rand4] + \
            ' ' + 'находится в стадии разработки'
        return getpocket


ans = str(input('Скажите что-нибудь: \n'))
print(fab_answer(ans))
