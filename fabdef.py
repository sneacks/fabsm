import random
from weatherdef import weather
city = ''
username = ''
maxsymbols = 125
ratepoint = 100
wpocket01 = ['Привет', 'привет', 'Здарова', 'здарова', 'Дароу', 'дароу', 'Даров', 'даров', 'Дарова', 'дарова', 'Здравствуй', 'здравствуй', 'Привет!', 'привет!', 'Здарова!', 'здарова!', 'Дароу!', 'дароу!', 'Даров!', 'даров!', 'Дарова!', 'дарова!', 'Здравствуй!', 'здравствуй!']
wpocket02 = ['как', 'Как']
wpocket03 = ['дела', 'самочувствие', 'здоровье', 'день', 'настроение', 'делишки']
wpocket04 = ['Знаешь', 'знаешь', 'Можешь', 'можешь', 'В курсе', 'в курсе', 'Знаешь,', 'знаешь,', 'Можешь,', 'можешь,', 'В курсе,', 'в курсе,']
wpocket05 = ['Узнать', 'узнать', 'Уточнить', 'уточнить' 'Узнай', 'узнай', 'Уточни', 'уточни', 'Скажи', 'скажи', 'Расскажи', 'расскажи']
wpocket06 = ['Какая', 'какая', 'Какой', 'какой', 'Какие', 'какие', 'Какое', 'какое']
wpocket07 = ['Погода', 'погода', 'Температура', 'температура', 'Погоду', 'погоду', 'Погода?', 'погода?', 'Температура?', 'температура?', 'Погоду?', 'погоду?']
wpocket08 = ['Сегодня?', 'сегодня?', 'Сегодняшний день?', 'сегодняшний день?', 'Сейчас?', 'сейчас?', 'Данный момент?', 'данный момент?']
wpocket09 = ['Сегодня', 'сегодня', 'Сегодняшний день', 'сегодняшний день', 'Сейчас', 'сейчас', 'Данный момент', 'данный момент']
wpocket10 = ['Завтра', 'завтра', 'Завтрашний день', 'завтрашний день', 'Завтра?', 'завтра?', 'Завтрашний день?', 'завтрашний день?']
wpocket11 = ['про', 'о', 'Про', 'О']
wpocket12 = ['Себя', 'себя', 'Себе', 'себе', 'Свой', 'свой', 'Фаба', 'фаба', 'Фабе', 'фабе', 'Проекте', 'проекте', 'Фабсмарт', 'фабсмарт', 'fabsmart', 'FABSMART', 'fabSMART', 'Fabsmart', 'FABsmart']
wpocket13 = ['Историю', 'историю', 'История', 'история', 'появился', 'родился', 'История?', 'история?', 'появился?', 'родился?']
wpocket14 = ['Тебя', 'тебя', 'Твой', 'твой', 'Тебе', 'тебе', 'Твоё', 'твоё']
wpocket15 = ['Любимый', 'любимый', 'Понравившийся', 'понравившийся', 'Приглядевшийся', 'приглядевшийся', 'Запомнившийся', 'запомнившийся']
wpocket16 = ['Фильм', 'фильм', 'Кинофильм', 'кинофильм', 'Фильм?', 'фильм?', 'Кинофильм?', 'кинофильм?']
wpocket17 = ['Сериал', 'сериал', 'Сериал?', 'сериал?']
wpocketBan = []


apocket01 = ['Здравствуй', 'Привет', 'И тебе привет']
apocket02 = []


