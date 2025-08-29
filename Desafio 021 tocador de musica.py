#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import paygame
paygame.init()
paygame.mixer.music.load('ex021.mp3')
paygame.mixer.music.play()
paygame.event.wait()

