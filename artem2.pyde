I=20
def setup():
    size(500,500)
    background(255)
def draw():
    global I
    push()
    fill(0,0,0)
    stroke(0)
    strokeWeight(2)
    fill(255,0,0)
    rect(0,0,50,50)
    fill(255,158,0)
    rect(50,0,50,50)
    fill(255,243,0)
    rect(100,0,50,50)
    fill(0,255,40)
    rect(150,0,50,50)
    fill(0,244,255)
    rect(200,0,50,50)
    fill(0,0,255)
    rect(250,0,50,50)
    fill(207,0,255)
    rect(300,0,50,50)
    fill(0,0,0)
    rect(350,0,50,50)
    fill(255)
    rect(450,0,50,50)
    pop()

    strokeWeight(I)
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
        if mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50:
            stroke(255,0,0)
        if mouseX<100 and mouseX>50 and mouseY>0 and mouseY<50:
            stroke(255,158,0)
        if mouseX<150 and mouseX>100 and mouseY>0 and mouseY<50:
            stroke(255,243,0)
        if mouseX<200 and mouseX>150 and mouseY>0 and mouseY<50:
            stroke(0,255,40)
        if mouseX<250 and mouseX>200 and mouseY>0 and mouseY<50:
            stroke(0,244,255)
        if mouseX<300 and mouseX>250 and mouseY>0 and mouseY<50:
            stroke(0,0,255)
        if mouseX<350 and mouseX>300 and mouseY>0 and mouseY<50:
            stroke(207,0,255)
        if mouseX<500 and mouseX>450 and mouseY>0 and mouseY<50:
            stroke(255)

            
            
            
def keyPressed():
    global I
    if key=='1':
        stroke(255,0,0)
    if key=='2':
        stroke(255,158,0)
    if key=='3':
        stroke(255,243,0)
    if key=='4':
        stroke(0,255,40)
    if key=='5':
        stroke(0,244,255)
    if key=='6':
        stroke(0,0,255)
    if key=='7':
        stroke(207,0,255)
    if key=='8':
        stroke(0,0,0)
    if key=='a':
        I=I+1
    if key=='d' and I>0:
        I=I-1            
            
             
            
            
            
