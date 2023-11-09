# -*- coding: utf-8 -*-

from datetime import datetime


import base64
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import xlrd

import math
import random

import numpy as np
import matplotlib.pyplot as plt

a = str(datetime.today())


nommm = "distri a"

# ouverture feuille du fichier excel
classeur = xlrd.open_workbook('E:\\zapmaths2\\tab qcm '+nommm[0:len(nommm)-2]+'.xlsx') 
feuille = classeur.sheet_by_name('txt '+nommm)



  




#supprime le suffixe ".0" que XLRD ajoute dans la chaine renvoyée en cas de lecture d'un nombre  entier dans une cellule
def suppressionFormeDdecimaleCasEntierLu(chaine):
    if (chaine[len(chaine)-2:len(chaine)] == '.0'):
        chaine = chaine[0:len(chaine)-2]
    return chaine



################################## TXT IMG ##############################################
# récupération et redimensionnement image
def cheminImageModifiee(chemin_fichier_image):
    img = Image.open(chemin_fichier_image)
    ratio_largeur = 480 / img.size[0]
    ratio_hauteur = 360 / img.size[1]
    ratio = min(ratio_hauteur, ratio_largeur)
    nouvelle_largeur = int( ratio * img.size[0])
    nouvelle_hauteur = int( ratio * img.size[1])
    img = img.resize((nouvelle_largeur, nouvelle_hauteur), Image.ANTIALIAS)
    img.save('temp_image.png')
    return 'temp_image.png'

#texte sur image redimensionnée
def texteSurImage(chemin_image,texte,posX,posY,txtSize,txtColor):
    im = Image.open(chemin_image)
    draw = ImageDraw.Draw(im)
    draw.text((posX, posY), texte,txtColor,ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtSize))
    im.save('temp_image.png')
    return('temp_image.png')
    
    
# encodage image en base64 depuis le chemin --- REDIMENSIONNEMENT A FAIRE !! ----
def imageBase64(chaine_chemin_image):
    with open(chaine_chemin_image, "rb") as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = str(base64_encoded_data)
    return base64_message



#################################### fin TXT IMG #######################################
    
