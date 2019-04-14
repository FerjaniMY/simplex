import numpy as np
n=2
m=3

M=[[ 0. ,  2. ,  3. ,  1. ,  0. ,  0. ,  6. ,  2. ],
       [ 0. ,  0. ,  1. ,  0. ,  1. ,  0. ,  1.5,  1.5],
       [ 0. ,  1. , -1. ,  0. ,  0. ,  1. ,  2. , -2. ],
       [ 0. ,  1. ,  2. ,  0. ,  0. ,  0. ,  0. ,  0. ]]
M2=np.zeros_like(M)
 
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
            m_ratio=M[i,n+m+2]
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
def calcul_elements(M):#a'=a-b*c/pivot
    for i in range(1,n+m+1):
        for j in range(m+1):
            M2[i,j]=M[i,j]- (M[indice_sortante(M),j]*M[i,indice_entrante(M)])/pivot(M)

            return M2
def nv_coeff(M):
    
      M[indice_sortante(M),0]= M[m+1,indice_entrante(M)]
      
def optimize(M):
    
     
     for x in M[m][1:n+m+1] :
       condition=x<0
     while condition is True:
         M=calcul_elements(M)  
         M[m+1,n+m+3]=calcul_Z(M)
         M[indice_sortante(M),0]= M[m+1,indice_entrante(M)] #remplace nv_coeff
         for i in range(1,m+1):
             M[i-1][n+m+3]=colonne_ratio(M)
     print(M)
     return M
