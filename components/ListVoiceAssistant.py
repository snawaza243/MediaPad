import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice.name)

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     if 'hindi' in voice.name.lower():
#         print(voice.name)