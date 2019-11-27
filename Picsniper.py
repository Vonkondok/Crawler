# 20191109 26-08-11 [9356]
# My first pachong
import os
import re
import urllib.request
import requests

# Variables
modelname = '22162'
foldername = '31558'
capacity = 104

def seqfile(seq):
    if seq in range(10):
        filename = r'D:\Desktop\{}\00{}.jpg'.format(foldername,seq)
    elif seq in range(10,100):
        filename = r'D:\Desktop\{}\0{}.jpg'.format(foldername,seq)
    else:
        filename = r'D:\Desktop\{}\{}.jpg'.format(foldername,seq)
    return filename

def sequrl(seq):
    if seq in range(10):
        urlname = "https://img.xsnvshen.com/album/{}/{}/00{}.jpg".format(modelname,foldername,seq)
    elif seq in range(10,100):
        urlname = "https://img.xsnvshen.com/album/{}/{}/0{}.jpg".format(modelname,foldername,seq)
    else:
        urlname = "https://img.xsnvshen.com/album/{}/{}/{}.jpg".format(modelname,foldername,seq)
    return urlname

def downpic(picurl,picpath):
    headers = {'User-Agent':'Mozilla/5.0 3578.98 Safari/537.36'}
    imgurl = urllib.request.Request(picurl,headers=headers)
    data = urllib.request.urlopen(imgurl).read()

    with open(picpath, 'wb') as f:
        f.write(data)
        f.close()

for ml in range(capacity):
    downpic(sequrl(ml),seqfile(ml))
