from tkinter import *
from tkinter import messagebox
from random import *
from PIL import Image
import pygame
import threading

def finitochoix() :
    global fenchoix,musicplayed
    fenchoix.destroy()
    if musicplayed == True :
        play_music()
    return None

def finitojeu() :
    global fenjeu
    fenjeu.destroy()
    fenzero()
    return None


    

def propjeu() :
    global tablon,motprop,mot,nblettre,essai
    global UU,UD,UT,UQ,UC,USi,USe,UH,UN
    global DU,DD,DT,DQ,DC,DSi,DSe,DH,DN
    global TU,TD,TT,TQ,TC,TSi,TSe,TH,TN
    global QU,QD,QT,QQ,QC,QSi,QSe,QH,QN
    global CU,CD,CT,CQ,CC,CSi,CSe,CH,CN
    global SU,SD,ST,SQ,SC,SSi,SSe,SH,SN
    
    copnbl = nblettre.copy()
    
    Mt = motprop.get()
    Mt = Mt.lower()
    
    
    LMt1 = [*Mt][0]
    LMt2 = [*Mt][1]
    LMt3 = [*Mt][2]
    LMt4 = [*Mt][3]
    LMt5 = [*Mt][4]
    if tablon > 5 :
        LMt6 = [*Mt][5]
    else :
        LMt6 = None
    if tablon > 6 :
        LMt7 = [*Mt][6]
    else :
        LMt7 = None
    if tablon > 7 :
        LMt8 = [*Mt][7]
    else :
        LMt8 = None
    if tablon > 8 :
        LMt9 = [*Mt][8]
    else :
        LMt9 = None
    
    Lmt = [("deep sky blue",LMt1),("deep sky blue",LMt2),("deep sky blue",LMt3),
           ("deep sky blue",LMt4),("deep sky blue",LMt5),("deep sky blue",LMt6),
           ("deep sky blue",LMt7),("deep sky blue",LMt8),("deep sky blue",LMt9)]
    
    for i in range(1,tablon+1) :
            if Lmt[i-1][1] == [*mot][i-1] :
                Lmt[i-1] = ('red',[Lmt[i-1][1]])
                for h in range(0,len(copnbl)-1) :
                    if [*mot][i-1] == copnbl[h][0] :
                        copnbl[h] = (copnbl[h][0],copnbl[h][1]-1)
                    else : None
            else : None

    for i in range(1,tablon+1) :
        for j in range(1,tablon+1) :
            if Lmt[j-1][1] == [*mot][i-1] :
                for h in range(0,len(copnbl)-1) :
                    if [*mot][i-1] == copnbl[h][0] :
                        if copnbl[h][1] != 0 :
                            copnbl[h] = (copnbl[h][0],copnbl[h][1]-1)
                            Lmt[j-1] = ('yellow',[Lmt[j-1][1]])
                            print(i,j,Lmt[j-1])
                        else : None
                    else : None
            else : None
    if essai == 1 :
        UU.config(background=Lmt[0][0],text=Lmt[0][1])
        UD.config(background=Lmt[1][0],text=Lmt[1][1])
        UT.config(background=Lmt[2][0],text=Lmt[2][1])
        UQ.config(background=Lmt[3][0],text=Lmt[3][1])
        UC.config(background=Lmt[4][0],text=Lmt[4][1])
        if tablon > 5 :
            USi.config(background=Lmt[5][0],text=Lmt[5][1])
        if tablon > 6 :
            USe.config(background=Lmt[6][0],text=Lmt[6][1])
        if tablon > 7 :
            UH.config(background=Lmt[7][0],text=Lmt[7][1])
        if tablon > 8 :
            UN.config(background=Lmt[8][0],text=Lmt[8][1])
            
    if essai == 2 :
        DU.config(background=Lmt[0][0],text=Lmt[0][1])
        DD.config(background=Lmt[1][0],text=Lmt[1][1])
        DT.config(background=Lmt[2][0],text=Lmt[2][1])
        DQ.config(background=Lmt[3][0],text=Lmt[3][1])
        DC.config(background=Lmt[4][0],text=Lmt[4][1])
        if tablon > 5 :
            DSi.config(background=Lmt[5][0],text=Lmt[5][1])
        if tablon > 6 :
            DSe.config(background=Lmt[6][0],text=Lmt[6][1])
        if tablon > 7 :
            DH.config(background=Lmt[7][0],text=Lmt[7][1])
        if tablon > 8 :
            DN.config(background=Lmt[8][0],text=Lmt[8][1])

    if essai == 3 :
        TU.config(background=Lmt[0][0],text=Lmt[0][1])
        TD.config(background=Lmt[1][0],text=Lmt[1][1])
        TT.config(background=Lmt[2][0],text=Lmt[2][1])
        TQ.config(background=Lmt[3][0],text=Lmt[3][1])
        TC.config(background=Lmt[4][0],text=Lmt[4][1])
        if tablon > 5 :
            TSi.config(background=Lmt[5][0],text=Lmt[5][1])
        if tablon > 6 :
            TSe.config(background=Lmt[6][0],text=Lmt[6][1])
        if tablon > 7 :
            TH.config(background=Lmt[7][0],text=Lmt[7][1])
        if tablon > 8 :
            TN.config(background=Lmt[8][0],text=Lmt[8][1])


    if essai == 4 :
        QU.config(background=Lmt[0][0],text=Lmt[0][1])
        QD.config(background=Lmt[1][0],text=Lmt[1][1])
        QT.config(background=Lmt[2][0],text=Lmt[2][1])
        QQ.config(background=Lmt[3][0],text=Lmt[3][1])
        QC.config(background=Lmt[4][0],text=Lmt[4][1])
        if tablon > 5 :
            QSi.config(background=Lmt[5][0],text=Lmt[5][1])
        if tablon > 6 :
            QSe.config(background=Lmt[6][0],text=Lmt[6][1])
        if tablon > 7 :
            QH.config(background=Lmt[7][0],text=Lmt[7][1])
        if tablon > 8 :
            QN.config(background=Lmt[8][0],text=Lmt[8][1])

    if essai == 5 :
        CU.config(background=Lmt[0][0],text=Lmt[0][1])
        CD.config(background=Lmt[1][0],text=Lmt[1][1])
        CT.config(background=Lmt[2][0],text=Lmt[2][1])
        CQ.config(background=Lmt[3][0],text=Lmt[3][1])
        CC.config(background=Lmt[4][0],text=Lmt[4][1])
        if tablon > 5 :
            CSi.config(background=Lmt[5][0],text=Lmt[5][1])
        if tablon > 6 :
            CSe.config(background=Lmt[6][0],text=Lmt[6][1])
        if tablon > 7 :
            CH.config(background=Lmt[7][0],text=Lmt[7][1])
        if tablon > 8 :
            CN.config(background=Lmt[8][0],text=Lmt[8][1])

    if essai == 6 :
        SU.config(background=Lmt[0][0],text=Lmt[0][1])
        SD.config(background=Lmt[1][0],text=Lmt[1][1])
        ST.config(background=Lmt[2][0],text=Lmt[2][1])
        SQ.config(background=Lmt[3][0],text=Lmt[3][1])
        SC.config(background=Lmt[4][0],text=Lmt[4][1])
        if tablon > 5 :
            SSi.config(background=Lmt[5][0],text=Lmt[5][1])
        if tablon > 6 :
            SSe.config(background=Lmt[6][0],text=Lmt[6][1])
        if tablon > 7 :
            SH.config(background=Lmt[7][0],text=Lmt[7][1])
        if tablon > 8 :
            SN.config(background=Lmt[8][0],text=Lmt[8][1])


    essai += 1

    if essai == 7 :
        messagebox.showerror(title="Perdu",message="Perdu, le mot était "+str(mot))
        finitojeu()
    
    if Mt == mot :
        messagebox.showinfo(title="Victoire",message="Gagné, le mot étaitv"+str(mot)+" Vous l'avez trouvé en "+str(essai-1)+" essais !")
        finitojeu()
    return None

