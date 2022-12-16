import speech_recognition

class SpeechRecognitionModule:
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()

    def listen(self):
        with speech_recognition.Microphone() as source:
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_sphinx(audio)
        except speech_recognition.UnknownValueError:
            print("[clearsight_3.vocaloid] Sphinx could not understand audio.")
            return "..."
        except speech_recognition.RequestError as e:
            print("[clearsight_3.vocaloid] Sphinx error; " + str(e))