from pygame import *

#створи вікно гри
window = display.set_mode((1200, 900))
display.set_caption('Runer')
clock = time.Clock()
FPS = 60  

#задай фон сцени
background = transform.scale(image.load('background.png'), (1200, 900))

#створення спрайтів
sprite1 = transform.scale(image.load('sprite1.png'), (100,100))
sprite2 = transform.scale(image.load('sprite2.png'), (100,100))

#змінні x1 та x2, y1, y2
x1 = 100
x2 = 300
y1 = 200
y2 = 200

#змінна speed
speed = 12

#ігровий цикл
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (0,0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    keys_pressed = key.get_pressed()

    if keys_pressed [K_LEFT] and x1 > 5:
        x1 -= speed
    if keys_pressed [K_RIGHT] and x1 < 1100:
        x1 += speed
    if keys_pressed [K_UP] and y1 > 5:
        y1 -= speed
    if keys_pressed [K_DOWN] and y1 < 800:
        y1 += speed


    if keys_pressed [K_a] and x2 > 5:
        x2 -= speed
    if keys_pressed [K_d] and x2 < 1100:
        x2 += speed
    if keys_pressed [K_w] and y2 > 5:
        y2 -= speed
    if keys_pressed [K_s] and y2 < 800:
        y2 += speed

    display.update()
