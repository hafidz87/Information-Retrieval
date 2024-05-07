# -*- coding: utf-8 -*-
"""Scraper_Gplay_Ok.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/145jHOd1Lr7EKAWu1SwS0nEtJY1nYLPWt
"""

!pip install google-play-scraper #membuat koneksi dengan google play

!pip install pymongo #membuat koneksi dengan database MongoDB

import pandas as pd #untuk manipulasi dan analisis data

from google_play_scraper import app, Sort, reviews #mengambil informasi
from pprint import pprint #mencetak objek Python agar mudah dibaca

import pymongo #database MongoDB
from pymongo import MongoClient #membuat koneksi dengan server MongoDB

import datetime
from tzlocal import get_localzone

import random # operasi terkait dengan angka acak
import time

client = MongoClient(host='localhost', port=27017) #koneksi dengan server

test_project_db = client['test_project_db'] #mengakses database

info_collection = test_project_db['info_collection'] #menyimpan dokumen-dokumen

reviews_collection= test_project_db['info_collection']  #menyimpan ulasan-ulasan terkait

rvws, token = reviews(
    'com.gojek.gopay', #id apps iD
    lang='id', #bahasa ulasan
    country='id', #negara asal ulasan
    sort=Sort.NEWEST, #urutan terbaru
    count=20, #maksimal ulasan yang akan diambil
    filter_score_with=5 #mengambil ulasan dengan skor 5 (nilai maksimal)
)

print(rvws)

# Commented out IPython magic to ensure Python compatibility.
from ast import increment_lineno #untuk analisis sintaksis
import json  #untuk mengolah data dalam format JSON
import pandas as pd
from tqdm import tqdm #untuk menampilkan progress bar saat proses iterasi

import seaborn as sns #untuk membuat visualisasi data
import matplotlib.pyplot as plt #jenis grafik dan plot

from pygments import highlight  #library yang digunakan untuk melakukan penyorotan
from pygments.lexers import JsonLexer #data dalam format JSON
from pygments.formatters import TerminalFormatter #Mengimpor kelas untuk mengatur format output

from google_play_scraper import Sort, reviews, app

# %matplotlib inline #menampilkan plot Matplotlib secara inline

# %config InlineBackend.figure_format='retina' #Mengatur format gambar plot Matplotlib agar lebih tajam pada layar retina

sns.set(style='whitegrid', palette='muted', font_scale=1.2) # Mengatur gaya visualisasi default Seaborn

#lebih dari 1 app
app_packages = [
    'ovo.id',
    'net.sprintasia.ewallet',
    'id.dana',
    'com.telkom.mwallet',
    'com.shopeepay.id',
    'com.dokuwallet.android',
    'com.bca',
    'com.isaku.app',
    'com.paypal.android.p2pmobile'
]

len(app_packages)

#app reviews
app_reviews = []

for ap in tqdm(app_packages):
  for score in list(range(1, 6)):
    for sort_order in [Sort.MOST_RELEVANT, Sort.NEWEST]:
      rvs, __ = reviews(
          ap,
          lang='id',
          country='id',
          sort=sort_order,
          count=20 if score == 3 else 100,
          filter_score_with=score
      )
      for r in rvs:
        r['sortOrder'] = 'most_relevan' if sort_order == Sort.MOST_RELEVANT else 'newest'
        r['appId'] = ap
        app_reviews.extend(rvs)

print(app_reviews[0])

len(app_reviews)

app_reviews_df = pd.DataFrame(app_reviews)
app_reviews_df.to_csv('ReviewWalletId.csv', index=None, header=True)

app_reviews_df.sample(20)