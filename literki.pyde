def setup():
    background(253, 170, 90)
    size(400, 400)
    textSize(140)
    textAlign(CENTER)
    
def draw():
    print(mouseX, mouseY)
    print(hex(get(mouseX, mouseY)))
    c = hex(get(mouseX, mouseY))
    if c == "FFFFFFFF":
        text("J", width/2-75, (height/3)*2)
        fill(255, 180, 110)
    else:
        text("J", width/2-75, (height/3)*2)
        fill(100, 200, 150)
    print(LEFT)
    if keyPressed:
        print(key)
        print(keyCode)
    #if c == "FFFFFFFF":
        text("W", width/2+75, (height/3)*2)
        fill(255, 185, 140)
    else:
        text("W", width/2+75, (height/3)*2)
        fill(get(100, 100))

    
    if keyPressed:
        if key == "j":
            if mouseX > 89 and mouseX < 134:
                fill(255, 0, 120)
        if key == "w":
            fill(255, 235, 120)
    if keyPressed == False:
        fill(255, 255, 255)
        
        
    s = createShape()
    s.beginShape()
    s.fill(255, 218, 154)
    s.noStroke()
    s.vertex(50, (height/4)*3)
    s.vertex(width/2-30, (height/4)*3+30)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2-50, (height/4)*3+50)
    s.vertex(width-70, (height/4)*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)
