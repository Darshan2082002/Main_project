import numpy as np #To deal with array
import pandas as pd # To deal with file 
import matplotlib.pyplot as plt # Plot the graph 
import librosa #for aduio Processing 
import librosa.display
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import os
data_set=(r'D:\Python project\Main_project\archive(2)')
genres=(r'D:\Python project\Main_project\archive (2)\genres').split()
X,y=[],[]
for genere in genres:
    folder=os.path.join(data_set,genere)
    for filename in os.listdir(folder):
        file_path=os.path.join(folder,filename)
        