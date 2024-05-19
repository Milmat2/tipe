import numpy as np
import matplotlib.pyplot as plt
import random

class Field:
    
    def __init__(self, w, l, n_mine):
        self.width = w
        self.length = l
        self.mines = np.zeros((self.width, self.length))
        self.vision = np.zeros((self.width, self.length))
        self.grass =  np.zeros((self.width, self.length))-1
        self.flag = np.zeros((self.width, self.length))-2
        self.n_mine = n_mine
        self.is_generated = False
        self.loose = False
        self.generate_mines()
        
        
        
        
    def generate_mines(self):
        self.is_generated = True
        count = self.n_mine
        while count > 0:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.length-1)
            if not self.mines[x, y]:
                self.mines[x, y] = True
                count = count - 1
            else:
                continue
        
        for x in range(self.width):
            for y in range(self.length):
                if self.mines[x,y] == 1:
                    L = self.neighbours(x,y)
                    for i,j in L:
                        self.vision[i,j] += 1
            
    def reset(self):
        self.is_generated = False
        self.mines = np.zeros((self.width, self.length))
        self.vision = np.zeros((self.width, self.length))
        self.grass =  np.zeros((self.width, self.length))-1
        
        
    def loose(self):
        return self.loose
    
    
    def put_flag(self,x,y):
        self.flag[x, y] = -7
        
                
                    
                
    
    
    
    def win(self):
        A = 0
        for i in range(self.width):
            for j in range(self.length):
                if self.grass[i,j] == -1:
                    A += 1
        return A == self.n_mine
     
       
        
        
    
        
    
        
            
    def reveal(self, x ,y):
        if self.has_mine(x, y):
            print("perdu nullos")
            self.loose = True
        else:
            self.grass[x,y] = self.vision[x,y]
            if self.vision[x,y] == 0:
                for i,j in self.neighbours(x,y):
                    if self.grass[i,j] == -1 and 0 <= i <= self.width and 0 <= j <= self.length :
                        self.reveal(i,j)
        for i in range(self.width):
           for j in range(self.length):
               if self.grass[i, j] != -1:
                   self.flag[i, j] = 0                 
    
   
    def reveal1(self, x ,y):
        while self.vision[x,y] != 0 :
            self.reset()
            self.generate_mines()
        self.reveal(x,y)
        for i in range(self.width):
            for j in range(self.length):
                if self.grass[i, j] != -1:
                    self.flag[i, j] = 0
    

          
    def has_mine(self, x, y):
        if self.mines[x, y]==1:
            return True
        else:
            return False
        
    def neighbours(self, x, y):
        L=[]
        for i in [-1,0,1]:
            for k in [-1,0,1]:
                if 0<=x+i<self.width and 0<=y+k<self.length and (i,k) != (0,0):
                    L.append((x+i,y+k))
                
        return(L)
                
    
    
    def neighbours_ligne(self, x, y):
        L = []
        for i in [-1,1]:
            if 0 <= y+i <= self.length :
                L.append((x,y+i))
        return(L)
        
    
    def neighbours_colonne(self, x, y):
        L = []
        for i in [-1,1]:
            if 0 <= x+i <= self.width :
                L.append((x+i,y))
        return(L)
    
    def neighbours_diagonale(self,x ,y):
        L = []
        for i in [-1,1]:
            for j in [-1,1]:
                 if 0<=x+i<self.width and 0<=y+j<self.length :
                    L.append((x+i,y+j))
        return(L)
    


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
        if self.field.grass.all() == -1:
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
        
    
    def reso_group(self, x, y):
        l = self.field.neighbours(x,y)
        for v in l:
            if self.field.grass[v] == -1:
                
        
                            
                            
                            
                            
                    
                    
                
    


       
