# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:37:40 2019

@author: hp
"""

import numpy as np
# n,m sont les nbres resp des VHB et VB
 try:
   n=int(input("Donner le nombre de VHB x : \n"))
   assert n>0
except AssertionError:
    print("L'entier saisie est inférieure ou égale à 0.")
  

 try:
   m=int(input("Donner le nombre des VB e :  \n"))
except AssertionError:
    print("L'entier saisie est inférieure ou égale à 0.")

M=np.zeros((m+1,n+m+3))
 #Le tableau initial quand va l'optimiser
def Remplissage_mat(M):
    for i in range (m+1):
        for j in range (n+m+3):
            try:
                M[i,j]=float(input("Donner l'élément M["+str(i)+"]["+str(j)+"] = ")) #Je peut specifier de plus je peut ajouter des  string pour spécifier de plus comme coef,Valeur,..
                print(M)
            except:  
                print("Veuiller saisir un entier")
                M[i,j]=float(input("Donner l'élément M["+str(i)+"]["+str(j)+"] = "))
                print(M)
                return M
def V_entrante(M):
    max_c=0
    #Détermination du cj le plus grand 
    for i in range (1,n+m+1):
        if M[m+1,i]>=max_c : 
            max_c=M[m+1,i]#on vérifie aprés avec le rang en python peut etre M[m,i-1]
    print("max des cj "+str(max_c))
    return max_c #manque du msg La v entrante est : ...
def indice_entrante(M):
    max_c=0
    #Détermination du cj le plus grand 
    for i in range (1,n+m+1):
        if M[m+1,i]>max_c : 
            max_c=M[m+1,i]#on vérifie aprés avec le rang en python peut etre M[m,i-1]
    print("max des cj "+str(max_c))
    return i #manque du msg La v entrante est : ...
def colonne_ratio(M):
    ratio=np.zeros(m)
    for i in range(m):
        M[i,n+m+3]=M[i,n+m+2] / M[i,indice_entrante(M)]
        ratio[i]= M[i,n+m+3]
    return ratio   
def calcul_ratio(M):
    
    for i in range(m):
        M[i,n+m+3]=M[i,n+m+2] / M[i,indice_entrante(M)] 
          
def V_sortante(M):#min ratio
    m_ratio=M[1][m+n+2]
    for i in range (m):
        if M[i,n+m+3]<0:
            continue
        if M[i,n+m+2]<m_ratio :
            m_ratio=M[i-1,n+m+2]
            print("m_ratio="+str(m_ratio))
            return (m_ratio)
def indice_sortante(M):
    m_ratio=M[1][m+n+2]
    for i in range (m):
        if M[i,n+m+3]<0:
            continue
        if M[i,n+m+2]<m_ratio :
            m_ratio=M[i,n+m+2]
            print("indice_ratio="+str(i))
            return i        
def calcul_Z(M):
    s=0
    for i in range(m+1):
        s+=M[i,0]*M[i,m-1]
        M[m+1,n+m+3]==s
        print("Z= "+str(s))
        return s
def pivot(M):
    p=0
    for i in range (m):
        for j in range (1,n+m):
            if(M[m,j]==V_entrante(M) and M[i,n+m]==V_sortante(M)):
                p=M[i,j]
                
                return p
                print("pivot est :"+str(p))   
def calcul_elements(M):#a'=a-b*c/pivot cette fct calcul des les éléments du tab en utilisant la methode du rectangle (voir cours)
    for i in range(1,n+m+1):
        for j in range(m+1):
            M[i,j]=M[i,j]- (M[indice_sortante][j]*M[i][indice_entrante])/pivot(M)

            return M
def nv_coeff(M):
    
      M[indice_sortante(M),0]= M[m+1,indice_entrante(M)]
   # on peut ajouter ici return
def optimize(M):
     Remplissage_mat(M)
     for x in M[m][1:n+m+1] :#parcours du ligne des cj
       condition=x > 0  #la condition d'optimisation
     while condition is True:
         M=calcul_elements(M)  
         M[m+1,n+m+3]=calcul_Z(M)
         M[indice_sortante(M),0]= M[m+1,indice_entrante(M)] #remplace nv_coeff
          for i in range(1,m+1):
             M[i-1][n+m+3]=colonne_ratio(M)
     

      print(M)
      return M


    
        
        
        

