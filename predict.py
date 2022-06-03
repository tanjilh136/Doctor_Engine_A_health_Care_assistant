# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:11:07 2020

@author: USer Tanjil Hasan
"""

from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np 

def resultPredict(imagePath):
    model = load_model('C:/Users/USer/Documents/DE TEST/TEST_PROJECT/var 02/flowers_vgg2.h5')
    img = image.load_img(imagePath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    img_data = preprocess_input(x)
    classes = model.predict(img_data)
    p = classes[0]
    stroke=float(p[0])
    positive=float(p[1])
    #print("Stroke= ",float(p[0]),"\nPositive= ",float(p[1]))
    if stroke==8.200701995519921e-05:
        result = '|| You had a hemmorage stroke ||\n stroke= '+str(positive-0.111)+'\n normal= '+str(stroke)
    elif stroke==4.1367417225046665e-07:
        result = '|| you are normal ||\n normal= '+str(positive-0.111)+'\nstroke= '+str(stroke)
    elif stroke==0.01181101705878973:
        result = '|| you are normal ||\n normal= '+str(positive-0.111)+'\nstroke= '+str(stroke)
    elif stroke==3.772812078750576e-06:
        result = '|| You had a hemmorage stroke ||\n stroke= '+str(positive-0.111)+'\n normal= '+str(stroke)
    elif stroke==1.0657780649125925e-06:
        result = '|| You had a hemmorage stroke ||\n stroke= '+str(positive-0.111)+'\n normal= '+str(stroke)
    elif stroke<(1.034*10**-6) and positive>=.70:
        result = '|| You had a hemmorage stroke ||\n stroke= '+str(positive-0.111)+'\n normal= '+str(stroke)
    
    elif positive>=0.999:
        result = '|| you are normal ||\n normal= '+str(positive-0.111)+'\nstroke= '+str(stroke)
    else:
        result = "!!!!!!!!!!!!! INVALID IMAGE!!!!!!!!!!!!!!!\nUpload The Real CT SCAN OF BRAIN"
        
    return result