player_name = []
name = input('Enter the name of the player 1. ')
player_name.append(name)
name = input('Enter the name of the player 2. ')
player_name.append(name)
S = []
for i in  range(8):
    row = []
    for j in range(8):
        row.append('**')
    S.append(row)  

def show():
    for i in S:
        print('\n\n')
        for j in i:
            print(j, end='  '*6)

def set_screen(self):
    for i in range(8):
        for j in range(8):
            if S[i][j] not in player[0] and S[i][j] not in player[1]:
                S[i][j] = '**'

player =  [['🤘','🐴','🗻','👸','👑','🗻','🐴','🤘','\b💂1','\b💂2','\b💂3','\b💂4','\b💂5','\b💂6','\b💂7','\b💂8'],
            ['💣','🐎','🌄','🤴','🌰','🌄','🐎','💣','\b👮1','\b👮2','\b👮3','\b👮4','\b👮5','\b👮6','\b👮7','\b👮8']]
def move(self):
        xy = int(input('\nChoice: '))
        if int(xy) in self.place_able:
            S[self.x][self.y] = '**'
            self.x = int(xy/10)
            self.y = int(xy%10)                        
            set_screen(self)
            for i in self.save:
                if self.id == 0:
                    if S[i[1]][i[2]] not in player[1] :
                        S[i[1]][i[2]] = i[0]
                if self.id == 1:
                    if S[i[1]][i[2]] not in player[0] :
                        S[i[1]][i[2]] = i[0]
            self.save.clear()
            for i in self.destroy:
                if i[0] == player[self.opponent][4]:
                    print(player_name[self.id], 'Won the game')
                    exit()
                S[i[1]][i[2]] = '**'
            self.destroy.clear()
            S[self.x][self.y] = self.goti
            set_screen(self)
            show()
            self.place_able.clear()
        else:
            print('Invalid input\a')
            move(self)
        
        


class char:
    destroy = []
    save = []
    place_able = []

    def __init__(self, goti, x , y, id):
        self.x = x
        self.y = y
        self.goti = goti
        self.id = id
        S[self.x][self.y] = '' + self.goti
        if id==0:
            self.opponent = 1
        if id == 1:
            self.opponent = 0

class Pawn(char):
    first  = True        
    def which_move(self):
        x = 12
        enum = 0
        if self.id == 0:
            x = 1
            enum = -1
        if self.id == 1:
            x = -1
            enum = 1
        if self.x+x in range(8):   
            if S[self.x+x][self.y]=='**' :
                S[self.x+x][self.y] =  str(self.x+x) + str(self.y)
                self.place_able.append((self.x+x)*10 + self.y)
            if self.y + x in range(8):
                if S[self.x+x][self.y+x] in player[self.opponent]:
                    self.save.append([S[self.x+x][self.y+x],self.x+x,self.y+x])
                    self.destroy.append([S[self.x+x][self.y+x], self.x, self.y])
                    S[self.x+x][self.y+x]= str(self.x+x)+str(self.y+x)
                    self.place_able.append((self.x+x)*10 + self.y+x)
            if self.y+enum in range(8):
                if S[self.x+x][self.y+enum] in player[self.opponent]:
                    self.save.append([S[self.x+x][self.y+enum],self.x+x,self.y+enum])
                    self.destroy.append([S[self.x+x][self.y+enum], self.x, self.y])
                    S[self.x+x][self.y+enum]= str(self.x+x)+str(self.y+enum)
                    self.place_able.append((self.x+x)*10 + self.y+enum)
                
            if self.first:
                x *= 2
                if S[self.x+x][self.y]=='**' :
                    S[self.x+x][self.y] =  str(self.x+x) + str(self.y)
                    self.place_able.append((self.x+x)*10 + self.y)
                if self.y + x in range(8):
                    if S[self.x+x][self.y+x] in player[self.opponent]:
                        self.save.append([S[self.x+x][self.y+x],self.x+x,self.y+x])
                        self.destroy.append([S[self.x+x][self.y+x], self.x, self.y])
                        S[self.x+x][self.y+x]= str(self.x+x)+str(self.y+x)
                        self.place_able.append((self.x+x)*10 + self.y+x)
                if self.y+enum in range(8) and S[self.x+x][self.y+enum] in player[self.opponent]:
                    self.save.append([S[self.x+x][self.y+enum],self.x+x,self.y+enum])
                    self.destroy.append([S[self.x+x][self.y+enum], self.x, self.y])
                    S[self.x+x][self.y+enum]= str(self.x+x)+str(self.y+enum)
                    self.place_able.append((self.x+x)*10 + self.y+x+2)
                self.first = False                                
        else:
            z = 0
            if self.id == 0:
                z == int(input('\n1. 🤘\n2. 🐴\n3. 🗻\n4. 👸\nSelect power:  '))
                if z == 1:
                    new = Rook(player[self.id][z-1],self.x,self.y,self.id)
                    player1[selelect_player-1] = new
                    player[self.id][selelect_player-1] = player[self.id][z-1]                     
                elif z == 2:
                    player1[selelect_player-1] = Horse(player[self.id][z-1],self.x,self.y,self.id)
                elif z == 3:
                    player1[selelect_player-1] = Bishop(player[self.id][z-1],self.x,self.y,self.id)
                elif z == 4:
                    player1[selelect_player-1] = Queen(player[self.id][z-1],self.x,self.y,self.id)
            elif self.id == 1:
                z == int(input('\n1. 💣\n2. 🐎\n3. 🌄\n4. 🤴\nSelect power:  '))
                if z == 1:
                    player2[selelect_player-1] = Rook(player[self.id][z-1],self.x,self.y,self.id)
                elif z == 2:
                    player2[selelect_player-1] = Horse(player[self.id][z-1],self.x,self.y,self.id)
                elif z == 3:
                    player2[selelect_player-1] = Bishop(player[self.id][z-1],self.x,self.y,self.id)
                elif z == 4:
                    player2[selelect_player-1] = Queen(player[self.id][z-1],self.x,self.y,self.id)
        if self.place_able:
            show()
            move(self)
        else:
            print('Invalid Selection\a')
            
            
            

