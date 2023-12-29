# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1otFgLh2Kvc_4q0zSCCDZeSHQ6LPSa1_-
"""

# Pandas ve Numpy kütüphanelerini ekle
import pandas as pd
import numpy as np

# Veri setini oku
df = pd.read_csv("teleCust1000t.csv")

# İlk 10 kaydı göster (head() fonksiyonu varsayılan olarak 5 kaydı gösterir, değer verirsek verilen değer kadar gösterir)
df.head(10)

# Sütun isimlerini yazdırın
print(df.columns)

# Her sınıftan kaç tane örnek var yazdırın
print(df["custcat"].value_counts())

# Girdileri numpy array olarak x değişkeninde sakla
# Numpy olarak getirmek için sonuna .values ekledik
X = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed',
       'employ', 'retire', 'gender', 'reside']].values

# İlk 5 girdiyi ekrana yazdır
print(X[:5]) # 0'dan başla 5'e kadar git ve 5 dahil değil

# Çıktıları numpy array olarak y değişkeninde sakla
y = df['custcat'].values

# İlk 5 çıktıyı yazdır
print(y[:5])

# Veriyi eğitim ve test veriseti olarak böl
from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=60) # %20'si Test için %80'de eğitim için kullanılacak
                                                                                      # random_state ile belli bir değer verirsek rastgele bölmeyecektir
# Eğitim ve test setlerindeki verilerin şeklini yazdır
print("Eğitim Seti", Xtrain.shape, ytrain.shape)
print("Test Seti", Xtest.shape, ytest.shape)

# Verilerin, ortalamaları 0 varyansları 1 olacak şekilde ölçeklendir
# Sadece X'leri kullanacağız
from sklearn.preprocessing import StandardScaler

olceklendir = StandardScaler()
Xtrain = olceklendir.fit_transform(Xtrain) # Xtrain'e öğretip bu ölçeklendirmeyi uygulama işlemini yapıyoruz
Xtest = olceklendir.transform(Xtest) # Öğrenmeyi train'de yapacağı için test'de fit yazmadık

# Ölçeklendirilmiş verinin ilk 5 satırını göster
print(Xtrain[:5])

# Sınıflandırma kütüphanesini dahil et
# 5 Adet komşuluğua bakan sınıflandırma nesnesi yarat
from sklearn.neighbors import KNeighborsClassifier
k = 5
model = KNeighborsClassifier(n_neighbors=k) # Kullanacağımız komşu sayısını argüman olarak sınıfa belirtiyoruz

# Modeli eğit
model.fit(Xtrain, ytrain) # Girdi ve Çıktıları belirttik ve öğrettik
                          # Sadece train kısmını yazmalıyız

# Modelin çıktılarını göster
model_ciktilari = model.predict(Xtest) # Xtrain yazarsak öğrenme kısmındaki doğruluğa bakar, xtest yazarsak testteki doğruluk oranını verir

# Modelin performansını yazdırın
from sklearn.metrics import accuracy_score # Modelin doğruluğunu gösterecek olan kütüphane
print(accuracy_score(ytest, model_ciktilari)) # Olması gereken çıktılar ile modelin çıktılarını karşılaştırıyoruz

                                          # Yukarda Xtrain yazarsak ytest yerine de Xtrain yazmalıyız

# # Bilinmeyen bir veri gösterelim
# bilinmeyen = np.array([[5.1, 3.5, 1.4, 0.2]])
# bilinmeyen = olceklendir.transform(bilinmeyen)
# print(model.predict(bilinmeyen)) # Iris-virginica çıktısı gelecektir.
#                                  # Verilen değerler bu sınıfa en yakın değerler olduğundan bu sekil bir çıktı alırız.