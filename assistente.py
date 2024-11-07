import speech_recognition as sr
import subprocess
import sys
import webbrowser

def abrir_link(url):
    try:
        webbrowser.open(url)
        print(f"Abrindo o link: {url}")
    except Exception as e:
        print(f"Erro ao abrir o link: {e}")

def abrir_steam():
    try:
        subprocess.Popen(["E:\Steam\\steam.exe"])  # Caminho para o executável do Steam
        print("Abrindo Steam...")
    except Exception as e:
        print(f"Erro ao abrir Steam: {e}")

def abrir_firefox():
    try:
        subprocess.Popen(["C:\Program Files\Mozilla Firefox\\firefox.exe"])  # Caminho para o executável do Firefox
        print("Abrindo Firefox...")
    except Exception as e:
        print(f"Erro ao abrir Firefox: {e}")

def reconhecer_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguarde um momento... Estou ouvindo.")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        comando = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {comando}")
        return comando.lower()
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
    except sr.RequestError as e:
        print(f"Erro ao se conectar ao serviço de reconhecimento de voz: {e}")

def main():
    while True:
        comando = reconhecer_voz()
        if comando:
            if "steam" in comando:
                abrir_steam()
            elif "firefox" in comando:
                abrir_firefox()
            elif "abrir link" in comando:
                url = "https://www.youtube.com/"  # Substitua pelo link desejado
                abrir_link(url)
            elif "sair" in comando:
                print("Saindo...")
                sys.exit()
            else:
                print("Comando não reconhecido. Tente novamente.")

if __name__ == "__main__":
    main()