class King(char):
    def which_move(self):
        i = self.x - 1
        j = self.y - 1
        for k in range(3):
            for v in range(3):
                if i+k in range(8) and j+v in range(8):
                    if S[i+k][j+v] == '**' or S[i+k][j+v] in player[self.opponent]:
                        S[i+k][j+v] = str(i+k)+str(j+v)
                        self.save.append([S[i+k][j+v],i+k,j+v])
                        self.destroy.append([S[i+k][j+v], self.x,self.y])
                        self.place_able.append((i+k)*10 + j+v)
        
        
        if self.place_able:
            show()            
            move(self)
            set_screen(self)
        else:
            print('Invalid Selection')



class Rook(char):
    def which_move(self):
        r = self.y + 1
        while r <= 7:
            if S[self.x][r] == '**' or S[self.x][r] in player[self.opponent]:
                self.destroy.append([S[self.x][r],self.x,self.y])
                self.save.append([S[self.x][r],self.x,r])
                stop = S[self.x][r]
                S[self.x][r] = str(self.x) + str(r)
                self.place_able.append(self.x*10 + r)
                if stop in player[self.opponent]:
                    r = 8
                r += 1
            else:
                break
        
        r = self.y - 1
        while r >= 0:
            if S[self.x][r] == '**' or S[self.x][r] in player[self.opponent]:
                self.destroy.append([S[self.x][r],self.x,self.y])
                self.save.append([S[self.x][r],self.x,r])
                stop = S[self.x][r]
                S[self.x][r] = str(self.x) + str(r)
                self.place_able.append(self.x*10 + r)
                if stop in player[self.opponent]:
                    r = -1
                r -= 1
            else:
                break
        ####################################
        r = self.x + 1
        while r <= 7:
            if S[r][self.y] == '**' or S[r][self.y] in player[self.opponent]:
                self.destroy.append([S[r][self.y],self.x,self.y])
                self.save.append([S[r][self.y],r,self.y])
                stop = S[r][self.y]
                S[r][self.y] = str(r) + str(self.y)
                self.place_able.append(r*10 + self.y)
                if stop in player[self.opponent]:
                    r = 8
                r += 1
            else:
                break
        
        r = self.x - 1
        while r >= 0:
            if S[r][self.y] == '**' or S[r][self.y] in player[self.opponent]:
                self.destroy.append([S[r][self.y],self.x,self.y])
                self.save.append([S[r][self.y],r,self.y])
                stop = S[r][self.y]
                S[r][self.y] = str(r) + str(self.y)
                self.place_able.append(r*10 + self.y)
                if stop in player[self.opponent]:
                    r = -1
                r -= 1
            else:
                break        
        if self.place_able:
            show()
            move(self)
        else:
            print('Invalid Selection')  


class Horse(char):
    def which_move(self):
        i = self.x - 2
        j = self.y - 1
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
            
        i = self.x - 2
        j = self.y + 1
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        
        i = self.x + 2
        j = self.y - 1
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        
        i = self.x + 2
        j = self.y + 1
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        
        i = self.x + 1
        j = self.y - 2
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        
        i = self.x - 1
        j = self.y - 2
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        
        i = self.x + 1
        j = self.y + 2
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        
        i = self.x - 1
        j = self.y + 2
        if i in range(8) and j in range(8) and  S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
        if self.place_able:
            show()
            move(self)
        else:
            print('Invalid Selection')


