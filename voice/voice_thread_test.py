from playsound import playsound as play
import _thread
while(1):
    a=input()
    if a=='1':
    	_thread.start_new_thread(play,('straight.mp3',))
    if a=='2':
    	_thread.start_new_thread(play,('turnleft.mp3',))
    if a=='3':
    	_thread.start_new_thread(play,('turnright.mp3',))
    if a=='4':
    	play('hardleft.mp3')
    if a=='5':
    	play('hardright.mp3')
    if a=='0':
    	os.system('play STOP.mp3')
