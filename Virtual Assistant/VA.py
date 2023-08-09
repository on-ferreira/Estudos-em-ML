'''
Assistente Virtual Usando Processamento de Linguagem Natural



'''
from vosk import Model, KaldiRecognizer
import os
from datetime import datetime
import pyjokes
import wikipedia
import pyaudio
import webbrowser
import winshell
from pygame import mixer, time as t
import time
import pyttsx3
import json


# Validacao da pasta de modelo
# È necessário criar a pasta model-br a partir de onde estiver este fonte
if not os.path.exists("model-br"):
    print("Modelo em portugues nao encontrado.")
    exit(1)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
stream.start_stream()

# Apontando o algoritmo para ler o modelo treinado na pasta "model-br"
model = Model("model-br")
rec = KaldiRecognizer(model, 16000)


# Inicializando o speaker
speaker = pyttsx3.init()

#    Lingua: portugues do Brasil
#    Velocidade: padrao (200) -45
speaker.setProperty('voice', 'brazil')
rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 45)

#Definindo o idioma da wikipedia
wikipedia.set_lang("pt")


# speak converted audio to text
def speak(text):
    print(f"(Assistant): {text}")
    speaker.say(text)
    speaker.runAndWait()


# get mic audio
def get_audio():
    said = ""
    while True:
        data = stream.read(4000)

        # Convertendo audio em texto
        if rec.AcceptWaveform(data):
            finalResult = json.loads(rec.Result())
            said = finalResult.get("text")
            break
        # Descomente para testar o microfone parcialmente
        # else:
        #     print(rec.PartialResult())
    if len(said) == 0:
        return "Desculpe. Não entendi..."
    return said.lower()

#Function to respond the commands
def respond(text):
    if text == 'Desculpe. Não entendi...':
        speak(text)
        return
    print(f"(log) Você disse: {text}")
    if 'que horas' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        speak(strTime)
    elif 'youtube' in text:
        speak("What do you want to search for?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Isso é o que achei por {keyword} no youtube")
    elif 'limpar lixeira' in text:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        speak("Lixeira esvaziada")
    elif 'buscar' in text:
        speak("O que deseja buscar?")
        assunto = get_audio()
        if assunto != '':
            resultado = wikipedia.summary(assunto, sentences=3)
            speak("De acordo com o Wikipedia:")
            speak(resultado)
    elif 'adeus' in text:
        speak("Até a próxima.")
        exit()



while True:
    speak("Estou ouvindo.")
    text = get_audio()
    respond(text)