def play_music():
    global musicplayed
    if musicplayed == False :
        pygame.mixer.init()
        pygame.mixer.music.load('motus.mp3')
        pygame.mixer.music.play(-1)  # "-1" indique de jouer la musique en boucle
        musicplayed = True
        return None
    if musicplayed == True :
        pygame.mixer.music.stop()
        musicplayed = False
        return None

def suitechoix() :
    global fenchoix
    motaleatoire()
    fenchoix.destroy()
    fendejeu()
    return None

def fctmot() :
    global tablon,mot,motdec,nblettre
    nblettre = []
    lettreuni = set(motdec)
    for lettre in lettreuni:
        count = motdec.count(lettre)
        nblettre.append((lettre, count))
    

def motaleatoire():
    global long,mot,motdec,tablon
    longmot = long.get()
    tablon = 4
    if longmot == 5 :
        mot = liste5[randint(0, len(liste5)-1)]
        tablon = 5
    if longmot == 6 :
        mot = liste6[randint(0, len(liste6)-1)]
        tablon = 6
    if longmot == 7 :
        mot = liste7[randint(0, len(liste7)-1)]
        tablon = 7
    if longmot == 8 :
        mot = liste8[randint(0, len(liste8)-1)]
        tablon = 8
    if longmot == 9 :
        mot = liste9[randint(0, len(liste9)-1)]
        tablon = 9
    motdec = [*mot]
    fctmot()
    print(mot)
    return None

