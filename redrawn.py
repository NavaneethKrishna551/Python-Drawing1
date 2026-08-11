import pygame as pg

# pygame setup
pg.init()
screen = pg.display.set_mode((500, 500))
clock = pg.time.Clock()
screen.fill("black")
surface = pg.Surface(size=(500,500))

running = True

mouse_pressed = False
times_pressed = 0
mousestate = None

mouse_second_x = None
mouse_second_y = None
mouse_x = None
mouse_y =None

white = (255,255,255)

l_key_pressed = False
s_key_pressed = False


draw_line = False

right_mouse_pressed = (False,False,True)
middle_mouse_pressed = (False, True, False)
left_mouse_pressed = (True, False, False)
mouse_pressed_counter = 0


drawings = []


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mousestate = pg.mouse.get_pressed(3)
            mouse_pressed = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_l:
                l_key_pressed = True
            elif event.key == pg.K_s:
                s_key_pressed = True

    # fill the screen with a color to wipe away anything from last frame
    

    # RENDER YOUR GAME HERE
    

    #drawing a line

    if l_key_pressed and mousestate == right_mouse_pressed:
        mouse_pressed_counter += 1
        print("right button has been pressed")
        mouse_pos = pg.mouse.get_pos()
        
        if mouse_pressed_counter == 1:
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            print(mouse_x, mouse_y, mouse_second_x, mouse_second_y)
        if mouse_pressed_counter == 2:
            mouse_second_x = mouse_pos[0]
            mouse_second_y = mouse_pos[1]
            print(mouse_x, mouse_y, mouse_second_x, mouse_second_y)
            line = pg.draw.line(surface, white,(mouse_x, mouse_y), (mouse_second_x, mouse_second_y) )
            drawings.append(line)
            
        
    if s_key_pressed and mousestate == right_mouse_pressed:
        mouse_pressed_counter +=1
        print("right button has been pressed")
        mouse_pos = pg.mouse.get_pos()

        if mouse_pressed_counter == 1:
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
            print(mouse_x, mouse_y, mouse_second_x, mouse_second_y)

        if mouse_pressed_counter == 2:
            mouse_second_x = mouse_pos[0]
            mouse_second_y = mouse_pos[1]

            width = mouse_second_x - mouse_x

            print(mouse_x, mouse_y, mouse_second_x, mouse_second_y)
            rect = pg.draw.rect(surface, white, [mouse_x,mouse_y, width, width]) # rectangle with same width and height is a square
            
            drawings.append(rect)




    # flip() the display to put your work on screen
    
    pg.display.flip()
    screen.blit(surface, (0,0))
    clock.tick(60)  # limits FPS to 60

    if mouse_pressed_counter == 2:
        l_key_pressed = False
        s_key_pressed = False
        mouse_pressed_counter = 0
        mouse_x = None
        mouse_second_x = None
        mouse_y = None
        mouse_second_y = None   


    mouse_pressed = False
    mousestate = None

pg.quit()