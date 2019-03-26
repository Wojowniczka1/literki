def setup():
    size(400, 400)
    textSize(130)
    textAlign(CENTER)
def draw():
    fill(255, 0, 0)
    text("J", width/2-75, (height/3)*2)
    text("W", width/2+75, (height/3)*2)
    print(mouseX, mouseY)
    print(hex(get(mouseX, mouseY)))
    #print(CODED)
    print(LEFT)
    if keyPressed:
        #print(key)
        print(keyCode)
    
        
        
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.noStroke()
    s.vertex(50, (height/4)*3)
    s.vertex(width/2-20, (height/4)*3+30)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2+20, (height/4)*3-30)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2-30, (height/4)*3+40)
    s.vertex(width/2, (height/4)*3)
    s.vertex(width/2+30, (height/4)*3-40)
    s.vertex(width-50, (height/4)*3)
    s.endShape(CLOSE)
    shape(s, 25, 25)
