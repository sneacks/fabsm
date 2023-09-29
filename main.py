from flask import Flask, render_template, request
from fabdef import fab_answer
import sqlite3
import speech_recognition as sr
import json


app = Flask(__name__)
r = sr.Recognizer()
last_ans = 'Вас приветствует Фаб! Старайтесь соблюдать грамматику для более точной работы бота'
last_quest = 'Здесь будет ваш запрос'
last_account_page = '/reg'
page = ''
last_ans1 = ''
last_quest1 = ''

@app.route('/')
def index():
    query = request.args.get("intext")
    global last_ans
    global last_quest
    global page
    global last_ans1
    global last_quest1
    page = 'index'
    last_ans1 = last_ans
    last_quest1 = last_quest
    if not query:
        text = last_ans
        query = last_quest
    else:
        text = fab_answer(query)
        text2 = text
        text3 = query
    if text == "":
        last_ans = text
        last_quest = query
        return render_template("index.html", text=text, text1=query)
    else:
        last_ans = text
        last_quest = query
        return render_template("index.html", text=text, text1=query, text2=last_ans1, text3=last_quest1)

@app.route('/upload', methods=['POST'])
def upload():
    global r
    global query
    global last_ans
    global last_quest
    if request.method == 'POST':
        audio_data = request.files['audio_data'].read()
        with open('upload/audio.wav', 'wb') as f:
            f.write(audio_data)
        with sr.AudioFile('audio.wav') as audio_file:
            audio_data = r.record(audio_file)
            query = r.recognize_google(audio_data, language='ru-RU')
            if not query:
                text = last_ans
                query = last_quest
            else:
                text = fab_answer(query)
                text2 = text
                text3 = query
            if text == "":
                last_ans = text
                last_quest = query
        return render_template("index.html", text=text, text1=query)
    else:
        return 'Bad request'

@app.route('/reg')
def reg():
    global last_account_page
    global page
    if last_account_page == '/account':
        page = 'account'
        return render_template("account_page.html")
    elif last_account_page == '/reg':
        page = 'reg'
        return render_template("reg.html")
    elif page == 'login' and last_account_page == '/login':
        last_account_page = '/reg'
        return render_template("reg.html")
    else:
        page = 'login'
        return render_template("login.html")


@app.route('/offers')
def offers():
    global page
    page = 'offers'
    return render_template("offers.html")

@app.route('/login', methods=['get', 'post'])
def loginform():
    global last_account_page
    last_account_page = '/login'
    global page
    page = 'login'
    if request.method == 'post':
       login = request.form.get('login')
       password = request.form.get('password')
       db_userdata = sqlite3.connect('userdata.db')
       cursor_db = db_userdata.cursor()
       cursor_db.execute(('''SELECT password FROM passwords WHERE login = '{}';''').format(login))
       pas = cursor_db.fetchall()
       cursor_db.close()
       try:
           if pas[0][0] != password:
               return render_template('user_bad.html')
       except:
           return render_template('user_bad.html')
       db_userdata.close()
    return render_template('login.html')

@app.route('/account')
def account():
    global page
    global last_account_page
    page = 'account'
    last_account_page = '/account'
    return render_template("account_page.html")

app.run()