from scipy.fft import fft, fftfreq
from scipy.signal import butter, lfilter, freqz, filtfilt, lfilter_zi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


ECG_read =  pd.read_table("./ECG_data.txt")
ECG_np = ECG_read.to_numpy()

Sudavel = pd.DataFrame(ECG_np[:,:150])
Arritmia = pd.DataFrame(ECG_np[:,150:])

plt.plot(Sudavel[0], label='sudavel')
plt.plot(Arritmia[0], label='arritmia')
plt.legend()
plt.show()


def Calcula_Media (Media):
    media = (1/9000)*sum(Media)
    return media


def Calcula_Desviopadrao (Desviopadrao):
    dsviopadrao = np.sqrt((1/9000)*sum(pow(Desviopadrao-Calcula_Media(Desviopadrao),2)))
    return dsviopadrao


def Calcula_Skewness (Skewness):
    skewness = np.sqrt((1/9000)*sum((pow(Skewness-Calcula_Media(Skewness),3))/pow(Calcula_Desviopadrao(Skewness),3)))
    return skewness


def Calcula_Kurtosis (SKurtosis):
    skurtosis = np.sqrt((1/9000)*sum((pow(SKurtosis-Calcula_Media(SKurtosis), 4))/pow(Calcula_Desviopadrao(SKurtosis),4)))
    return skurtosis


def Calcula_Energia (Energia):
    energia = (1/9000)*sum(pow(Energia,2))
    return energia


def correlação (X,Y):

    mediaX = Calcula_Media(X)
    mediaY = Calcula_Media(Y)

    Correlação = (
        sum(
            (X-mediaX)*(Y-mediaX)
        
        )
        /
        (
            pow(
                sum(
                    pow(
                        (X-mediaX)
                    ,2)
                )
            ,-2)
        ) 
        *
        (
            pow(
                sum(
                    pow(
                        (Y-mediaX)
                    ,2)
                )
            ,-2)
        )
    )

    return Correlação


#Saudavel media/desviopadrao/skewness/skurtosis/energia/maximo/minimo

mediaSaudavel = []
desviopadraoSaudavel = []
skewnessSaudavel = []
skurtosisSaudavel = []
energiaSaudavel = []
maximoSaudavel = []
minimoSaudavel = []

for i in range(150):
    mediaSaudavel.append(Calcula_Media(Sudavel[i]))
    desviopadraoSaudavel.append(Calcula_Desviopadrao(Sudavel[i]))
    skewnessSaudavel.append(Calcula_Skewness(Sudavel[i]))
    skurtosisSaudavel.append(Calcula_Kurtosis(Sudavel[i]))
    energiaSaudavel.append(Calcula_Energia(Sudavel[i]))
    maximoSaudavel.append(Sudavel[i].max())
    minimoSaudavel.append(Sudavel[i].min())
    

#Arritmia media/desviopadrao/skewness/skurtosis/energia/maximo/minimo

mediaArritmia = []
desviopadraoArritmia = []
skewnessArritmia = []
skurtosisArritmia = []
energiaArritmia = []
maximoArritmia = []
minimoArritmia = []

for i in range(150):
    mediaArritmia.append(Calcula_Media(Arritmia[i]))
    desviopadraoArritmia.append(Calcula_Desviopadrao(Arritmia[i]))
    skewnessArritmia.append(Calcula_Skewness(Arritmia[i]))
    skurtosisArritmia.append(Calcula_Kurtosis(Arritmia[i]))
    energiaArritmia.append(Calcula_Energia(Arritmia[i]))
    maximoArritmia.append(Arritmia[i].max())
    minimoArritmia.append(Arritmia[i].min())


#eixo X

X = []

for i in range(150):
    X.append(i)


#calculo da FFT
fftSudavel = []
ftArritmia = []

for i in range(150):
    fftSudavel.append(fft(Sudavel[i]))
    ftArritmia.append(fft(Arritmia[i]))

componenteSaudavel = []
componenteArritimia = []
y_componente = []


#calcula o lugar aonde a componente fica no gráfico
componente = math.floor(73*(9000/150))

for i in range(150):
    y_componente.append(i)
    add = fftSudavel[i][componente]
    componenteSaudavel.append(add)

for i in range(150):
    add = ftArritmia[i][componente]
    componenteArritimia.append(add)


#correlação
coeficientePronto = np.corrcoef(Sudavel,Arritmia)

# corela = []

# for i in range(150):
    # corela.append(correlação(Sudavel[i],Arritmia[i]))
# corela

# np.corrcoef(Sudavel,Arritmia)

# corela = []

# corela.append(correlação(Sudavel[1],Arritmia[1]))


#PLOT
plt.plot(X, 2.0/300 * np.abs(fftSudavel[75][0:300//2]), label='FFT sudavel')
plt.plot(X, 2.0/300 * np.abs(ftArritmia[34][0:300//2]), label='FFT aritmia')
plt.grid()
plt.legend()
plt.show()


#componente que tem alguma relação com o problema de saude
plt.scatter(y_componente, componenteSaudavel, label='componente saudavel')
plt.scatter(y_componente, componenteArritimia, label='componente arritimia')
plt.legend()
plt.show()


#correlação com função pronta
plt.matshow(coeficientePronto)
plt.show()


#plot media/desviopadrao/skewness/skurtosis/energia/maximo/minimo
plt.scatter(X, mediaSaudavel, label='Media sudavel')
plt.scatter(X, mediaArritmia, label='Media arritmia')
plt.legend()
plt.show()

plt.scatter(X, desviopadraoSaudavel, label='Desviopadrao sudavel')
plt.scatter(X, desviopadraoArritmia, label='Desviopadrao arritmia')
plt.legend()
plt.show()

plt.scatter(X, skewnessSaudavel, label='Skewness sudavel')
plt.scatter(X, skewnessArritmia, label='Skewness arritmia')
plt.legend()
plt.show()

plt.scatter(X, skurtosisSaudavel, label='SKurtosis sudavel')
plt.scatter(X, skurtosisArritmia, label='SKurtosis arritmia')
plt.legend()
plt.show()

plt.scatter(X, energiaSaudavel, label='Energia sudavel')
plt.scatter(X, energiaArritmia, label='Energia arritmia')
plt.legend()
plt.show()

plt.scatter(X, maximoSaudavel, label='Maximo sudavel')
plt.scatter(X, maximoArritmia, label='Maximo arritmia')
plt.legend()
plt.show()

plt.scatter(X, minimoSaudavel, label='Minimo sudavel')
plt.scatter(X, minimoArritmia, label='Minimo arritmia')
plt.legend()
plt.show()