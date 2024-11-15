import random
import pygame
import sys
from logic import *

#inteface#

def draw_interface(score):
    screen.fill(MARGIN_COLOR)
    pygame.draw.rect(screen, WHITE, TITLE_RECT)

    font = pygame.font.SysFont('stxingkai', 48)

    text_score = font.render('Счёт: ', 1, GRAY)
    text_score_value = font.render(f'{score}', 1, GRAY)
    screen.blit(text_score, (20, 30))
    screen.blit(text_score_value, (120, 30))

    pretty_printer(mas)
    for row in range(BLOCKS):
        for col in range(BLOCKS):

            value = mas[row][col]
            if value < 8:
                text = font.render(f'{value}', 1, GRAY)
            else:
                text = font.render(f'{value}', 1, WHITE)

            w = col * SIZE_BLOCK + (col + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))

            if value != 0:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))





mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

#Размер поля#
BLOCKS = 4
SIZE_BLOCK = 100
MARGIN = 10
WIDTH = SIZE_BLOCK * BLOCKS + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + SIZE_BLOCK
TITLE_RECT = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)

#colors#
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (122, 110, 93)
MARGIN_COLOR = (187, 173, 162)
COLORS = {
    0: (205, 193, 181),
    2: (240, 230, 221),
    4: (236, 223, 203),
    8: (241, 177, 123),
    16: (242, 152, 105),
    32: (242, 125, 99),
    64: (244, 96, 69),
    128: (235, 206, 118),
    256: (237, 203, 103),
    512: (236, 200, 89),
    1024: (232, 194, 88),
    2048: (176, 22, 219)
}


mas[1][2] = 2  #строка и столбик#
mas[3][0] = 4
score = 0

print(get_empty_list(mas))
pretty_printer(mas)


#POle igry#
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')


def draw_game_over():
    global mas, score
    font = pygame.font.SysFont('stxingkai', 48)
    text_game_over = font.render("Игра окончена", True, WHITE)
    text_restart = font.render("Нажмите ПРОБЕЛ", True, WHITE)
    text_restart1 = font.render("чтобы сыграть снова", True, WHITE)
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart = True
                    mas = [
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                    ]
                    mas[1][2] = 2  # строка и столбик#
                    mas[3][0] = 4
                    score = 0
        screen.fill(BLACK)
        screen.blit(text_game_over, (110,80))
        screen.blit(text_restart, (80, 120))
        screen.blit(text_restart1, (50, 160))
        pygame.display.update()

def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()


    #-----------Обработчик------------#
    while is_zero_in_mas(mas) or can_move(mas):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit(0)


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mas, delta = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta = move_right(mas)

                elif event.key == pygame.K_UP:
                    mas, delta = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta = move_down(mas)
                else:
                    continue

                score += delta
                score += delta
                if is_zero_in_mas(mas):
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                    print(f"Заполнен элемент с номером {random_num}")
                draw_interface(score)
                pygame.display.update()
while True:
    game_loop()
    draw_game_over()