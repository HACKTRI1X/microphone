import speech_recognition as sr

# Microphone'dan veri almak için kullanacağımız recognizer objesini oluşturuyoruz.
r = sr.Recognizer()

# Mikrofonu varsayılan cihaz olarak belirliyoruz.
with sr.Microphone() as source:
    print("Dil seçin: 1 - İngilizce, 2 - Türkçe, 3 - Rusça")
    language = input("Seçiminiz: ")

    if language == '1':
        lang = 'en-US'
    elif language == '2':
        lang = 'tr-TR'
    elif language == '3':
        lang = 'ru-RU'
    else:
        print("Geçersiz seçim.")
        exit()

    print("Konuşun...")
    audio = r.listen(source)  # Mikrofondan gelen veriyi dinliyoruz.

try:
    # Konuşmayı metne dönüştürüyoruz.
    text = r.recognize_google(audio, language=lang)
    print("Söylediğiniz metin: {}".format(text))
except sr.UnknownValueError:
    print("Ne dediğinizi anlayamadım.")
except sr.RequestError as e:
    print("Google API hatası: {}".format(e))
