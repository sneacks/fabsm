import speech_recognition as sr

# создаем объект recognizer
r = sr.Recognizer()

# открываем файл audio.wav и записываем аудиоданные в переменную audio_file
with sr.AudioFile('audio.wav') as audio_file:
    audio_data = r.record(audio_file)

# распознаем речь с помощью Google Speech Recognition
text = r.recognize_google(audio_data, language='ru-RU')

# выводим распознанный текст на экран
print(text)