def fenzero() :
    global long,fenchoix
    fenchoix = Tk()
    fenchoix.geometry("445x320+460+224")
    fenchoix.title("MOTUS")
    
    long = IntVar()
    LogoM = PhotoImage(file="motus_logo.png")
    Icon = PhotoImage(file = "logob.png")
    fenchoix.iconphoto(False, Icon)
    icoMusic = PhotoImage(file="audio.png")
    
    Logo = Label(fenchoix,image=LogoM)
    TexteChx = Label(fenchoix,text="Choissisez le Nombre de lettres")
    
    l5 = Radiobutton(fenchoix,text="5 lettres",variable=long,value=5)
    l6 = Radiobutton(fenchoix,text="6 lettres",variable=long,value=6)
    l7 = Radiobutton(fenchoix,text="7 lettres",variable=long,value=7)
    l8 = Radiobutton(fenchoix,text="8 lettres",variable=long,value=8)
    l9 = Radiobutton(fenchoix,text="9 lettres",variable=long,value=9)
    
    Audio = Button(fenchoix,image=icoMusic,command=play_music).place(x=400,y=125)
    commencer = Button(fenchoix,text="Commencer",command=suitechoix)
    Quitter = Button(fenchoix,text="Quitter",command=finitochoix)
    
    Logo.place(x=0,y=0)
    TexteChx.place(x=130,y=125)
    l5.place(x=180,y=150)
    l6.place(x=180,y=175)
    l7.place(x=180,y=200)
    l8.place(x=180,y=225)
    l9.place(x=180,y=250)
    
    commencer.place(x=150,y=285)
    Quitter.place(x=235,y=285)
    fenchoix.mainloop()
    return None


