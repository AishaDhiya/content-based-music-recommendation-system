from keras.utils.np_utils import to_categorical
import numpy
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import Session
import os
import librosa
import warnings
from random import shuffle
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json # to load
import numpy

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import time
import numpy as np
from src.dbconnector import *
config = ConfigProto()
config.gpu_options.allow_growth = True
sess = Session(config=config)
warnings.filterwarnings("ignore")
labels = ['blues','classical','country','disco']

def predict(fn):



    model = model_from_json(open("model1.json", "r").read())
    model.load_weights("model1.h5")
    wave, sr = librosa.load(fn, mono=True)
    mfcc = librosa.feature.mfcc(wave, sr)
    p = 0
    if len(mfcc[0]) < 300:
        p = 300 - len(mfcc[0])
    mfcc = np.pad(mfcc, ((0, 0), (0, p)), mode='constant', constant_values=0)

    samples = []
    for i in range(0, 20):
        for j in range(300):
            samples.append(mfcc[i][j])




    samples=np.array(samples)

    y = model.predict(np.array([samples]))
    yy=np.argmax(y[0])
    print(y,yy)
    return yy
# predict(r"D:\MusicPlayer\new\MusicPlayer\src\static\music\20220624031107.wav")
while True:
    qry="select m_id,file from music where m_id not in (select muid from mtype)"
    res=select(qry)
    print(res)
    for i in res:
        try:
            tyid=predict(i[1])
            qry="insert into mtype values(%s,%s)"
            val=(i[0],tyid)
            print(val,"val=============")
            iud(qry,val)
        except Exception as e:
            pass
    time.sleep(10)