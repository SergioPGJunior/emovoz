from flask import Flask, request, jsonify
import pickle
import librosa
import utils
import random
import os
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def verifica_api():
    return "Reconhecimento de emoções na voz", 200


@app.route("/prediction", methods=['POST'])
def infer_audio():
    try:
        # carrega e salva o arquivo de audio
        audio_file = request.files["file"]
        
        file_name = str(random.randint(0, 100000))
        audio_file.save(file_name)
        
        # leitura do arquivo de audio
        y, fs = librosa.load(file_name)
        
        #remove o arquivo
        os.remove(file_name)
        
        #extrai os parâmetros
        mfcc = utils.matriz_mfcc(y, fs, 20, delta=False, delta2=False)
        parametros = np.array(utils.parametros_globais(mfcc))
        
        #Predicao
        predicted = model.predict([parametros])
        resultado = predicted[0]
        resposta = {'EMOCAO': int(resultado)}
        return jsonify(resposta)

    except Exception as e:

        return {'code':500, 'data':'{}'.format(e)}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')