def fendejeu() :
    global LogoM,tablon,fenjeu,motprop,mot,essai
    global UU,UD,UT,UQ,UC,USi,USe,UH,UN
    global DU,DD,DT,DQ,DC,DSi,DSe,DH,DN
    global TU,TD,TT,TQ,TC,TSi,TSe,TH,TN
    global QU,QD,QT,QQ,QC,QSi,QSe,QH,QN
    global CU,CD,CT,CQ,CC,CSi,CSe,CH,CN
    global SU,SD,ST,SQ,SC,SSi,SSe,SH,SN
    
    
    fenjeu = Tk()
    fenjeu.geometry("445x500+460+119")
    
    LogoM = PhotoImage(file="motus_logo.png")
    Icon = PhotoImage(file = "logob.png")
    icoMusic = PhotoImage(file="audio.png")
    fenjeu.title("MOTUS - "+str(tablon)+" lettres")
    
    fenjeu.iconphoto(False, Icon)
    Label(fenjeu,image=LogoM).place(x=0,y=0)
    
    UU = Label(fenjeu,background="deep sky blue",text=str([*mot][0]))
    UU.place(x=180,y=150)
    UD = Label(fenjeu,background="deep sky blue",text=".")
    UD.place(x=210,y=150)
    UT = Label(fenjeu,background="deep sky blue",text=".")
    UT.place(x=20,y=150)
    UQ = Label(fenjeu,background="deep sky blue",text=".")
    UQ.place(x=210,y=150)
    UC = Label(fenjeu,background="deep sky blue",text=".")
    UC.place(x=220,y=150)

    
    DU = Label(fenjeu,background="deep sky blue",text=".")
    DU.place(x=180,y=180)
    DD = Label(fenjeu,background="deep sky blue",text=".")
    DD.place(x=190,y=180)
    DT = Label(fenjeu,background="deep sky blue",text=".")
    DT.place(x=200,y=180)
    DQ = Label(fenjeu,background="deep sky blue",text=".")
    DQ.place(x=210,y=180)
    DC = Label(fenjeu,background="deep sky blue",text=".")
    DC.place(x=220,y=180)

    
    TU = Label(fenjeu,background="deep sky blue",text=".")
    TU.place(x=180,y=210)
    TD = Label(fenjeu,background="deep sky blue",text=".")
    TD.place(x=190,y=210)
    TT = Label(fenjeu,background="deep sky blue",text=".")
    TT.place(x=200,y=210)
    TQ = Label(fenjeu,background="deep sky blue",text=".")
    TQ.place(x=210,y=210)
    TC = Label(fenjeu,background="deep sky blue",text=".")
    TC.place(x=220,y=210)

   
    QU = Label(fenjeu,background="deep sky blue",text=".")
    QU.place(x=180,y=240)
    QD = Label(fenjeu,background="deep sky blue",text=".")
    QD.place(x=190,y=240)
    QT = Label(fenjeu,background="deep sky blue",text=".")
    QT.place(x=200,y=240)
    QQ = Label(fenjeu,background="deep sky blue",text=".")
    QQ.place(x=210,y=240)
    QC = Label(fenjeu,background="deep sky blue",text=".")
    QC.place(x=220,y=240)    
                    
    CU = Label(fenjeu,background="deep sky blue",text=".")
    CU.place(x=180,y=270)
    CD = Label(fenjeu,background="deep sky blue",text=".")
    CD.place(x=190,y=270)
    CT = Label(fenjeu,background="deep sky blue",text=".")
    CT.place(x=200,y=270)
    CQ = Label(fenjeu,background="deep sky blue",text=".")
    CQ.place(x=210,y=270)
    CC = Label(fenjeu,background="deep sky blue",text=".")
    CC.place(x=220,y=270)

    SU = Label(fenjeu,background="deep sky blue",text=".")
    SU.place(x=180,y=300)
    SD = Label(fenjeu,background="deep sky blue",text=".")
    SD.place(x=190,y=300)
    ST = Label(fenjeu,background="deep sky blue",text=".")
    ST.place(x=200,y=300)
    SQ = Label(fenjeu,background="deep sky blue",text=".")
    SQ.place(x=210,y=300)
    SC = Label(fenjeu,background="deep sky blue",text=".")
    SC.place(x=220,y=300)
    
    
    if tablon > 5 :
        USi = Label(fenjeu,background="deep sky blue",text=".")
        USi.place(x=230,y=150)
        DSi = Label(fenjeu,background="deep sky blue",text=".")
        DSi.place(x=230,y=180)
        TSi = Label(fenjeu,background="deep sky blue",text=".")
        TSi.place(x=230,y=210)
        QSi = Label(fenjeu,background="deep sky blue",text=".")
        QSi.place(x=230,y=240)
        CSi = Label(fenjeu,background="deep sky blue",text=".")
        CSi.place(x=230,y=270)
        SSi = Label(fenjeu,background="deep sky blue",text=".")
        SSi.place(x=230,y=300)
    if tablon > 6 :
        USe = Label(fenjeu,background="deep sky blue",text=".")
        USe.place(x=240,y=150)
        DSe = Label(fenjeu,background="deep sky blue",text=".")
        DSe.place(x=240,y=180)
        TSe = Label(fenjeu,background="deep sky blue",text=".")
        TSe.place(x=240,y=210)
        QSe = Label(fenjeu,background="deep sky blue",text=".")
        QSe.place(x=240,y=240)
        CSe = Label(fenjeu,background="deep sky blue",text=".")
        CSe.place(x=240,y=270)
        SSe = Label(fenjeu,background="deep sky blue",text=".")
        SSe.place(x=240,y=300)
    if tablon > 7 :
        UH = Label(fenjeu,background="deep sky blue",text=".")
        UH.place(x=250,y=150)
        DH = Label(fenjeu,background="deep sky blue",text=".")
        DH.place(x=250,y=180)
        TH = Label(fenjeu,background="deep sky blue",text=".")
        TH.place(x=250,y=210)
        QH = Label(fenjeu,background="deep sky blue",text=".")
        QH.place(x=250,y=240)
        CH = Label(fenjeu,background="deep sky blue",text=".")
        CH.place(x=250,y=270)
        SH = Label(fenjeu,background="deep sky blue",text=".")
        SH.place(x=250,y=300)
    if tablon > 8 :
        UN = Label(fenjeu,background="deep sky blue",text=".")
        UN.place(x=260,y=150)
        DN = Label(fenjeu,background="deep sky blue",text=".")
        DN.place(x=260,y=180)
        TN = Label(fenjeu,background="deep sky blue",text=".")
        TN.place(x=260,y=210)
        QN = Label(fenjeu,background="deep sky blue",text=".")
        QN.place(x=260,y=240)
        CN = Label(fenjeu,background="deep sky blue",text=".")
        CN.place(x=260,y=270)
        SN = Label(fenjeu,background="deep sky blue",text=".")
        SN.place(x=260,y=300)
    
    essai = 1
    motprop = Entry()
    motprop.place(x=165,y=360)
    Prop = Button(fenjeu,text="Proposer",command=propjeu).place(x=195,y=385)
    Audio = Button(fenjeu,image=icoMusic,command=play_music).place(x=400,y=125)
    Button(fenjeu,text="Quitter",command=finitojeu).place(x=195,y=430)
    fenjeu.mainloop()
    return None

fichier = open("as_dict5letters.txt","r",encoding="utf-8")
contenu = fichier.read()
fichier.close()
liste5 = contenu.split("\n")

fichier = open("as_dict5letters.txt","r",encoding="utf-8")
contenu = fichier.read()
fichier.close()
liste6 = contenu.split("\n")

fichier = open("as_dict7letters.txt","r",encoding="utf-8")
contenu = fichier.read()
fichier.close()
liste7 = contenu.split("\n")

fichier = open("as_dict8letters.txt","r",encoding="utf-8")
contenu = fichier.read()
fichier.close()
liste8 = contenu.split("\n")

fichier = open("as_dict9letters.txt","r",encoding="utf-8")
contenu = fichier.read()
fichier.close()
liste9 = contenu.split("\n")

musicplayed = False
essai = 1

play_music()

fenzero()
