import pygame
from pygame.locals import * 
import sys
import random
import copy

pygame.init()

max_row = 20 
max_col = 10

class Block:
    def __init__(self, block_type):
        self.shapes = [[],[],
                        [[0,-1], [0, 0], [0, 1], [0, 2]],  # I block
                        [[-1, -1], [0, -1], [0, 0], [0, 1]], # J block
                        [[0, -1], [0, 0], [0, 1], [-1, 1]], # L block
                        [[0, -1], [0, 0], [-1, 0], [-1, 1]], # S blosk
                        [[-1, -1], [-1, 0], [0, 0], [0, 1]], # Z block
                        [[0, -1], [0, 0], [-1, 0], [0, 1]], # T block
                        [[0, 0], [-1, 0], [0, 1], [-1, 1]]] # square]
        self.bloke_type = block_type
        self.shape = copy.deepcopy(self.shapes[block_type])
        self.row = 1
        self.col = 5
        self.level = 0
        self.drop_rate = [60, 50, 45, 42, 39, 36, 35, 34, 33, 32, 31, 
                            30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 
                            20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 
                            10,  9,  8,  7,  6,  5,  4,  3,  2,  1, 0]
        self.count = 60
        self.hold_flag = True
        
    # key command movement
    def move(self, board, directtion):
        if directtion == 0 and self.moveable(board, [1, 0]):
            self.row += 1
        elif directtion == 1 and self.moveable(board, [0, -1]):
            self.col -= 1
        elif directtion == 2 and self.moveable(board, [0,1]):
            self.col += 1
        elif directtion == 3:
            self.row += self.bottom(board)
            self.count = 60
    
    def bottom(self, board):
        direction = [1, 0]
        while self.moveable(board, direction):
            direction[0] += 1
        return direction[0]-1
    
    def rotate(self, board, direction):
        if self.bloke_type == 2:
            if direction == 0:
                for dx in self.shape:
                    dx[0],dx[1] = dx[1], 1-dx[0]
            elif direction == 1:
                for dx in self.shape:
                    dx[0],dx[1] = 1-dx[1], dx[0]
            
        elif self.block_type == 8:
            pass
                
        
        elif direction == 0:
            for dx in self.shape:
                dx[0], dx[1] = dx[1], -dx[0]
        elif direction == 1:
            for dx in self.shape:
                dx[0], dx[1] = -dx[1], dx[0]
        
        self.rotate_correction(board)
        
    def drop(self, screen, board):
        if self.count < self.drop_rate[self.level]:
            self.count += 1
            return 0
        elif self.moveable(board, [1, 0]):
            self.count = 0
            self.row += 1
            return 0
        else:
            return 1
        
    def moveable(self, board, direction):
        drow, dcol = direction
        
        for dx in self.shape:
            row = self.row = dx[0] + drow
            col = self.col + dx[1] + dcol
            if 0 <= row < max_row + 3 and 0 <= col < max_col + 2 and board[row][col] != 0:
                return False
        return True
    
    def rotate_correction(self, board):
        move_priority = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0], [2, 0], [-1, 1], [1, 1]]
        for direction in move_priority:
            if self.moveable(board, direction):
                self.row += direction[0]
                self.col += direction[1]
                return
        direction = [0, 2]
        while not self.moveable(board, direction):
            direction[1] += 1
        self.row += direction[0]
        self.col += direction[1]
    
    def draw(self, screen, block_color, board):
        drow = self.bottom(board)
        for row, col in self.shape:
            row += self.row + drow
            col += self.col
            if row > 1:
                pygame.draw.rect(screen, block_color[self.block_type], Rect(30+35*col, 30+35*(row-2), 35, 35))
                pygame.draw.rect(screen, block_color[10], Rect(32+35*col, 32+35*(row-2), 31, 31))
                
        for row, col in self.shape:
            row += self.row
            col += self.col
            if row > 1:
                pygame.draw.rect(screen, (0, 0, 0), Rect(30+35*col, 30+35*(row-2), 35, 35))
                pygame.draw.rect(screen, block_color[self.block_type], Rect(32+35*col, 32+35*(row-2), 31, 31))
        
    def place(self,screen, board, record):
        for dx in self.shape:
            row = self.row + dx[0]
            col = self.col + dx[1]
            if not ((2 <= row < max_row + 2 ) and ( 1 <= col < max_col + 1)):
                gameover(screen, record)
                return 1
            board[row][col] = self.block_type
        return 0
    
class Record:
    def __init__(self):
        self.cleared_row = 0
        self.score = 0
        self.level = 0
        self.score_table = [0, 80, 100, 300, 1200]
        self.level_up = [2, 5, 8, 12, 16, 20, 25, 30, 35, 40, # level 0 to 9
                        46, 52, 58, 64, 70, 77, 84, 91, 98, 105, # level 10 to 19
                        112, 120, 128, 136, 144, 152, 160, 168, 177, 186, # level 20 to 29
                        195, 204, 213, 222, 231, 240, 255, 270, 285, 300, 1000] # 30 to 40
        
        def update(self, count):
            self.score += self.score_table[count]*(self.level+1)
            self.cleared_row += count
            
            if self.level < 40 and self.level_up[self.level] <= self.cleared_row:
                self.level  += 1
        def show(self, screen):
            font = pygame.font.Font(None, 50)
            text1 = font.render("LEVEL:", True, (255, 255, 255))
            level = font.render("{}".format(self.level), True, (255, 255, 255))
            screen.blit(text1, [500, 300])
            screen.blit(level, [700, 300])
            
            text2 = font.render("CLEARED ROW", True, (255, 255, 255))
            cleared_row = font.render("{}".format(self.cleared_row), True, (255,255,255))
            