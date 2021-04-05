import random


class Tetris:
    '''A simple game.'''

    def __init__(self):
        self.i_shape = [[1, 1, 1, 1]]
        self.l_shape = [[1], [1], [1, 1]]
        self.j_shape = [[0, 1], [0, 1], [1, 1]]
        self.s_shape = [[0, 1], [1, 1], [1, 0]]
        self.o_shape = [[1, 1], [1, 1]]
        self.current_shape = None
        self.boards=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.new_boards = []
        self.current_pos = []
        self.pos_dict = {}
        self.new_pos = []
        self.new_pos_dict = {}


    def draw_screen(self):
        '''Draws first screen, makes first block not overlaping with borders.'''

        num_of_ones = sum(num.count(1) for num in self.boards)
        board_func = self.boards
        while True:
            shape = random.choice([self.i_shape, self.l_shape, self.j_shape,
                                   self.s_shape, self.o_shape])
            position = random.randint(1, 20)
            m = 0
            for i in range(len(shape)):
                sub_shape = shape[m]
                n = 0
                pos = position
                for i in range(len(sub_shape)):
                    if sub_shape[n] == 1 and pos <= 21: board_func[m][pos] = 1
                    pos += 1
                    n += 1
                m += 1
            if (num_of_ones+4) == (sum(num.count(1) for num in board_func)):
                break
            else:
                board_func=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        self.boards = board_func
        self.current_shape = shape
        for board in self.boards:
            print(*["*" if elem == 1 else " " for elem in board], sep='')
            self.current_pos.append([i for i, x in enumerate(board) if x == 1])
        for pos in self.current_pos:
            pos.remove(0)
            pos.remove(21)
        for i, pos in enumerate(self.current_pos[:-1]):
            if len(pos) > 0:
                self.pos_dict[i] = pos
        self.move()


    def move(self):
        '''
        Operate block fragments on the board; implemented for a/d and partially
        for w. Pressing q quits the game; pressing any other key changes
        currently operated block into a new one, emerging on top of the board.
        '''

        num_of_ones = sum(num.count(1) for num in self.boards)
        self.new_boards = self.boards
 #'print' here and below - if uncommented, user can see changing coordinates
#        print(self.pos_dict)
        while True:
            if num_of_ones != (sum(num.count(1) for num in self.new_boards)):
                self.redraw()
            for board in self.new_boards:
                print(*["*" if elem == 1 else " " for elem in board], sep='')
            move = input()
            for k in self.pos_dict.keys():
                for item in self.pos_dict.get(k):
                    self.new_boards[k][item] = 0

            if move == "d":
#                print(self.pos_dict)
                for k in self.pos_dict.keys():
                    for item in self.pos_dict.get(k):
                        self.new_boards[k+1][item+1] = 1
                self.pos_dict = {k+1: v for k, v in self.pos_dict.items()}
                self.pos_dict = {k: [x+1 for x in v] for k,
                                 v in self.pos_dict.items()}
#                print(self.pos_dict)
                continue

            if move == "a":
#                print(self.pos_dict)
                for k in self.pos_dict.keys():
                    for item in self.pos_dict.get(k):
                        self.new_boards[k+1][item-1]=1
                self.pos_dict = {k+1: v for k, v in self.pos_dict.items()}
                self.pos_dict = {k: [x-1 for x in v] for k,
                                 v in self.pos_dict.items()}
#                print(self.pos_dict)
                continue

            if move == "w":
#                print(self.pos_dict)
                if self.current_shape == [[1, 1], [1, 1]]:
                    for k in self.pos_dict.keys():
                        for item in self.pos_dict.get(k):
                            self.new_boards[k+1][item+1] = 1
                    self.pos_dict = {k+1: v for k, v in self.pos_dict.items()}
                    self.pos_dict = {k: [x+1 for x in v] for k,
                                     v in self.pos_dict.items()}
                elif self.current_shape == [[1, 1, 1, 1]]:
                    self.pos_dict = {k+1: v for k, v in self.pos_dict.items()}
                    row = list(self.pos_dict.keys())[0]
                    col = self.pos_dict.get(row)[-1] #0 for 's' key
                    for i in range(4):
                        self.new_boards[row-i][col] = 1
                    pass
                    #unfinished block: update pos_dict
                    #
                    #{9: [10, 11, 12, 13]}into:
                    #10:10, 9:10, 8:10, 7:10
#                print(self.pos_dict)
                continue

            #unfinished for j and l shapes

            #if move == "s": rotate clockwise thrice

            elif move == "q":
                quit()
            else:
                continue


    def redraw(self):
        '''Re-draws board after a fragment collided with another/with frame'''

        self.new_pos = []
        self.current_pos = []
        self.pos_dict = {}
        for board in self.boards:
            self.current_pos.append([i for i, x in enumerate(board) if x == 1])
        for pos in self.current_pos:
            pos.remove(0)
            pos.remove(21)
        for i, pos in enumerate(self.current_pos[:-1]):
            if len(pos) > 0:
                self.pos_dict[i] = pos
        for board in self.boards:
            print(*["*" if elem == 1 else " " for elem in board], sep='')
            self.current_pos.append([i for i, x in enumerate(board) if x == 1])
        num_of_ones = sum(num.count(1) for num in self.boards)
        board_func = self.boards
        while True:
            shape = random.choice([self.i_shape, self.l_shape, self.j_shape,
                                   self.s_shape, self.o_shape])
            position = random.randint(1, 20)
            m = 0
            for i in range(len(shape)):
                sub_shape = shape[m]
                n = 0
                pos = position
                for i in range(len(sub_shape)):
                    if sub_shape[n] == 1 and pos <= 21: board_func[m][pos] = 1
                    pos += 1
                    n += 1
                m += 1
            if (num_of_ones+4) == (sum(num.count(1) for num in board_func)):
                break
            else:
                board_func = self.boards
        for board in board_func:
            self.new_pos.append([i for i, x in enumerate(board) if x == 1])
        print(self.new_pos)
        for pos in self.new_pos:
            pos.remove(0)
            pos.remove(21)
        for i, pos in enumerate(self.new_pos[:-1]):
            if len(pos) > 0:
                self.new_pos_dict[i] = pos
        for key in self.pos_dict.keys() & self.new_pos_dict.keys():
            del self.new_pos_dict[key]
        self.pos_dict = self.new_pos_dict
        self.new_pos_dict = {}
        self.boards = board_func
        self.current_shape = shape
        for board in self.boards:
            print(*["*" if elem == 1 else " " for elem in board], sep='')
        self.move()


game = Tetris()
game.draw_screen()