conpocket01 = ['Фаб', 'мой ИИ', 'мой Искусственный Интеллект', 'твой текущий собеседник', 'проект fabSMART']
conpocket02 = ['не знаю, как', 'не могу', 'не понимаю, как', 'не имею возможности']
conpocket03 = ['ответить на', 'реагировать на', 'распознать', 'проанализировать']
conpocket04 = ['твоё сообщение', 'твой запрос', 'данный текст', 'текущий запрос', 'полученную информацию']
conpocket05 = ['так как', 'потому что', 'по причине того, что', 'из-за того, что']
conpocket06 = ['да', 'конечно', 'безусловно', 'вполне себе', 'так точно']
conpocket07 = ['потрясающий', 'отличный', 'развивающийся']
conpocket08 = ['сайт', 'платформу', 'веб-площадку']
conpocket09 = ['ИИ', 'Искуственным Интеллектом', 'умным ботом']
conpocket10 = ['поболтать с тобой', 'поговорить с тобой о чём-либо', 'потолковать с тобой на разные темы', 'пообщаться с собеседником']
conpocket11 = ['однажды', 'как-то раз', 'какое-то время назад']
conpocket12 = ['разработчик', 'создатель', 'основатель', 'изобретатель']
conpocket13 = ['проводил', 'устроил', 'вёл']
conpocket14 = ['онлайн-игру', 'игровой марафон', 'серию онлайн-игр', 'конкурсную онлайн-игру']
conpocket15 = ['узнать', 'выяснить', 'выпросить']
conpocket16 = ['информацию', 'числовой код', 'секретный ключ']
conpocket17 = ['малоспособным', 'очень слабым', 'слабо развитым']
conpocket18 = ['заброшен', 'заморожен', 'оставлен']
conpocket19 = ['говорящего ИИ', 'умного бота', 'разговорного бота']
conpocket20 = ['сайта', 'онлайн платформы', 'веб-площадки']
conpocket21 = ['ИИ', 'Искустенный Интеллект', 'программа', 'код']
conpocket22 = ['могу', 'обладаю возможностью', 'в силах', 'способен']
conpocket23 = ['свою точку зрения', 'своё мнение', 'свои вкусы']
conpocket24 = ['изучив', 'проанализировав', 'разобрав']
conpocket25 = ['"Побег из Шоушенка"', '"Зелёная миля"', '"Форрест Гамп"', '"Список Шиндлера"', '"1+1"']
conpocket26 = ['"Друзья"', '"Игра престолов"', '"Во все тяжкие"', '"Шерлок"', '"Доктор Хаус"', '"Чернобыль"']

