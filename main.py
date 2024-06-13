import pygame
from sys import exit


class Cell():

    def __init__(self,rect,width,height,color='black'):
        self.surface = rect
        self.width = width
        self.height = height
        self.color = color
        if self.color == 'white': self.isAlive = True
        else: self.isAlive = False

        if color:self.surface.fill(color)

    def set_color(self,color):
        self.surface.fill(color)
        self.color = color
        if self.color == 'white': self.isAlive = True
        else: self.isAlive = False

    def __str__(self) -> str:
        return f'rect:[{self.rect}] width:[{self.width}]'


def get_neighbours(cell,cell_x,cell_y):
    global x 
    global y
    neighbour = []
    

    neighbour.append((cell_x+1,cell_y))
    neighbour.append((cell_x-1,cell_y))
    neighbour.append((cell_x,cell_y+1))
    neighbour.append((cell_x,cell_y-1))
    neighbour.append((cell_x-1,cell_y-1))
    neighbour.append((cell_x+1,cell_y-1))
    neighbour.append((cell_x-1,cell_y+1))
    neighbour.append((cell_x+1,cell_y+1))

    tmp = []
    for n in neighbour:
        if n[0] >= 0 and n[1] >= 0 and n[0] < x and n[1] < y:
            tmp.append(grid[n[0]][n[1]])

    neighbour = tmp

    return neighbour
    



    


pygame.init()
#set screen width and height
screen = pygame.display.set_mode((1000,1000))
#for title 
pygame.display.set_caption("Game of Life")
#for fps
clock = pygame.time.Clock()

t=0

x = 30
y = 30
num = 50

grid = [[Cell(pygame.Surface((29,29)),i*x,j) for i in range(num)] for j in range(0,num*y,y)]
# surf = pygame.Surface((50,50))


#startup
grid[5][5].set_color('white')
grid[5][4].set_color('white')
grid[6][5].set_color('white')
grid[6][4].set_color('white')

grid[4][4].set_color('white')
grid[5][3].set_color('white')
grid[3][4].set_color('white')
grid[4][7].set_color('white')
grid[4][2].set_color('white')

grid[10][4].set_color('white')
grid[11][3].set_color('white')
grid[9][11].set_color('white')
grid[15][7].set_color('white')
grid[12][2].set_color('white')

grid[7][9].set_color('white')
grid[7][10].set_color('white')
grid[7][11].set_color('white')
grid[6][10].set_color('white')

grid[9][8].set_color('white')
grid[10][8].set_color('white')
grid[11][8].set_color('white')
grid[12][8].set_color('white')






while True:
    #check which event is invoked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    
    screen.fill((200,200,200))
    for line in grid:
        for surf in line:
            screen.blit(surf.surface,(surf.width,surf.height))
    
    next_gen = [[False for _ in range(y)] for _ in range(x)]
    
    
    for i in range(x):
        for j in range(y):
            # if grid[i][j].isAlive:
                neighbour = get_neighbours(grid[i][j],i,j) 

                aliveSum = len([n for n in neighbour if n.isAlive])
                
                cell = grid[i][j]

                if cell.isAlive:
                    if aliveSum == 2 or aliveSum == 3:
                        next_gen[i][j] = True
                elif not cell.isAlive:
                    if aliveSum == 3:
                        next_gen[i][j] = True
                
                

    for i in range(x):
        for j in range(y):
            if next_gen[i][j] :
                grid[i][j].set_color('white')
            else:
                grid[i][j].set_color('black')  
                         

    
    t+=1
    print(f'{t} generation')
    #update screen
    pygame.display.update()
    
    #set fps to 60
    clock.tick(10) 
