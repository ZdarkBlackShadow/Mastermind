#!/usr/bin/python2.7
# -*- coding: iso-8859-1 -*-

import time
import glob
import os
from os import path, listdir
from time import strftime
from datetime import datetime

mini = 100.0
maxi = 0.0

base_dir = '/sys/bus/w1/devices/'  # Chemin des sondes dallas
device_files = []


def init_temp_probes():
    for s in listdir(base_dir):
        if s.startswith('28'):
            device_files.append(path.join(base_dir, s, 'w1_slave'))

#Fontion récupérant la température


def read_temp_raw(i):
    with open(device_files[i], 'r') as f:
        lines = f.readlines()
    return lines

#Fonction syntaxe temperature


def read_temp(i):
    lines = read_temp_raw(i)
    if lines[0].strip()[-3:] != 'YES':
        raise OSError("La sonde n'est pas prête ")
    temp_string = lines[1].split('=')[1]
    temp_c = float(temp_string)/1000
    return temp_c


def afficheTemp(i):
    temperature = round(read_temp(i), 1)
    return temperature


#Fonction retournant la temperature mini enregistré
def tempMini(temperature):
    global mini
    if mini > temperature:
        mini = temperature

    return mini
#Fonction retournant la temperature maxi enregistré


def tempMaxi(temperature):
    global maxi
    if maxi < temperature:
        maxi = temperature

    return maxi


def afficheHeure():
    heure = strftime("%H:%M:%S", time.localtime())
    return heure
