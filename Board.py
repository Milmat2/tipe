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
    


                
        
                            
                            
                            
                            
                    
                    
                
    


       
