import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))

running = True
x=400
y=250
circle_x = 200
circle_y = 200
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            x += 5
        if keys[pygame.K_LEFT]:
            x -= 5
        if keys[pygame.K_UP]:
            y -= 5
        if keys[pygame.K_DOWN]:
            y += 5
        if x < 0:
            x = 0
        if x > 720:
            x = 720
        if y < 0:
            y = 0
        if y > 460:
            y = 460
        circle_x += 2
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 80, 40))
    pygame.draw.circle(screen, (0, 255, 0), (circle_x, circle_y), 30)
    pygame.display.flip()

pygame.quit()