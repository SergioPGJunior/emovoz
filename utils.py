import numpy as np
from sklearn.preprocessing import StandardScaler
import librosa

def matriz_mfcc(y, fs, n_mfcc=12, delta=False, delta2=False):
    mfcc = librosa.feature.mfcc(y, fs, n_mfcc=n_mfcc)

    if delta == True & delta2 == True:
        mfcc_delta = librosa.feature.delta(mfcc)
        mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
        parametros = np.concatenate((mfcc, mfcc_delta, mfcc_delta2))

    elif delta == True:
        mfcc_delta = librosa.feature.delta(mfcc)
        parametros = np.concatenate((mfcc, mfcc_delta))

    elif delta2 == True:
        mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
        parametros = np.concatenate((mfcc, mfcc_delta2))

    else:
        parametros = mfcc

    return parametros.tolist()


def parametros_globais(vetor_parametros):
    media = np.mean(vetor_parametros, axis=1).transpose()
    mediana = np.median(vetor_parametros, axis=1).transpose()
    maximo = np.amax(vetor_parametros, axis=1).transpose()
    minimo = np.amin(vetor_parametros, axis=1).transpose()
    std = np.std(vetor_parametros, axis=1).transpose()

    return np.concatenate((media, mediana, maximo, minimo, std)).tolist()

def tratamento_dados(X):
    X = np.array([list(dados.values())])
    # Executa o escalonamento dos dados
    scaler = StandardScaler()
    scaler.fit(X)
    X = scaler.transform(X)

    return X