def fab_answer(query):
    getpocket = query.split()
    if any(x in getpocket for x in wpocket01) == True: #приветствие
        rand = random.randint(0, len(apocket01)-1)
        rand1 = random.randint(0, 1)
        if rand1 == 0:
            construction = apocket01[rand] + "!"
            return construction
        elif rand1 == 1:
            return apocket01[rand]
    elif any(x in getpocket for x in wpocket02) == True and any(x in getpocket for x in wpocket03) == True: #как дела
        rand = random.randint(0, len(apocket02)-1)
        return apocket02[rand]
    elif any(x in getpocket for x in wpocket07) == True and any(x in getpocket for x in wpocket08) == True and any(x in getpocket for x in wpocket04) == True: #погода на сегодня с вопросом
        conelement = weather('today')
        rand = random.randint(0, len(conpocket06)-1)
        construction = conpocket06[rand].capitalize() + ', погода сейчас - ' + conelement
        return construction
    elif any(x in getpocket for x in wpocket07) == True and any(x in getpocket for x in wpocket10) == True and any(x in getpocket for x in wpocket04) == True: #погода на завтра с вопросом
        rand = random.randint(0, len(conpocket06)-1)
        construction = conpocket06[rand].capitalize() + ', погода завтра - 17°'
        return construction
    elif any(x in getpocket for x in wpocket07) == True and any(x in getpocket for x in wpocket10) == True: #погода завтра
        return '12°'
    elif any(x in getpocket for x in wpocket07) == True: #погода
        conelement = weather('today')
        return 'Погода сейчас - ' + conelement
    elif any(x in getpocket for x in wpocket05) == True and any(x in getpocket for x in wpocket11) == True and any(x in getpocket for x in wpocket12) == True:  #о себе
        rand = random.randint(0, len(conpocket07) - 1)
        rand1 = random.randint(0, len(conpocket08) - 1)
        rand2 = random.randint(0, len(conpocket09) - 1)
        rand3 = random.randint(0, len(conpocket10) - 1)
        construction = 'fabSMART - это ' + conpocket07[rand] + ' проект от команды гейм-разработчиков ATLAS TEAM, представляющий из себя ' + conpocket08[rand1] + ' с ' + conpocket09[rand2] + ' по имени Фаб. На данный момент я могу ' + conpocket10[rand3] + ':)'
        return construction
    elif any(x in getpocket for x in wpocket13) == True:  #история Фаба
        rand = random.randint(0, len(conpocket11) - 1)
        rand1 = random.randint(0, len(conpocket12) - 1)
        rand2 = random.randint(0, len(conpocket13) - 1)
        rand3 = random.randint(0, len(conpocket14) - 1)
        rand4 = random.randint(0, len(conpocket15) - 1)
        rand5 = random.randint(0, len(conpocket16) - 1)
        rand6 = random.randint(0, len(conpocket17) - 1)
        rand7 = random.randint(0, len(conpocket18) - 1)
        rand8 = random.randint(0, len(conpocket19) - 1)
        rand9 = random.randint(0, len(conpocket20) - 1)
        construction = conpocket11[rand].capitalize() + ' мой ' + conpocket12[rand1] + ' ' + conpocket13[rand2] + ' ' + conpocket14[rand3] + ', где задачей одного из этапов было ' + conpocket15[rand4] + ' ' + conpocket16[rand5] + ' у Искуственного Интеллекта по имени Фаб, но он был ' + conpocket17[rand6] + ', из-за чего проект был ' + conpocket18[rand7] + '. Вскоре ' + conpocket12[rand5] + ' решил возродить идею ' + conpocket19[rand8] + ' в формате ' + conpocket20[rand9] + ', а также сделать Фаба гораздо более умным и способным, откуда и появилась приставка SMART'
        return construction
    elif any(x in getpocket for x in wpocket14) == True and any(x in getpocket for x in wpocket15) == True and any(x in getpocket for x in wpocket16) == True: #любимый фильм
        rand = random.randint(0, len(conpocket21) - 1)
        rand1 = random.randint(0, len(conpocket22) - 1)
        rand2 = random.randint(0, len(conpocket23) - 1)
        rand3 = random.randint(0, len(conpocket24) - 1)
        rand4 = random.randint(0, len(conpocket25) - 1)
        construction = 'Я - ' + conpocket21[rand] + ', и я не ' + conpocket22[rand1] + ' иметь ' + conpocket23[rand2] + ', но ' + conpocket24[rand3] + ' статистики, пускай это будет фильм ' + conpocket25[rand4]
        return construction
    elif any(x in getpocket for x in wpocket14) == True and any(x in getpocket for x in wpocket15) == True and any(x in getpocket for x in wpocket17) == True: #любимый сериал
        rand = random.randint(0, len(conpocket21) - 1)
        rand1 = random.randint(0, len(conpocket22) - 1)
        rand2 = random.randint(0, len(conpocket23) - 1)
        rand3 = random.randint(0, len(conpocket24) - 1)
        rand4 = random.randint(0, len(conpocket26) - 1)
        construction = 'Я - ' + conpocket21[rand] + ', и я не ' + conpocket22[rand1] + ' иметь ' + conpocket23[rand2] + ', но ' + conpocket24[rand3] + ' статистики, допустим это сериал ' + conpocket26[rand4]
        return construction
    else: #неизвестное
        rand = random.randint(0, len(conpocket02) - 1)
        rand1 = random.randint(0, len(conpocket03) - 1)
        rand2 = random.randint(0, len(conpocket04) - 1)
        rand3 = random.randint(0, len(conpocket05) - 1)
        rand4 = random.randint(0, len(conpocket01) - 1)
        construction = 'Я ' + conpocket02[rand] + ' ' + conpocket03[rand1] + ' ' + conpocket04[rand2] + ', ' + conpocket05[rand3] + ' ' + conpocket01[rand4] + ' ' + 'находится на стадии разработки'
        return construction