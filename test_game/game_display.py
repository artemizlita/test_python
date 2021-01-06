import pygame

pygame.init()

display_width = 1200
display_height = 900

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ship game')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

usr_width = 100
usr_height = 100
ship_move = []
ship_stay = []
for i in range(12):
    ship_move.append(pygame.image.load('lugger\\' + str(i) + '\\sail_1.png'))
    ship_stay.append(pygame.image.load('lugger\\' + str(i) + '\\sail_0.png'))
direction = 0

clock = pygame.time.Clock()

move = False

def run_game():
    global move
    global direction
    usr_x = display_width // 2 - 50
    usr_y = display_height // 2 - 50
    game = True

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            move = True
        elif keys[pygame.K_a]:
            direction -= 0.2
            if direction == -0.2:
                direction = 11.8
        elif keys[pygame.K_d]:
            direction += 0.2
            if direction == 12:
                direction = 0
        elif keys[pygame.K_s]:
            move = False

        display.fill((63, 72, 204))

        if move:
            if round(direction) % 12 == 0:
                usr_x += 1 * 2
                usr_y += 0
            elif round(direction) % 12 == 1:
                usr_x += 0.9 * 2
                usr_y += 0.2 * 2
            elif round(direction) % 12 == 2:
                usr_x += 0.5 * 2
                usr_y += 0.3 * 2
            elif round(direction) % 12 == 3:
                usr_x += 0
                usr_y += 0.4 * 2
            elif round(direction) % 12 == 4:
                usr_x += -0.5 * 2
                usr_y += 0.3 * 2
            elif round(direction) % 12 == 5:
                usr_x += -0.9 * 2
                usr_y += 0.2 * 2
            elif round(direction) % 12 == 6:
                usr_x += -1 * 2
                usr_y += 0
            elif round(direction) % 12 == 7:
                usr_x += -0.9 * 2
                usr_y += -0.2 * 2
            elif round(direction) % 12 == 8:
                usr_x += -0.5 * 2
                usr_y += -0.3 * 2
            elif round(direction) % 12 == 9:
                usr_x += 0
                usr_y += -0.4 * 2
            elif round(direction) % 12 == 10:
                usr_x += 0.5 * 2
                usr_y += -0.3 * 2
            elif round(direction) % 12 == 11:
                usr_x += 0.9 * 2
                usr_y += -0.2 * 2
            image = pygame.transform.smoothscale(ship_move[round(direction) % 12], (88, 75))
            display.blit(image, (usr_x, usr_y))
        else:
            image = pygame.transform.smoothscale(ship_stay[round(direction) % 12], (88, 75))
            display.blit(image, (usr_x, usr_y))

        pygame.display.update()
        clock.tick(5)


run_game()