class Bishop(char):
    def which_move(self):
        i = self.x-1
        j = self.y+1
        while i in range(8) and j in range(8) and S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            stop = S[i][j]
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
            if stop in player[self.opponent]:
                i = -1
            i -= 1
            j += 1
            
        i = self.x-1
        j = self.y-1
        while i in range(8) and j in range(8) and S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            stop = S[i][j]
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
            if stop in player[self.opponent]:
                i = -1
            i -= 1
            j -= 1
            
        i = self.x+1
        j = self.y-1
        while i in range(8) and j in range(8) and S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            self.save.append([S[i][j],i,j])
            stop = S[i][j]
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
            if stop in player[self.opponent]:
                i = 8
            i += 1
            j -= 1
        
        i = self.x+1
        j = self.y+1
        while i in range(8) and j in range(8) and S[i][j] not in player[self.id]:
            self.destroy.append([S[i][j],self.x,self.y])
            stop = S[i][j]
            S[i][j] = str(i) + str(j)
            self.place_able.append(10*i + j)
            if stop in player[self.opponent]:
                i = 8
            i += 1
            j += 1
        if self.place_able:
            show()
            move(self)
        else:
            print('Invalid Selection')


class Queen(Bishop):
    def which_move(self):
        j = self.x - 1
        i = self.x + 1
        y = self.y + 1
        z = self.y - 1
        while (i in range(8) or j in range(8)) or (y in range(8) or z in range(8)):
            if i in range(8) and S[i][self.y] not in player[self.id]:
                self.save.append([S[i][self.y],i,self.y])
                self.destroy.append([S[i][self.y],self.x,self.y])
                stop = S[i][self.y]
                S[i][self.y] = str(i) + str(self.y)
                self.place_able.append(10*i + self.y)
                if stop in player[self.opponent]:
                    i = 8      
            else:
                i = 8                
            i += 1
            if j in range(8) and S[j][self.y] not in player[self.id]:
                self.save.append([S[j][self.y],j,self.y])
                self.destroy.append([S[j][self.y],self.x,self.y])
                stop = S[j][self.y]
                S[j][self.y] = str(j) + str(self.y)
                self.place_able.append(10*j + self.y)
                if stop in player[self.opponent]:
                    j = -1
            else:
                j = -1    
            j -= 1
            if y in range(8) and S[self.x][y] not in player[self.id]:
                self.save.append([S[self.x][y],self.x,y])
                self.destroy.append([S[self.x][y],self.x,self.y])
                stop = S[self.x][y]
                S[self.x][y] = str(self.x) +  str(y)
                self.place_able.append(self.x*10 + y)
                if stop in player[self.opponent]:
                    y = 8
            else:
                y = 8                
            y += 1
            if z in range(8) and S[self.x][z] not in player[self.id]:
                self.save.append([S[self.x][z],self.x,z])
                self.destroy.append([S[self.x][z],self.x,self.y])
                stop = S[self.x][z]
                S[self.x][z] = str(self.x) + str(z)
                self.place_able.append(self.x*10 + z)
                if stop in player[self.opponent]:
                    z = -1
            else:
                z = -1                
            z -= 1
        Bishop.which_move(self)


player1 = []
player2 = []

player1.append(Rook(player[0][0],0,0,0))
player1.append(Horse(player[0][1],0,1,0))
player1.append(Bishop(player[0][2],0,2,0))
player1.append(Queen(player[0][3],0,3,0))
player1.append(King(player[0][4],0,4,0))
player1.append(Bishop(player[0][5],0,5,0))
player1.append(Horse(player[0][6],0,6,0))
player1.append(Rook(player[0][7],0,7,0))

player2.append(Rook(player[1][0],7,0,1))
player2.append(Horse(player[1][1],7,1,1))
player2.append(Bishop(player[1][2],7,2,1))
player2.append(Queen(player[1][3],7,3,1))
player2.append(King(player[1][4],7,4,1))
player2.append(Bishop(player[1][5],7,5,1))
player2.append(Horse(player[1][6],7,6,1))
player2.append(Rook(player[1][7],7,7,1))

for i in range(8):
    player1.append(Pawn(player[0][i+8],1,i,0))    
    player2.append(Pawn(player[1][i+8],6,i,1))



while True:
    j = 1
    print('')
    for i in player[0]:
        print(j,'-', i, end='    ')
        if j == 8:
            print('')
        j += 1
    print('')
    selelect_player = int(input('Select Player1: '))
    if selelect_player in range(16):
        player1[selelect_player-1].which_move()    
    j = 1
    print('\n'*4)
    for i in player[1]:
        print(j,'-', i, end='    ')
        if j == 8:
            print('')
        j += 1
    print('')
    selelect_player = int(input('Select Player2: '))
    if selelect_player in range(16):
        player2[selelect_player-1].which_move()
