NORTH = 0
EAST  = 1
SOUTH = 2
WEST  = 3
NtoS  = 0
StoN  = 1
EtoW  = 2
WtoE  = 3

MAZE_WIDTH = 3

class Passage():
    pass

class OneWayPassage():
    def __init__(self,direction):
        self.direction=direction
    pass

class Wall():
    pass

class Door():
    pass

class LockedDoor():
    def __init__(self, key, locked=True):
        self.key    = key
        self.locked = locked
    pass

class SecretDoor():
    pass

class Cell:
    def __init__(self,
                 n    = Passage(),
                 e    = Passage(),
                 dark = False):
        self.n    = n
        self.e    = e
        self.dark = dark

class MessageCell(Cell):
    def __init__(self,message=""):
        self.message = message

class Maze:
    def __init__(self, width):
        self.width = width
        self.first  = 0
        self.last   = width - 1
        self.size   = width * width
        self.cells  = []
        for i  in range(self.size):
            self.cells.append(Cell())

    def xy_to_id(self, x, y):
        return(x + y * self.width)

    def id_to_xy(self, index):
        return(divmod(index, self.width))

    def modified(self, x, y):
        mx=x
        my=y
        if mx<0:
            mx = x + self.width
        elif mx>self.last:
            mx = x - self.width
            if my<0:
                my = y + self.width
            elif my>self.last:
                my = y - self.width
        return(mx, my)
    
    def read(self, filename):
        pass
    def write(self, filename):
        pass

    def draw(self):
        for y in range(self.width):
            for x in range(self.width):
                print("+", end="")
                if type(self.cells[self.xy_to_id(x,y)].n) is Passage :
                    print(" ", end="")
                else:
                    print("-", end="")
            print("+")
            if type(self.cells[self.xy_to_id(self.width-1, y)].e) is Passage :
                print(" ", end="")
            else:
                print("|", end="")
            for x in range(self.width):
                print(".", end="")
                if type(self.cells[self.xy_to_id(x,y)].e) is Passage:
                    print(" ", end="")
                else:
                    print("|", end="")
            print()
        print("+", end="")
        for x in range(self.width):
            if type(self.cells[self.xy_to_id(x,self.first)].n) is Passage :
                print(" ", end="")
            else:
                print("-", end="")
            print("+", end="")
        print()


def edit_maze(m):
    quit_editor=False
    command_list=['W','P','D','Q']
    while quit_editor==False:
        m.draw()
        print("W)all P)assage D)oor Q)uit")
        command=input('>')[0].upper()
        print(command)
        if command in command_list:
            if command=='Q':
                quit_editor=True

if __name__=="__main__":
    print("Maze Maker ver. 0.1")

    quit_maker  = False
    maze         = None
    maze_exist   = False
    maze_filename = ""
    command_list = ['M', 'R', 'W', 'E', 'Q']

    while(quit_maker==False):
        print("Maze File:", maze_filename)
        print("M)ake C)hangeFile R)ead W)rite E)dit Q)uit")
        command=input('>')[0].upper()
        if command in command_list:
            if command=='C':
                maze_filename=input("ファイル名:")
            if command=='M':
                maze=Maze(int(input("迷路のサイズ:")))
            elif command=='R':
                if maze_filename=="":
                    print("ファイル名が入力されていません。")
                else:
                    maze.read(maze_filename)
            elif command=='W':
                if maze_filename=="":
                    print("ファイル名が入力されていません。")
                else:
                    maze.write(maze_filename)
            elif command=='E':
                edit_maze(maze)
            elif command=='Q':
                quit_maker=True
