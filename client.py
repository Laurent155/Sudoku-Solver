import pygame

width = 611
height = 611
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku")
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 35)


def draw_window(window):
    window.fill((255, 255, 255))
    pygame.draw.line(window, (0, 0, 0), (0, 0), (611, 0), 1)
    for i in range(1, 10):
        pygame.draw.line(window, (0, 0, 0), (0, 68 * i), (611, 68 * i), 1)
        pygame.draw.line(window, (0, 0, 0), (68 * i, 0), (68 * i, 611), 1)
    for i in range(1, 4):
        pygame.draw.line(window, (0, 0, 0), (0, 68 * i * 3), (611, 68 * i * 3), 2)
        pygame.draw.line(window, (0, 0, 0), (68 * i * 3, 0), (68 * i * 3, 611), 2)


def update_window(window, board, c, r):
    draw_window(window)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                number = myfont.render(str(board[i][j]), False, (0, 0, 0))
                win.blit(number, (j * 68 + 28, i * 68 + 11))
    if r != -1:
        pygame.draw.line(window, (0, 255, 0), (r * 68, c * 68), (r * 68, c * 68 + 68), 2)
        pygame.draw.line(window, (0, 255, 0), (r * 68, c * 68), (r * 68 + 68, c * 68), 2)
        pygame.draw.line(window, (0, 255, 0), (r * 68 + 68, c * 68), (r * 68 + 68, c * 68 + 68), 2)
        pygame.draw.line(window, (0, 255, 0), (r * 68, c * 68 + 68), (r * 68 + 68, c * 68 + 68), 2)
    pygame.display.update()


def update_window_false(window, board, c, r, number_tried):
    draw_window(window)
    for i in range(9):
        for j in range(9):
            if (i, j) != (c, r):
                if board[i][j] != 0:
                    number = myfont.render(str(board[i][j]), False, (0, 0, 0))
                    win.blit(number, (j * 68 + 28, i * 68 + 11))
    number = myfont.render(str(number_tried), False, (0, 0, 0))
    win.blit(number, (r * 68 + 28, c * 68 + 11))
    pygame.draw.line(window, (255, 0, 0), (r * 68, c * 68), (r * 68, c * 68 + 68), 2)
    pygame.draw.line(window, (255, 0, 0), (r * 68, c * 68), (r * 68 + 68, c * 68), 2)
    pygame.draw.line(window, (255, 0, 0), (r * 68 + 68, c * 68), (r * 68 + 68, c * 68 + 68), 2)
    pygame.draw.line(window, (255, 0, 0), (r * 68, c * 68 + 68), (r * 68 + 68, c * 68 + 68), 2)
    pygame.display.update()


def complete_window(window):
    window.fill((255, 255, 255))
    text_surface = myfont.render('Complete!', False, (0, 0, 0))
    window.blit(text_surface, (230, 273))
    pygame.display.update()
