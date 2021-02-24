from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
import vlc
from . models import *


mArr = []
def StartPage(request):
    radioStream = RadioStream.objects.all()
    playPos = 0
    pausePos = 0

    if request.GET.get('play') != None:
        playPos = int(request.GET.get('play'))
    elif request.GET.get('pause') != None:
        pausePos = int(request.GET.get('pause'))

    print(f'playPos = {playPos} \npausePos = {pausePos}')


    try :
        link = RadioStream.objects.get(id = playPos)
        p = vlc.MediaPlayer(link.StreamUrl)
        if len(mArr) ==  0:
            mArr.append(p)
            mArr[0].play()
        else :
            print(f'играет {mArr} {len(mArr)}')
            mArr[0].stop()

            mArr.remove(mArr[0])


    except ObjectDoesNotExist as e:
        print("kekyou")








    return render(request,"Radio/index.html",{'radios':radioStream})
