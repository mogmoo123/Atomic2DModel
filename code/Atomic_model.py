import cv2
import pandas as pd
import numpy as np
from math import sin,cos,pi,radians
from tkinter import *
from PIL import Image,ImageTk

data = pd.read_csv('../files/PubChemElements_all.csv') #배포용
data = data.fillna(value='')


def hex2BGR(hex : str=None):
    return [int(hex[2:4],16),int(hex[4:6],16),int(hex[0:2],16)]

atimg = None
model = None
N = 0
def Atomic(
        number = 1,
        rate = 10,
        download : bool = False,
        
):
    global atimg, model
    number -= 1
    R = data['AtomicRadius'][number]
    hexcolor = data['CPKHexColor'][number]
    remains = number+1
    junjas = [2,8,8,18,18,32,32]

    if R != '' and hexcolor != '':
        r = R/rate
        #원자핵
        model = np.full((400,400,3),(224,224,224))
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
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
        #보여주기
    elif R == '' and hexcolor != '':
        #원자핵
        r = 245/rate
        model = np.full((400,400,3),(224,224,224))
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
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
    elif hexcolor == '' and R != '':
        r = R/rate
        model = np.full((400,400,3),(224,224,224))
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
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            i+=1 
    else:
        r = 245/rate
        model = np.full((400,400,3),(224,224,224))
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
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
                    cv2.circle(model,radius=3,center=pos,color=(175,0,0),thickness=-1)
            else:
                for j in range(junjas[i]+remains):
                    theta = radians(360/junjas[i]*j)
                    pos = (int(200-R_*cos(theta)),int(R_*sin(theta)+200))
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
    
    #tkinter 표시
    img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(model,cv2.COLOR_BGR2RGB)))
    
    if atimg is None:
        atimg = Label(atomimg,image=img)
        #아이네 Ine
        atimg.img = img
        atimg.pack()
    else:
        atimg.configure(image=img)
        atimg.img = img
    
    name_L.configure(text=f"Name: {data['Name'][number]}")
    obital_L.configure(text=f"| Electron configuration |\n {data['ElectronConfiguration'][number]}")
    mass_L.configure(text=f"| Atomic mass | \n {data['AtomicMass'][number]}")
    Elecna_L.configure(text=f"| Electro negativity | \n {data['Electronegativity'][number]}")
    #원자 성질

def download(model,number :int):
    cv2.imwrite(f'../img/{number+1}_{data["Name"][number]}.png',model) #배포용

def buttoncommand():
    global N
    for i in range(0,118,1):
        if(symbol_E.get() == data['Symbol'][i]):
            N=i+1
            break
    Atomic(number=N,rate=10)

def download_():
    download(model=model,number=N-1)

if __name__ == '__main__':
    win = Tk()
    win.title('Atomics')
    win.geometry("700x500")

    atomimg = Frame(win,width=400,height=400)
    atomimg.pack(side='left')
    Text = Label(atomimg,text="Bohr Atomic Model",font=("나눔고딕",30))
    Text.pack(side='top')
    main = Frame(win,width=300,height=500)
    main.pack(side='left')
    

    #원소 기호 입력
    symbol = Frame(main,width=300,height=20)
    symbol_L = Label(symbol,text='Symbol',font=20)
    symbol_E = Entry(symbol,background="#BABABA")
    symbol.pack(side='top')
    symbol_L.pack(side='left')
    symbol_E.pack(side='left')
    
    
    #이름
    name = Frame(main,width=300,height=20)
    name.pack(side='top')
    name_L = Label(name,text=f"Name: ",font=("나눔고딕",20,"bold"),justify='center')
    name_L.pack(side='left')

    #오비탈
    obital = Frame(main,width=300,height=20)
    obital.pack(side='top')
    obital_L=Label(obital,text=f"| Electron configuration |\n",font=("나눔고딕",13),justify='center')
    obital_L.pack(side='left')

    #원자량
    mass = Frame(main,width=300,height=20)
    mass.pack(side='top')
    mass_L=Label(mass,text="| Atomic Mass |",font=("나눔고딕",13),justify='center')
    mass_L.pack(side='left')

    #전기음성도
    Elecna = Frame(main,width=300,height=20)
    Elecna.pack(side='top')
    Elecna_L = Label(Elecna,text='| Electro negativity |',font=("나눔고딕",13),justify='center')
    Elecna_L.pack(side='left')
    Atomic(number=1,rate=10)
    #버튼
    symbol_B = Button(symbol,text="Input",background="#C9C9C9",command=buttoncommand)
    symbol_B.pack(side='left')
    
    down_F = Frame(main,width=300,height=20)
    down_B = Button(down_F,text="Download Image",font=("나눔고딕",13),command=download_,background="#c9c9c9")
    down_F.pack(side='top')
    down_B.pack(side='top')
    
    win.mainloop()