#################################### IMG PCTG ########################################
def img_proportion(p,txt_max):
    pctg = str(p*100)[0:2]
    p=p/100
    xp = 260*p + 30
    txtsize = 15
    
    im = Image.new('RGB', (320, 100), (255,255,255))
    draw = ImageDraw.Draw(im, 'RGBA')
    draw.rectangle((30, 30, xp, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
    draw.rectangle((xp, 30, 290, 50), fill=(255, 255, 255,255), outline=(0, 0, 0,255))
    
    draw.text((10,13),"0 %",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((280,13),"100 %",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((10,55),str("0 "+ txt_max[len(txt_max)-1:len(txt_max)]),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((280,55),txt_max,(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((xp-10,13), str(pctg+" %"),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((xp-10,55), "?" ,(255,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", 40))
    
    im.save('temp_img_pctg.png')
    return('temp_img_pctg.png')


def img_reduction_fleches(p,txt_max):
    p = (100-p)/100
    pctg = str(p*100)[0:2]
    xp = 260*p + 30
    txtsize = 15
    
    im = Image.new('RGB', (320, 150), (255,255,255))
    draw = ImageDraw.Draw(im, 'RGBA')
    draw.rectangle((30, 30, xp, 50), fill=(0, 255, 0,100), outline=(0, 0, 0,255))
    draw.rectangle((xp, 30, 290, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
    
    arrowedLine(im, (xp/2,55), (xp/2,100), width=5, color=(0,180,0))
    arrowedLine(im, (xp + (290-xp)/2,55), (xp + (290-xp)/2,80), width=5, color=(180,0,0))
    
   #draw.text((10,13),"0 %",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
   #draw.text((280,13),"100 %",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((10,13),str("0 "+ txt_max[len(txt_max)-1:len(txt_max)]),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((285,13),txt_max,(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
   #draw.text((xp-10,13), str(pctg+" %"),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
   #draw.text((xp-10,55), "?" ,(0,0,255,100),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", 40))
    draw.text((xp+(290-xp)/2-30,90), "réduction\n",(180,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((xp/2-45,110), "nouveau prix",(0,150,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf",txtsize))
    
    im.save('temp_img_pctg.png')
    return('temp_img_pctg.png')



def img_augmentation_fleches(p,txt_max):
    pctg = str(p*100)[0:2]
    xp = 30 + 260*(100/(p+100))
    txtsize = 15
    
    im = Image.new('RGB', (320, 150), (255,255,255))
    draw = ImageDraw.Draw(im, 'RGBA')
    draw.rectangle((30, 30, xp, 50), fill=(0, 0, 255,100), outline=(0, 0, 0,255))
    draw.rectangle((xp, 30, 290, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
    
    arrowedLine(im, (xp/2,55), (xp/2,100), width=5, color=(0,0,180))
    arrowedLine(im, (xp + (290-xp)/2,55), (xp + (290-xp)/2,80), width=5, color=(180,0,0))
    
   #draw.text((10,13),"0 %",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
   #draw.text((280,13),"100 %",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((10,13),str("0 "+ txt_max[len(txt_max)-1:len(txt_max)]),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
   #draw.text((285,13),str(int(100)+pctg)),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((xp-15,13), txt_max,(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
   #draw.text((xp-10,55), "?" ,(0,0,255,100),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", 40))
    draw.text((xp + (290-xp)/2-40,90), "augmentation",(180,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
    draw.text((xp/2-30,110), "ancien prix",(0,0,150),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf",txtsize))    
    
    im.save('temp_img_pctg.png')
    return('temp_img_pctg.png')

def arrowedLine(im, ptA, ptB, width=1, color=(0,255,0)):
    """Draw line from ptA to ptB with arrowhead at ptB"""
    # Get drawing context
    draw = ImageDraw.Draw(im)
    # Draw the line without arrows
    draw.line((ptA,ptB), width=width, fill=color)

    # Now work out the arrowhead
    # = it will be a triangle with one vertex at ptB
    # - it will start at 95% of the length of the line
    # - it will extend 8 pixels either side of the line
    x0, y0 = ptA
    x1, y1 = ptB
    # Now we can work out the x,y coordinates of the bottom of the arrowhead triangle
    xb = 0.80*(x1-x0)+x0
    yb = 0.80*(y1-y0)+y0

    # Work out the other two vertices of the triangle
    # Check if line is vertical
    if x0==x1:
       vtx0 = (xb-5, yb)
       vtx1 = (xb+5, yb)
    # Check if line is horizontal
    elif y0==y1:
       vtx0 = (xb, yb+5)
       vtx1 = (xb, yb-5)
    else:
       alpha = math.atan2(y1-y0,x1-x0)-90*math.pi/180
       a = 8*math.cos(alpha)
       b = 8*math.sin(alpha)
       vtx0 = (xb+a, yb+b)
       vtx1 = (xb-a, yb-b)

    #draw.point((xb,yb), fill=(255,0,0))    # DEBUG: draw point of base in red - comment out draw.polygon() below if using this line
    #im.save('DEBUG-base.png')              # DEBUG: save

    # Now draw the arrowhead triangle
    y = list(ptB)
    y[1]= y[1]+7
    ptB=tuple(y)
    draw.polygon([vtx0, vtx1, ptB], fill=color)
    return im
###################################   FIN IMG PCTG   ##################################################
    

#########################   figalea     ##################################
    
def reperage_points(xmin, xmax, ymin, ymax, x, y, lettres):
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    

    

    #plt.plot(x,y,'ro')    
    
    for i in range(0,len(lettres)):    
        plt.text(float(x[i])+.2,float(y[i])+.2,lettres[i],fontsize=16, color='red')
        plt.plot(float(x[i]),float(y[i]),'ro') 
    
        # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(np.arange(float(xmin),float(xmax)+1,1))
    ax.set_yticks(np.arange(float(ymin),float(ymax)+1,1))
    
    plt.grid()
    

    plt.savefig('temp_plt_img.png')
    return 'temp_plt_img.png'



def reperage_points_2rect(xmin, xmax, ymin, ymax, x, y, lettres):
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    #plt.plot(x,y,'ro')    
    
    for i in range(0,len(lettres)):    
        plt.text(float(x[i])+.2,float(y[i])+.2,lettres[i],fontsize=16, color='red')
        plt.plot(float(x[i]),float(y[i]),'ro') 
        plt.plot([float(x[i]),float(x[(i+1)%6])],[float(y[i]),float(y[(i+1)%6])], color='blue')
    
    plt.plot([float(x[0]),float(x[1])],[float(y[0]),float(y[0])], color='green', linestyle='dashed')
    plt.plot([float(x[1]),float(x[1])],[float(y[1]),float(y[0])], color='green', linestyle='dashed')
    plt.plot([float(x[1]),float(x[2])],[float(y[0]),float(y[0])], color='green', linestyle='dashed')
    plt.plot([float(x[4]),float(x[4])],[float(y[4]),float(y[3])], color='green', linestyle='dashed')
    plt.plot([float(x[0]),float(x[3])],[float(y[3]),float(y[3])], color='green', linestyle='dashed')
        # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(np.arange(float(xmin),float(xmax)+1,1))
    ax.set_yticks(np.arange(float(ymin),float(ymax)+1,1))
    
    plt.grid()
    
    plt.savefig('temp_plt_img.png')
    return 'temp_plt_img.png'

#############     fin figalea      ###################################
    


############ fonctions  #################################
    
def fct(xmin, xmax, ymin, ymax, f):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    
    
    x = np.linspace(xmin,xmax,100)
    y = eval(f)
    
    plt.plot(x,y,'r')
    
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(np.arange(float(xmin),float(xmax)+1,1))
    ax.set_yticks(np.arange(float(ymin),float(ymax)+1,1))
    
    plt.ylim(top=ymax+0.1)
    plt.ylim(bottom=ymin-0.1)
    plt.xlim(left=xmin-0.1)
    plt.xlim(right=xmax+0.1)
    #grille
    plt.grid()
    
    plt.savefig('temp_plt_img.png')
    return 'temp_plt_img.png'
    plt.close()
    
def fct_img(xmin, xmax, ymin, ymax, f, ximg, yimg):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    
    
    x = np.linspace(xmin,xmax,100)
    y = eval(f)
    
    plt.plot(x,y,'r')
    plt.plot([float(ximg),float(ximg)],[float(0),float(yimg)], color='green', linestyle='dashed')
    plt.plot([float(0),float(ximg)],[float(yimg),float(yimg)], color='green', linestyle='dashed')
    
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(np.arange(float(xmin),float(xmax)+1,1))
    ax.set_yticks(np.arange(float(ymin),float(ymax)+1,1))
    
    plt.ylim(top=ymax+0.1)
    plt.ylim(bottom=ymin-0.1)
    plt.xlim(left=xmin-0.1)
    plt.xlim(right=xmax+0.1)
    #grille
    plt.grid()
    
    plt.savefig('temp_plt_img.png')
    plt.close()
    return 'temp_plt_img.png'
    
    

def fct4(xmin, xmax, ymin, ymax, f1, f2, f3, f4):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    
    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    
    
    x = np.linspace(xmin,xmax,100)
    y1 = eval(f1)
    y2 = eval(f2)
    y3 = eval(f3)
    y4 = eval(f4)
    
    plt.plot(x,y1,'r')
    plt.plot(x,y2,'b')
    plt.plot(x,y3,'g')
    plt.plot(x,y4,'y')
    
    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_xticks(np.arange(float(xmin),float(xmax)+1,1))
    ax.set_yticks(np.arange(float(ymin),float(ymax)+1,1))
    
    plt.ylim(top=ymax+0.1)
    plt.ylim(bottom=ymin-0.1)
    plt.xlim(left=xmin-0.1)
    plt.xlim(right=xmax+0.1)
    #grille
    plt.grid()
    
    plt.savefig('temp_plt_img.png')
    return 'temp_plt_img.png'
    plt.close()

#############################      fin fonctions        ##############################
    
    
    
#############################      FRACTIONS        ##############################
    
    
def fraction_pie(numerateur, denominateur, couleur_num, couleur_den, angle):
    sizes = []
    mycolors = []
    
    for i in range(denominateur):
        sizes.append(1/(denominateur))
        if (i<numerateur):
            mycolors.append(str(couleur_num))
        else:
            mycolors.append(str(couleur_den))
    
    
    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes,
            wedgeprops = {'linewidth': 2, 'edgecolor' : 'black'},
            colors = mycolors,
            shadow=False, 
            startangle=angle
            
            )
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.savefig('temp_plt_img.png')
    return 'temp_plt_img.png'
    plt.close()



def fraction_pie_double(numerateur1, denominateur1, numerateur2, denominateur2, couleur_num, couleur_den, angle):
    
    sizes1 = []
    sizes2 = []
    mycolors1 = []
    mycolors2 = []
    
    for i in range(denominateur1):
        sizes1.append(1/(denominateur1))
        if (i<numerateur1):
            mycolors1.append(couleur_num)
        else:
            mycolors1.append(couleur_den)
            
    for i in range(denominateur2):
        sizes2.append(1/(denominateur2))
        if (i<numerateur2):
            mycolors2.append(couleur_num)
        else:
            mycolors2.append(couleur_den)
    
    
    fig1, (ax1, ax2) = plt.subplots(1,2)
    
    ax1.pie(sizes1,
            wedgeprops = {'linewidth': 2, 'edgecolor' : 'black'},
            colors = mycolors1,
            shadow=False, 
            startangle=angle
            
            )
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    
    ax2.pie(sizes2,
            wedgeprops = {'linewidth': 2, 'edgecolor' : 'black'},
            colors = mycolors2,
            shadow=False, 
            startangle=angle
            
            )
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    plt.savefig('temp_plt_img.png')
    return 'temp_plt_img.png'
    plt.close()
    
    
    

#############################      fin fractions        ##############################

with open("E:\\zapmaths2\\" + 'qcm '+nommm+' pour BDD ' + a[2:13] + 'h' + a[14:16] + '.csv', 'w', encoding='utf-8') as fichier:

    # récupération 1er en-tête
    entete = []
    i = 0
    
    
    while ( str(feuille.cell(i,0).value) != 'ENONCE'):
        i = i + 1
    ligne_entete = i
    for colonne in range(0,feuille.ncols):
        if str(feuille.cell(ligne_entete,colonne).value) != '':
            entete.append(str(feuille.cell(ligne_entete,colonne).value))
            
    
    
    
    # récupération données numériques et génération chaine question
    for ligne in range(ligne_entete+1,feuille.nrows):
        
        # cas nouvel en-tête : on forme le nouvel en têtee et on passe à la ligne suivante
        if str(feuille.cell(ligne,0).value) == 'ENONCE':
            entete = []
            ligne_entete = ligne
            for colonne in range(0,feuille.ncols):
                if str(feuille.cell(ligne_entete,colonne).value) != '':
                    entete.append(str(feuille.cell(ligne_entete,colonne).value))
        
        else: #on s'occupe de former la question
            
            enonce = ''
            liste_reponses  = []
            chaine_imageb64_question = ''
            feedback = ''
            prop_choix = []
            rep_choix = ''
            rep_txt = ''
            
            figalea_x = []
            figalea_y = []
            figalea_l = []

            
            for colonne in range(0, len(entete)):  
                
                #lecture cellule et suppression du suffixe ".0" dans le cas d'un entier
                chaine = suppressionFormeDdecimaleCasEntierLu(str(feuille.cell(ligne,colonne).value))
                
                # cas énoncé
                if (entete[colonne] == 'ENONCE' and chaine != ''):
                    enonce = enonce + chaine
                    chaine_propositions_variable = '' # spécifité de traitement pour textes à trous avec listes variables
                
                # cas feedback
                if (entete[colonne] == 'feedback' and chaine != ''):
                    feedback = feedback + chaine
                
                    
                #cas TXTIMG
                if (entete[colonne] == "TXTIMG_chemin" and chaine != ''):
                    TXTIMG_chemin = chaine
                if (entete[colonne] == "TXTIMG_texte" and chaine != ''):
                    TXTIMG_texte = chaine
                if (entete[colonne] == "TXTIMG_posX" and chaine != ''):
                    TXTIMG_posX = int(chaine)
                if (entete[colonne] == "TXTIMG_posY" and chaine != ''):
                    TXTIMG_posY = int(chaine)
                if (entete[colonne] == "TXTIMG_txtSize" and chaine != ''):
                    TXTIMG_txtSize = int(chaine)
                if (entete[colonne] == "TXTIMG_txtColor" and chaine != ''):
                    TXTIMG_txtColor = chaine
                    
                #traitement texte par texte : on ajoute le texte avec ses paramètres sur l'image pour la sauvegarder temp_image.png
                if (entete[colonne] == "TXTIMG_go"): # j'ai viré la ocndition chaine!=''
                    if chaine == 'go': #là on ajoute le texte sur temp_image.png
                        texteSurImage(cheminImageModifiee(TXTIMG_chemin),TXTIMG_texte,TXTIMG_posX,TXTIMG_posY,TXTIMG_txtSize,TXTIMG_txtColor)
                    if chaine == 'fin': #on convertit temp_image.png en message base64
                        chaine_imageb64_question = imageBase64('temp_image.png')
                        chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]

                        
                #cas img_pctg
                if (entete[colonne] == "img_pctg_p" and chaine != ''):
                    impg_pctg_p = chaine
                if (entete[colonne] == "img_pctg_txt_max" and chaine != ''):
                    impg_pctg_txt_max = chaine
                if (entete[colonne] == "img_pctg_cas" and chaine != ''):
                    if (chaine=="proportion"):
                        aaa = int(impg_pctg_p)
                        img_proportion(aaa,impg_pctg_txt_max)
                        chaine_imageb64_question = imageBase64('temp_img_pctg.png')
                        chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                    
                    if (chaine=="reduction"):
                        aaa = int(impg_pctg_p)
                        img_reduction_fleches(aaa,impg_pctg_txt_max)
                        chaine_imageb64_question = imageBase64('temp_img_pctg.png')
                        chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                    
                    if (chaine=="augmentation"):
                        aaa = int(impg_pctg_p)
                        img_augmentation_fleches(aaa,impg_pctg_txt_max)
                        chaine_imageb64_question = imageBase64('temp_img_pctg.png')
                        chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                        
                 #cas img_fps
                if (entete[colonne] == "img_fps_paht" and chaine != ''):
                    img_fps_paht = chaine
                if (entete[colonne] == "img_fps_marge" and chaine != ''):
                    img_fps_marge = chaine
                if (entete[colonne] == "img_fps_taux" and chaine != ''):
                    img_fps_taux = chaine
                    #img_fps(img_fps_paht,img_fps_marge,img_fps_tva)
                    
                    
                    
                    paht=int(img_fps_paht)
                    marge=int(img_fps_marge)
                    taux=float(img_fps_taux)
                    
                    pvht = paht + marge
                    tva = pvht*taux/100
                    pvttc = pvht + tva
                    
                    x1 = 30 + 260*paht/pvttc
                    x2 = 30 + 260*pvht/pvttc
                    
                    txtsize = 15
                    
                    im = Image.new('RGB', (320, 150), (255,255,255))
                    draw = ImageDraw.Draw(im, 'RGBA')
                    draw.rectangle((30, 30, x1, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
                    draw.rectangle((x1, 30, x2, 50), fill=(0, 255, 0,100), outline=(0, 0, 0,255))
                    draw.rectangle((x2, 30, 290, 50), fill=(0, 0, 255,100), outline=(0, 0, 0,255))
                    
                    arrowedLine(im, (30+(x1-30)/2,55), (30+(x1-30)/2,75), width=5, color=(180,70,70))
                    arrowedLine(im, (x1+(x2-x1)/2,55), (x1+(x2-x1)/2,95), width=5, color=(70,180,70))
                    arrowedLine(im, (x2+(290-x2)/2,55), (x2+(290-x2)/2,105), width=5, color=(70,70,180))
                    
                    draw.text((10,13),"0 €",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1-10,13),str(str(paht) + ' €'),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1-10,2),'PAHT',(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x2-15,2),"PVHT",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((280,13),"PVTTC",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    
                    draw.text((30+(x1-30)/2-15,85),str("PAHT\n"+str(paht)+" €"),(220,70,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1+(x2-x1)/2-15,105),str("Marge\n"+str(marge)+" €"),(70,180,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x2+(290-x2)/2-15,115),"TVA",(70,70,220),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    
                    im.save('temp_img_fps.png')
                
                    chaine_imageb64_question = imageBase64('temp_img_fps.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                    
                      
                 #cas img_fps_pvht
                if (entete[colonne] == "img_fps_pvht_paht" and chaine != ''):
                    img_fps_pvht_paht = chaine
                if (entete[colonne] == "img_fps_pvht_marge" and chaine != ''):
                    img_fps_pvht_marge = chaine                  
                    
                    
                    paht=int(img_fps_pvht_paht)
                    marge=int(img_fps_pvht_marge)
                    
                    pvht = paht + marge
                    
                    x1 = 30 + 260*paht/pvht
                    x2 = 290
                    txtsize = 15
                    
                    im = Image.new('RGB', (320, 150), (255,255,255))
                    draw = ImageDraw.Draw(im, 'RGBA')
                    draw.rectangle((30, 30, x1, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
                    draw.rectangle((x1, 30, x2, 50), fill=(0, 255, 0,100), outline=(0, 0, 0,255))
                    
                    arrowedLine(im, (30+(x1-30)/2,55), (30+(x1-30)/2,75), width=5, color=(180,70,70))
                    arrowedLine(im, (x1+(x2-x1)/2,55), (x1+(x2-x1)/2,95), width=5, color=(70,180,70))
                    
                    draw.text((10,13),"0 €",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1-10,13),str(str(paht) + ' €'),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1-10,2),'PAHT',(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x2-15,2),"PVHT",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                   
                    draw.text((30+(x1-30)/2-15,85),str("PAHT\n"+str(paht)+" €"),(220,70,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1+(x2-x1)/2-15,105),str("Marge\n"+str(marge)+" €"),(70,180,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    
                    im.save('temp_img_fps.png')
                
                    chaine_imageb64_question = imageBase64('temp_img_fps.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                
                
                #cas img_fps_tva

                if (entete[colonne] == "img_fps_2_pvht" and chaine != ''):
                    img_fps_2_pvht = chaine
                if (entete[colonne] == "img_fps_2_taux" and chaine != ''):
                    img_fps_2_taux = chaine
                    #img_fps(img_fps_paht,img_fps_marge,img_fps_tva)
                    
                    
                    
                    pvht=int(img_fps_2_pvht)
                    taux=float(img_fps_2_taux)
                    

                    tva = pvht*taux/100
                    pvttc = pvht + tva
                    
                    x1 = 30 + 260*pvht/pvttc
                    x2 = 290
                    
                    txtsize = 15
                    
                    im = Image.new('RGB', (320, 150), (255,255,255))
                    draw = ImageDraw.Draw(im, 'RGBA')
                    draw.rectangle((30, 30, x1, 50), fill=(255, 255, 0,100), outline=(0, 0, 0,255))
                    draw.rectangle((x1, 30, x2, 50), fill=(0, 0, 255,100), outline=(0, 0, 0,255))

                    
                    arrowedLine(im, (30+(x1-30)/2,55), (30+(x1-30)/2,75), width=5, color=(180,70,70))
                    arrowedLine(im, (x1+(290-x1)/2,55), (x1+(290-x1)/2,105), width=5, color=(70,70,180))
                    
                    draw.text((10,13),"0 €",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1-10,13),str(str(pvht) + ' €'),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((x1-15,2),"PVHT",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    draw.text((295,21),"PVTTC",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize-5))
                    
                    draw.text((30+(x1-30)/2-15,85),str("PVHT\n"+str(pvht)+" €"),(150,150,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                
                    draw.text((x1+(290-x1)/2-15,115),"TVA",(70,70,220),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
                    
                    im.save('temp_img_fps.png')
                
                    chaine_imageb64_question = imageBase64('temp_img_fps.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                
                
                                                        
                #cas reponse numérique
                if (entete[colonne] == 'répNUM' and chaine != '' and len(liste_reponses) == 0):
                    temp_col = colonne
                    temp_chaine = chaine
                    while temp_col < len(entete) and entete[temp_col] == 'répNUM' and temp_chaine != '':
                        temp_chaine = suppressionFormeDdecimaleCasEntierLu(str(feuille.cell(ligne,temp_col).value))
                        
                        
                        # remplacement virgule par point
                        temp_list = list(temp_chaine)
                        for i in range(0,len(temp_chaine)):
                            if temp_list[i] == ',':
                                temp_list[i] = '.'
                        temp_chaine = ''.join(temp_list)
                        liste_reponses.append(temp_chaine)
                        temp_col += 1
        
                
                # cas figalea
                if (entete[colonne] == "figalea_x" and chaine != ''):
                    figalea_x.append(chaine)
                if (entete[colonne] == "figalea_y" and chaine != ''):
                    figalea_y.append(chaine)
                if (entete[colonne] == "figalea_l" and chaine != ''):
                    figalea_l.append(chaine)
                if (entete[colonne] == "figalea_xmin" and chaine != ''):
                    figalea_xmin = chaine
                if (entete[colonne] == "figalea_xmax" and chaine != ''):
                    figalea_xmax = chaine
                if (entete[colonne] == "figalea_ymin" and chaine != ''):
                    figalea_ymin = chaine
                if (entete[colonne] == "figalea_ymax" and chaine != ''):
                    figalea_ymax = chaine
                    #on produit l'image après ymax
                    
                    reperage_points_2rect(figalea_xmin,figalea_xmax,figalea_ymin,figalea_ymax,figalea_x,figalea_y,figalea_l)
                    chaine_imageb64_question = imageBase64('temp_plt_img.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                    
                
                # cas fonction fct
                if (entete[colonne] == "fct_xmin" and chaine != ''):
                    fct_xmin = int(chaine)
                if (entete[colonne] == "fct_xmax" and chaine != ''):
                    fct_xmax = int(chaine)
                if (entete[colonne] == "fct_ymin" and chaine != ''):
                    fct_ymin = int(chaine)
                if (entete[colonne] == "fct_ymax" and chaine != ''):
                    fct_ymax = int(chaine)
                if (entete[colonne] == "fct_f" and chaine != ''):
                    fct_f = chaine
                #on produit l'image après f
                    fct(fct_xmin,fct_xmax,fct_ymin,fct_ymax,fct_f)
                    chaine_imageb64_question = imageBase64('temp_plt_img.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]

                
                # cas fonction fct_img
                if (entete[colonne] == "fct_img_xmin" and chaine != ''):
                    fct_img_xmin = int(chaine)
                if (entete[colonne] == "fct_img_xmax" and chaine != ''):
                    fct_img_xmax = int(chaine)
                if (entete[colonne] == "fct_img_ymin" and chaine != ''):
                    fct_img_ymin = int(chaine)
                if (entete[colonne] == "fct_img_ymax" and chaine != ''):
                    fct_img_ymax = int(chaine)
                if (entete[colonne] == "fct_img_ximg" and chaine != ''):
                    fct_img_ximg = float(chaine)
                if (entete[colonne] == "fct_img_yimg" and chaine != ''):
                    fct_img_yimg = int(chaine)
                if (entete[colonne] == "fct_img_f" and chaine != ''):
                    fct_img_f = chaine
                #on produit l'image après f
                    fct_img(fct_img_xmin,fct_img_xmax,fct_img_ymin,fct_img_ymax,fct_img_f,fct_img_ximg,fct_img_yimg)
                    chaine_imageb64_question = imageBase64('temp_plt_img.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                    
                    

                # cas fonction fct4
                if (entete[colonne] == "fct4_xmin" and chaine != ''):
                    fct4_xmin = int(chaine)
                if (entete[colonne] == "fct4_xmax" and chaine != ''):
                    fct4_xmax = int(chaine)
                if (entete[colonne] == "fct4_ymin" and chaine != ''):
                    fct4_ymin = int(chaine)
                if (entete[colonne] == "fct4_ymax" and chaine != ''):
                    fct4_ymax = int(chaine)
                if (entete[colonne] == "fct4_f1" and chaine != ''):
                    fct4_f1 = chaine
                if (entete[colonne] == "fct4_f2" and chaine != ''):
                    fct4_f2 = chaine
                if (entete[colonne] == "fct4_f3" and chaine != ''):
                    fct4_f3 = chaine
                if (entete[colonne] == "fct4_f4" and chaine != ''):
                    fct4_f4 = chaine
                #on produit l'image après f4
                    fct4(fct4_xmin,fct4_xmax,fct4_ymin,fct4_ymax,fct4_f1,fct4_f2,fct4_f3,fct4_f4)
                    chaine_imageb64_question = imageBase64('temp_plt_img.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]

                
                # cas fraction_pie
                if (entete[colonne] == "fraction_pie_numerateur" and chaine != ''):
                    fraction_pie_numerateur = int(chaine)
                if (entete[colonne] == "fraction_pie_denominateur" and chaine != ''):
                    fraction_pie_denominateur = int(chaine)
                if (entete[colonne] == "fraction_pie_couleur_numerateur" and chaine != ''):
                    fraction_pie_couleur_numerateur = str(chaine)
                if (entete[colonne] == "fraction_pie_couleur_denominateur" and chaine != ''):
                    fraction_pie_couleur_denominateur = str(chaine) 
                if (entete[colonne] == "fraction_pie_angle" and chaine != ''):
                    fraction_pie_angle = int(chaine) 
                        
                    # on produit l'image après "fraction_pie_couleur_angle"
                    fraction_pie(fraction_pie_numerateur, 
                                 fraction_pie_denominateur, 
                                 fraction_pie_couleur_numerateur, 
                                 fraction_pie_couleur_denominateur,
                                 fraction_pie_angle)
                    chaine_imageb64_question = imageBase64('temp_plt_img.png')
                    chaine_imageb64_question = chaine_imageb64_question[2:len(chaine_imageb64_question)-1]
                
                
                
                # cas fraction_pie_double (append sur feedback)
                if (entete[colonne] == "fraction_pie_double_numerateur1" and chaine != ''):
                    fraction_pie_numerateur1 = int(chaine)
                if (entete[colonne] == "fraction_pie_double_denominateur1" and chaine != ''):
                    fraction_pie_denominateur1 = int(chaine)
                if (entete[colonne] == "fraction_pie_double_numerateur2" and chaine != ''):
                    fraction_pie_numerateur2 = int(chaine)
                if (entete[colonne] == "fraction_pie_double_denominateur2" and chaine != ''):
                    fraction_pie_denominateur2 = int(chaine)
                if (entete[colonne] == "fraction_pie_double_couleur_numerateur" and chaine != ''):
                    fraction_pie_couleur_numerateur = str(chaine)
                if (entete[colonne] == "fraction_pie_double_couleur_denominateur" and chaine != ''):
                    fraction_pie_couleur_denominateur = str(chaine) 
                if (entete[colonne] == "fraction_pie_double_angle" and chaine != ''):
                    fraction_pie_double_angle = int(chaine) 
                    
                    # on produit l'image après "fraction_pie_double_angle"
                    fraction_pie_double(fraction_pie_numerateur1, 
                                        fraction_pie_denominateur1,
                                        fraction_pie_numerateur2, 
                                        fraction_pie_denominateur2, 
                                        fraction_pie_couleur_numerateur, 
                                        fraction_pie_couleur_denominateur,
                                        fraction_pie_double_angle)
                    chaine_imageb64_feedback = imageBase64('temp_plt_img.png')
                    chaine_imageb64_feedback = chaine_imageb64_feedback[2:len(chaine_imageb64_feedback)-1]
                    feedback = "<div align='center'><img src='data:image/png;base64, " + chaine_imageb64_feedback + "'" + " alt='imgb64' style=""max-width:100%"" /></div>" + feedback
                
                
                # cas prop_choix
                if (entete[colonne] == "prop_choix" and chaine != ''):
                    prop_choix.append(chaine)
                
                # cas rep_choix
                if (entete[colonne] == "rep_choix" and chaine != ''):
                    rep_choix = chaine
                    
                # cas rep_txt
                if (entete[colonne] == "rep_txt" and chaine != ''):
                    rep_txt = chaine
            
            
            
#            ################# on forme le tableau CSV à importer dans SQL   ##################
            if ((len(liste_reponses) != 0) & (len(rep_choix) == 0) & (len(rep_txt) == 0)):
                fichier.write(str(ligne))
                fichier.write(u"@")
                fichier.write(enonce)
                fichier.write(u"@")
                fichier.write(liste_reponses[0])
                fichier.write(u"@")
                fichier.write(chaine_imageb64_question)
                fichier.write(u"@")
                fichier.write(u"<div align='left'>")
                fichier.write(feedback)
                fichier.write(u"</div>")
                fichier.write(u"\n")
                print(ligne)
            
            
            ############### pour choix ------------- ###############"
            if (len(rep_choix) != 0):
                fichier.write(str(ligne))
                fichier.write(u"@")
                fichier.write(enonce)
                fichier.write(u"@")
                fichier.write(rep_choix)
                fichier.write(u"@")
                fichier.write(chaine_imageb64_question)
                fichier.write(u"@")
                fichier.write(u"<div align='left'>")
                fichier.write(feedback)
                fichier.write(u"</div>")
                for i in range(0,len(prop_choix)):
                    fichier.write(u"@")
                    fichier.write(prop_choix[i])
                fichier.write(u"\n")
                print(ligne)
#            
            
            ################ pour txt ------------- ###############"
            if (len(rep_txt) != 0):
                fichier.write(str(ligne))
                fichier.write(u"@")
                fichier.write(enonce)
                fichier.write(u"@")
                fichier.write(rep_txt)
                fichier.write(u"@")
                fichier.write(chaine_imageb64_question)
                fichier.write(u"@")
                fichier.write(u"<div align='left'>")
                fichier.write(feedback)
                fichier.write(u"</div>")
                fichier.write(u"\n")
                print(ligne)
            
            
            
            # pour figalea ou img dans feedback général
#            if (len(liste_reponses) != 0):
#                fichier.write(str(ligne))
#                fichier.write(u"@")
#                fichier.write(enonce)
#                fichier.write(u"@")
#                fichier.write(liste_reponses[0])
#                fichier.write(u"@")
#                #b64 vide
#                fichier.write(u"")
#                fichier.write(u"@")
#                #image pour démarrer le feedback
#                fichier.write(u"<div align='center'><img src='data:image/png;base64, ")
#                fichier.write(chaine_imageb64_question)
#                fichier.write(u"'")
#                fichier.write(u" alt='imgb64' width='100%' /></div>")
#                fichier.write(u"<div align='left'>")
#                fichier.write(feedback)
#                fichier.write(u"</div>")
#                fichier.write(u"\n")
#                print(ligne)
            





#def img_fps(paht,marge,taux):
#    paht=int(paht)
#    marge=int(marge)
#    taux=int(taux)
#    
#    pvht = paht + marge
#    tva = pvht*taux/100
#    pvttc = pvht + tva
#    
#    x1 = 30 + 260*paht/pvttc
#    x2 = 30 + 260*pvht/pvttc
#    
#    print(x1)
#    print(x2)
#    txtsize = 15
#    
#    im = Image.new('RGB', (320, 150), (255,255,255))
#    draw = ImageDraw.Draw(im, 'RGBA')
#    draw.rectangle((30, 30, x1, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
#    draw.rectangle((x1, 30, x2, 50), fill=(0, 255, 0,100), outline=(0, 0, 0,255))
#    draw.rectangle((x2, 30, 290, 50), fill=(0, 0, 255,100), outline=(0, 0, 0,255))
#    
#    arrowedLine(im, (30+(x1-30)/2,55), (30+(x1-30)/2,75), width=5, color=(180,70,70))
#    arrowedLine(im, (x1+(x2-x1)/2,55), (x1+(x2-x1)/2,95), width=5, color=(70,180,70))
#    arrowedLine(im, (x2+(290-x2)/2,55), (x2+(290-x2)/2,105), width=5, color=(70,70,180))
#    
#    draw.text((10,13),"0 €",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x1-10,13),str(str(paht) + ' €'),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x1-10,2),'PAHT',(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x2-15,13),"PVHT",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((280,13),"PVTTC",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    
#    draw.text((30+(x1-30)/2-15,85),str("PAHT\n"+str(paht)+" €"),(220,70,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x1+(x2-x1)/2-15,105),str("Marge\n"+str(marge)+" €"),(70,180,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x2+(290-x2)/2-15,115),"TVA",(70,70,220),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    
#    im.save('temp_img_fps.png')
#    return('temp_img_fps.png')
#    
#    
#def img_fps_PVHT(paht,marge):
#    paht=int(paht)
#    marge=int(marge)
#    
#    pvht = paht + marge
#    
#    x1 = 30 + 260*paht/pvht
#    
#    txtsize = 15
#    
#    im = Image.new('RGB', (320, 150), (255,255,255))
#    draw = ImageDraw.Draw(im, 'RGBA')
#    draw.rectangle((30, 30, x1, 50), fill=(255, 0, 0,100), outline=(0, 0, 0,255))
#    draw.rectangle((x1, 30, x2, 50), fill=(0, 255, 0,100), outline=(0, 0, 0,255))
#    
#    arrowedLine(im, (30+(x1-30)/2,55), (30+(x1-30)/2,75), width=5, color=(180,70,70))
#    arrowedLine(im, (x1+(x2-x1)/2,55), (x1+(x2-x1)/2,95), width=5, color=(70,180,70))
#    
#    draw.text((10,13),"0 €",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x1-10,13),str(str(paht) + ' €'),(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x1-10,2),'PAHT',(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x2-15,13),"PVHT",(0,0,0),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    
#    draw.text((30+(x1-30)/2-15,85),str("PAHT\n"+str(paht)+" €"),(220,70,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    draw.text((x1+(x2-x1)/2-15,105),str("Marge\n"+str(marge)+" €"),(70,180,70),ImageFont.truetype("C:\\Windows\\Fonts\\calibri.ttf", txtsize))
#    
#    im.save('temp_img_fps.png')
#    return('temp_img_fps.png')