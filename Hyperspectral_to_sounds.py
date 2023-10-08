#%%
#Inmersed in the sounds of Space
#Team Vacuum
import numpy as np
import astropy.io.fits as ft
import matplotlib.pyplot as plt
import winsound
import time

plt.style.use("bmh")
import sounddevice as sd

from math import exp, log

ff=ft.open('0098p408_ac51-w1-int-3_ra10.68479292_dec41.269065_asec600.000.fits')
ff2=ft.open('0098p408_ac51-w2-int-3_ra10.68479292_dec41.269065_asec600.000.fits')
ff3=ft.open('0098p408_ac51-w3-int-3_ra10.68479292_dec41.269065_asec600.000.fits')
ff4=ft.open('0098p408_ac51-w4-int-3_ra10.68479292_dec41.269065_asec600.000.fits')
img1=ff[0]
img2=ff2[0]
img3=ff3[0]
img4=ff4[0]
img=img1.data
img_2=img2.data
img_3=img3.data
img_4=img4.data
hdr=ff[0].header
hdr2=ff2[0].header
hdr3=ff3[0].header
hdr4=ff4[0].header
def frec(nota: int, octava: int) -> int:
    expo = octava * 12 + (nota - 56)
    return int(440 * ((2 * (1 / 12)) * expo))

def beep(nota: int, octava: int, duracion: int) -> None:
    framerate = 60100
    t = np.linspace(0, duracion / 1000, int(framerate * duracion / 500))
    frequency = frec(nota, octava)
    data = np.sin(2 * np.pi * frequency * t)
    sd.play(data,framerate)
    sd.wait()

for i in range(0,400,50):
    for j in range(0,400,50):
        beep(img[i][j],4,100)
        beep(img_2[i][j],4,100)
        beep(img_3[i][j],4,100)
        beep(img_4[i][j],4,100)

plt.figure(figsize=(5,5))
plt.imshow(img, vmin=np.min(img), vmax=np.mean(img)*1.5, origin='lower')
plt.xlabel('píxeles')
plt.ylabel('píxeles')
plt.show()


