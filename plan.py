import turtle as tu
import shapes as shp

turt = tu.Turtle()
turt.shape("circle")
turt.shapesize(0.5,0.5,0)

drawn_turts = []

def rect(cords_list, t=turt):
    i = 0

    for point in cords_list:
        i += 1

        x = point[0]
        y = point[1]
        
        t.goto(x, y)
        

        if i == 4:
            first = cords_list[0]
            x = first[0]
            y = first[1]
            t.goto(x, y)
    drawn_turts.append(t)

def coord_convertor(st_pnt_x, st_pnt_y, hei, bre) -> int:

    st_pnt_x = int(st_pnt_x)
    st_pnt_y = int(st_pnt_y)
    hei = int(hei)
    bre = int(bre)

    coords = []
    x1 , y1= st_pnt_x , st_pnt_y
    coords.append([x1,y1])
    x2 = st_pnt_x
    y2 = st_pnt_y + hei
    coords.append([x2, y2])
    x3 = st_pnt_x + bre
    y3 = st_pnt_y + hei
    coords.append([x3,y3])
    x4 = st_pnt_x + bre
    y4 = st_pnt_y
    coords.append([x4, y4])

    return coords

def clear():
    for turtles in drawn_turts:
        turtles.clear()
        turtles.ht()

def border(offset, coordsl, t= turt):
    x1, x2, x3, x4 = 0 , 0, 0, 0
    y1, y2, y3, y3 = 0, 0, 0, 0

    offset = int(offset)
    coordsl = list(coordsl)


    i = 0
    offset_coords = []
    for point in coordsl:

        x = point[0]
        y = point[1]
        i += 1
        match i:
            case 1:
                x1 = x - offset
                y1 = y - offset
                offset_coords.append([x1,y1])

            case 2:
                x2 = x - offset
                y2 = y + offset
                offset_coords.append([x2,y2])

            case 3:
                x3 = x + offset
                y3 = y + offset
                offset_coords.append([x3,y3])

            case 4:
                x4 = x + offset
                y4 = y - offset
                offset_coords.append([x4,y4])
    rect(offset_coords, t)

def line(startpointx, startpointy, endpointx, endpointy, t=turt):
    t.pu()
    t.goto(startpointx,startpointy)
    t.pd()
    t.goto(endpointx,endpointy)




q = False
while not q:
    sh = input(

        "What shape do you want to draw? \n" 
        " --Line: L"
        " --Rectangle : R \n" 
        " --Circle: C \n"
        " --clear: CL \n"
        " --quit: Q \n"
        
        
    )

    match sh.lower():
        case "l":
            stpntx = input("What x coordinate do you want the line to start at (number) ->  ")
            stpnty = input("What y coordinate do you want the line to start at (number) ->  ")
            endpntx = input("What x coordinate do you want the line to end at (number) ->  ")
            endpnty = input("What y coordinate do you want the line to end at (number) ->  ")
            stpntx = int(stpntx)
            stpnty = int(stpnty)
            endpntx = int(endpntx)
            endpnty = int(endpnty)
            
            line(stpntx, stpnty, endpntx, endpnty)

        case "r":
            coords = []
            stpntx = input("What x coordinate do you want the drawing to start from (number) ->  ")
            stpnty = input("What y coordinate do you want the drawing to start from (number) ->  ")
            length = input("What length do you want for your rectangle")
            height = input("What height do you want for your rectangle")
            coords = coord_convertor(stpntx, stpnty, height, length)

            stpntx = int(stpntx)
            stpnty = int(stpnty)
            length = int(length)
            height = int(height)

            inp = input("Do you want to add a border? (y/n)")
            if inp == "n":
                print(coords)
                rect(coords)
            elif inp == "y":
                off = input("How much offset do you want?")
                off = int(off)

                border(off, coords, turt)
                rect(coords)

        case "c":
            stpntx = input("What x coordinate do you want the drawing to start from (number) ->  ")
            stpnty = input("What y coordinate do you want the drawing to start from (number) ->  ")

            stpntx = int(stpntx)
            stpnty = int(stpnty)

            turt.goto(stpntx, stpnty)
            inp = input("What diameter do you want for your circle")
            inp = int(inp)
            shp.circle(turt,inp/2)
            drawn_turts.append(turt)

        case "cl":
            inp = input("are you sure you want to clear? (y/n)")
            if inp.lower() == "y":
                clear()
            else:
                continue
        case "q":
            q = True
            break
