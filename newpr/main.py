while True:
    import sounddevice as sd
    import numpy as np
    import scipy.io.wavfile as wav
    import speech_recognition as sr
    from googletrans import Translator

    duration = 5  # секунды записи
    sample_rate = 44100

    print("Говори...")
    recording = sd.rec(
    int(duration * sample_rate), # длительность записи в сэмплах
    samplerate=sample_rate,      # частота дискретизации
    channels=1,                  # 1 — это моно
    dtype="int16")               # формат аудиоданных
    sd.wait()  # ждём завершения записи

    wav.write("output.wav", sample_rate, recording)
    print("Запись завершена, теперь распознаём...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        lang = input("Введите код языка для перевода (например, 'en' — английский, 'es' — испанский): ")
        text = recognizer.recognize_google(audio, language="ru-RU")
        print("Ты сказал:", text)
        translator = Translator()
        translated = translator.translate(text, dest='en')  # здесь 'en' — это английский
        print("🌍 Перевод на английский:", translated.text)

    except sr.UnknownValueError:            
        print("Не удалось распознать речь.")
    except sr.RequestError as e:           
        print(f"Ошибка сервиса: {e}")

    a = int(input("Будешь еще переводить?"))
    if a == "да" or a == "Да":
        continue
    elif a == "нет" or a == "Нет":
        break
    else:
        print("Введите да или нет")
        a = int(input("Будешь еще переводить?"))
        if a == "да" or a == "Да":
            continue
        elif a == "нет" or a == "Нет":
            break