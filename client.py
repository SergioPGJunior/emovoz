import requests

URL = "http://127.0.0.1:5000/prediction"
TEST_AUDIO_FILE_PATH = "audios/felicidade.wav"

if __name__ == "__main__":

    audio_file = open(TEST_AUDIO_FILE_PATH, "rb")
    values = {"file": (TEST_AUDIO_FILE_PATH, audio_file, "audio/wav")}
    response = requests.post(URL, files=values)
    data = response.json()

    print(f"Predicted emotion is: {data}")