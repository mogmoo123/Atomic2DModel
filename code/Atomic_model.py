import cv2
import pandas as pd
import numpy as np
from math import sin,cos,pi,radians


data = pd.read_csv('../files/PubChemElements_all.csv')
data = data.fillna(value='')

def hex2BGR(hex : str=None):
    return [int(hex[2:4],16),int(hex[4:6],16),int(hex[0:2],16)]

def Atomic(
        number = 1,
        rate = 10,
        download : bool = False,
        
):
    number -= 1
    R = data['AtomicRadius'][number]
    hexcolor = data['CPKHexColor'][number]
    remains = number+1
    junjas = [2,8,8,18,18,32,32]

    if R != '' and hexcolor != '':
        r = R/rate
        #원자핵
        model = np.full((400,400,3),(255,255,255))
        model = np.array(model, dtype=np.uint8)
        cv2.circle(model,radius=int(r),center=(200,200),color = hex2BGR(hexcolor),thickness=-1)
        cv2.circle(model,radius=int(r),center=(200,200),color = (0,0,0),thickness=1)
        #전자
        #전자 껍질
        i = 0
        R_ = int(r)
        while remains > 0:
            R_ += int(junjas[i]*1.3)
            cv2.circle(model,radius=R_,center=(200,200),color=(0,0,0),thickness=1)
            remains -= junjas[i]
            #전자 생성
            if remains >= 0:
                for j in range(junjas[i]):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
        #보여주기
    elif R == '' and hexcolor != '':
        #원자핵
        r = 245/rate
        model = np.full((400,400,3),(255,255,255))
        model = np.array(model, dtype=np.uint8)
        cv2.circle(model,radius=int(r),center=(200,200),color = hex2BGR(hexcolor),thickness=-1)
        cv2.circle(model,radius=int(r),center=(200,200),color = (0,0,0),thickness=1)
        #전자
        #전자 껍질
        i = 0
        R_ = int(r)
        while remains > 0:
            R_ += int(junjas[i]*1.3)
            cv2.circle(model,radius=R_,center=(200,200),color=(0,0,0),thickness=1)
            remains -= junjas[i]
            #전자 생성
            if remains >= 0:
                for j in range(junjas[i]):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
    elif hexcolor == '' and R != '':
        r = R/rate
        model = np.full((400,400,3),(255,255,255))
        model = np.array(model, dtype=np.uint8)
        cv2.circle(model,radius=int(r),center=(200,200),color = (251,121,255),thickness=-1)
        cv2.circle(model,radius=int(r),center=(200,200),color = (0,0,0),thickness=1)
        #전자
        #전자 껍질
        i = 0
        R_ = int(r)
        while remains > 0:
            R_ += int(junjas[i]*1.3)
            cv2.circle(model,radius=R_,center=(200,200),color=(0,0,0),thickness=1)
            remains -= junjas[i]
            #전자 생성
            if remains >= 0:
                for j in range(junjas[i]):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
    else:
        r = 245/rate
        model = np.full((400,400,3),(255,255,255))
        model = np.array(model, dtype=np.uint8)
        cv2.circle(model,radius=int(r),center=(200,200),color = (251,121,255),thickness=-1)
        cv2.circle(model,radius=int(r),center=(200,200),color = (0,0,0),thickness=1)
        
        #전자
        #전자 껍질
        i = 0
        R_ = int(r)
        while remains > 0:
            R_ += int(junjas[i]*1.3)
            cv2.circle(model,radius=R_,center=(200,200),color=(0,0,0),thickness=1)
            remains -= junjas[i]
            #전자 생성
            if remains >= 0:
                for j in range(junjas[i]):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(R_*sin(theta)+200),int(200-R_*cos(theta)))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
    if len(data['Symbol'][number]) == 1:
        
        if data['Symbol'][number][0] == 'I':
            cv2.putText(model,text=f"{data['Symbol'][number]}",org=(200-3,200+7),color=(0,0,0),thickness=1,fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7)
        else:
            cv2.putText(model,text=f"{data['Symbol'][number]}",org=(200-7,200+7),color=(0,0,0),thickness=1,fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7)
    else:
        if data['Symbol'][number][0] == 'I' or data['Symbol'][number][1] == 'i' or data['Symbol'][number][1] == 'l':
            cv2.putText(model,text=f"{data['Symbol'][number]}",org=(200-7*2+4,200+7),color=(0,0,0),thickness=1,fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7)
        else:
            cv2.putText(model,text=f"{data['Symbol'][number]}",org=(200-7*2,200+7),color=(0,0,0),thickness=1,fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.7)
    cv2.imshow('Atomic',model)
    if download == True:
        cv2.imwrite(f'../img/{number+1}_{data["Name"][number]}.png',model)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    n= 49
    Atomic(number=n,rate=10,download=False)
