import sys
import os
import time
from playsound import playsound as play
import threading
import _thread

class VoiceInterface(object):

  def __init__(self, straight_file = 'straight.wav',
                     turnleft_file = 'turnleft.wav',
                     turnright_file = 'turnright.wav',
                     hardleft_file = 'hardleft.mp3',
                     hardright_file = 'hardright.mp3',
                     STOP_file = 'STOP.mp3',
                     noway_file = 'noway.mp3'):
    self.straight_file= straight_file
    self.turnleft_file= turnleft_file
    self.turnright_file=turnright_file
    self.hardleft_file=hardleft_file
    self.hardright_file=hardright_file
    self.STOP_file=STOP_file
    self.noway_file=noway_file

    self.prev_path = None
    self.count=0

  def play(self, pat, width):
    b=10
    center=width/2-0.5
    if len(pat)==0:
        play(self.noway_file)
        return
    path=[]
    path.append(pat[0]-center)
    for i in range (1,len(pat)):
        path.append(pat[i]-pat[i-1])
    print(path)
    for step in path:
        if step == 1 and step!=b:
            play(self.turnleft_file)
        if step == 2 and step!=b:
            play(self.hardleft_file)
        if step == -1 and step!=b:
            play(self.turnright_file)
        if step == -2 and step!=b:
            play(self.hardright_file)
        if step == 0 and step!=b:
            play(self.straight_file)
        b=step
    play(self.STOP_file)
  def play1(self, pat, width):
    center=width/2-0.5
    if len(pat)==0:
        play(self.noway_file)
        return
    path=[]
    path.append(pat[0]-center)
    for i in range (1,len(pat)):
        path.append(pat[i]-pat[i-1])
    print(path)
    for step in path:
        if step == 1:
            _thread.start_new_thread(play,(self.turnleft_file,))
            time.sleep(1)
            print(x)
        if step == 2:
            _thread.start_new_thread(play,(self.hardleft_file,))
            time.sleep(1)
            print("2")
        if step == -1:
            _thread.start_new_thread(play,(self.turnright_file,))
            time.sleep(1)
            print("-1")
        if step == -2:
            play(self.hardright_file)
        if step == 0:
            _thread.start_new_thread(play,(self.straight_file,))
            time.sleep(1)
    play(self.STOP_file)

## interface working with pointcloud
  def play2(self, pat):
    if len(pat)==0:
        play(self.noway_file)
        self.prev_path=10
        return
    step=pat[0]

    if step == -1 and (step!=self.prev_path or self.count>=5):
        play(self.turnleft_file)
        self.count=0
    if step == 1 and (step!=self.prev_path or self.count>=5):
        play(self.turnright_file)
        self.count=0
    if step == 0 and (step!=self.prev_path or self.count>=5):
        play(self.straight_file)
        self.count=0
    if step == self.prev_path:
        self.count+=1
    self.prev_path = step


  def play4(self, pat, width):
    center=width/2-0.5
    if len(pat)==0:
        play(self.noway_file)
        self.prev_path=10
        return
    path=[]
    path.append(pat[0]-center)
    for i in range (1,len(pat)):
        path.append(pat[i]-pat[i-1])
    print(path)
    if len(path)==0:
        play(self.noway_file)
        self.prev_path=10
        return
    step=path[0]
    if step == -1 and (step!=self.prev_path or self.count>=5):
        play(self.turnleft_file)
        self.count=0
    if step == -2 and (step!=self.prev_path or self.count>=5):
        play(self.hardleft_file)
        self.count=0
    if step == 1 and (step!=self.prev_path or self.count>=5):
        play(self.turnright_file)
        self.count=0
    if step == 2 and (step!=self.prev_path or self.count>=5):
        play(self.hardright_file)
        self.count=0
    if step == 0 and (step!=self.prev_path or self.count>=5):
        play(self.straight_file)
        self.count=0
    if step == self.prev_path:
        self.count+=1
    self.prev_path = step

if __name__=="__main__":

    interface = VoiceInterface()
    test=[1,0,0,1,-1,0,1,-1]
    for a in test:
        interface.play2([a])
        time.sleep(1)
