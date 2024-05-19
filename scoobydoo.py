from Board import Field
import numpy as np



def generate_binary(n,k):
    vec = np.zeros(n, dtype = bool)
    for i in range(n):
        vec[i] = bool(k%2)
        k//=2
    return(vec)  





class Algorithm:
    
    def __init__(self, field):
        self.field = field
        
        
    def play_move(self):
        pass
    
    def play_game(self):
        while self.field.win() == False and self.field.loose() == False :
            self.play_move()
        if self.field.win() :
            return True
        if self.field.loose() :
            return False
            

class ScoobyDoo(Algorithm):

    def play_move(self):       
        if (self.field.grass == -1).all():
            self.field.reveal1(0,0)
            return None
        
                            
                        
    def put_flag_auto(self):
        for x in range(self.field.length):
            for y in range(self.field.width):
                if self.field.grass[x,y] != -1 and self.field.grass[x,y] != 0 : 
                    l = self.field.neighbours(x,y)
                    n = 0
                    for c in l:
                        if self.field.grass[c] == -1 :
                            n += 1
                    if self.field.grass[x,y] == n :
                        for i in l:
                            if self.field.grass[i] == -1:    
                                self.field.put_flag(i[0],i[1]) 

        

    

    def Croc_scooby(self):
        self.put_flag_auto()
        for x in range(self.field.length):
            for y in range(self.field.width):
                if self.field.grass[x, y] != -1 and self.field.grass[x,y] != 0:
                    l = self.field.neighbours(x,y)
                    f = 0
                    for c in l :
                        if 0<= c[0] <= self.field.width and 0<= c[1] <= self.field.length :
                            if self.field.flag[c] == -7 :
                                f += 1 
                    if self.field.grass[x,y] == f :
                        for c in l :
                            if self.field.flag[c[0],c[1]] != -7 :
                                self.field.reveal(c[0],c[1])


                        



    def probabilities(self,x,y):
        a = self.field.grass[x,y]
        l = self.field.neighbours(x,y)
        for c in l:
            n = 0
            if self.field.grass[c] == -1 :
                n += 1
        P = a/n
        return(P)
        
    
    
    
    def frontiere_out(self):
        L=[]
        for i in range(self.field.length):
            for j in range(self.field.width):
                if self.field.grass[i,j] == -1:
                    toto = False
                    for x,y in self.field.neighbours(i,j):
                        if self.field.grass[x,y] !=-1:
                            toto = True
                    if toto == True:
                        L.append((i,j))
        return(L)
                        
    def frontiere_in(self):
        L=[]
        for i in range(self.field.length):
            for j in range(self.field.width):
                if self.field.grass[i,j] != -1:
                    toto = False
                    for x,y in self.field.neighbours(i,j):
                        if self.field.grass[x,y] == -1:
                            toto = True
                    if toto == True:
                        L.append((i,j))
        return(L)
                                          
                        
                        
            
    
    def generate_distributions(self,ncases,nmax, nmin = 0):
        G = []
        for i in range(2**ncases):
            vect = generate_binary(ncases, i)
            if nmin <=sum(vect)<= nmax :
                G.append(vect)
        return(G)    
            
        
        
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   