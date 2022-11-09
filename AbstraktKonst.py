# --Abstrakt konst - Inlämningsuppgift--
# Adam O, NA20, VT21

import random as r
import turtle as t

t.speed(0)
t.colormode(255)
t.tracer(0)
t.pu()
t.ht()

def farg():
    """Slumpar färg och tjocklek"""
    
    #Pennans färg:
    pr = r.randrange(256)
    pg = r.randrange(256)
    pb = r.randrange(256)
    t.pencolor(pr,pg,pb)
    
    #Fyllningsfärg
    fr = r.randrange(256)
    fg = r.randrange(256)
    fb = r.randrange(256)
    t.fillcolor(fr,fg,fb)
    
    tjocklek = r.randrange(6)
    t.pensize(tjocklek)
    
def fyrH(fylld, X, Y, maxX, maxY):
    """Ritar en fyrhörning"""
    
    maxSt = 200 #Max storlek
    
    #Slumpar fyra punkter som ska bli hörnen. T.ex. Punkt nr 0 är (px[0], py[0]).
    #Varje punkt kan bara vara inom ett område. Till exempel punkt 0 kan bara vara ovanför och till höger om klicket.
    #Jag gör så här för att figurerna ska få slumpade kanter och vinklar.
    px = [0, 0, 0, 0]
    px[0] = r.randrange(X, X+maxSt+1)
    px[1] = r.randrange(X, X+maxSt+1)
    px[2] = r.randrange(X-maxSt, X)
    px[3] = r.randrange(X-maxSt, X)
    py = [0, 0, 0, 0]
    py[0] = r.randrange(Y, Y+maxSt+1)
    py[1] = r.randrange(Y-maxSt, Y)
    py[2] = r.randrange(Y-maxSt, Y)
    py[3] = r.randrange(Y, Y+maxSt+1)
    
    #Kollar om punkterna behöver flyttas i x och/eller i y för att
    #inte ritas utanför kanten.
    #flyttaX är hur många steg figuren ska flyttas i x.
    flyttaX = 0
    for i in px:
        if i > maxX and maxX - i < flyttaX:
            flyttaX = maxX - i
        elif i < -maxX and -maxX - i > flyttaX:
            flyttaX = -maxX - i
    flyttaY = 0
    for i in py:
        if i > maxY and maxY - i < flyttaY:
            flyttaY = maxY - i
        elif i < -maxY and -maxY - i > flyttaY:
            flyttaY = -maxY - i 
    
    if fylld:
        t.begin_fill()
    
    #Rita:
    t.goto(px[0] + flyttaX, py[0] + flyttaY)
    t.pd()
    for i in range(3, -1, -1):
        t.goto(px[i] + flyttaX, py[i] + flyttaY)
    t.end_fill()
    t.pu()

def triangel(fylld, X, Y, maxX, maxY):
    """Ritar en triangel"""
    
    maxSt = 200 #Max storlek
    
    #Slumpar punkter för varje hörn på samma sätt som i fyrH-funktionen.
    px = [0, 0, 0]
    px[0] = r.randrange(X-maxSt/2, X+maxSt/2+1)
    px[1] = r.randrange(X, X+maxSt+1)
    px[2] = r.randrange(X-maxSt, X)
    py = [0, 0, 0]
    py[0] = r.randrange(Y, Y+maxSt+1)
    py[1] = r.randrange(Y-maxSt, Y)
    py[2] = r.randrange(Y-maxSt, Y)
    
    #Kollar om punkterna behöver flyttas i x (flyttaX) och/eller i y (flyttaY) för att
    #inte ritas utanför kanten.
    flyttaX = 0
    for i in px:
        if i > maxX and maxX - i < flyttaX:
            flyttaX = maxX - i
        elif i < -maxX and -maxX - i > flyttaX:
            flyttaX = -maxX - i
    flyttaY = 0
    for i in py:
        if i > maxY and maxY - i < flyttaY:
            flyttaY = maxY - i
        elif i < -maxY and -maxY - i > flyttaY:
            flyttaY = -maxY - i    
        
    if fylld:
        t.begin_fill()
        
    #Rita
    t.goto(px[0] + flyttaX, py[0] + flyttaY)
    t.pd()
    for i in range(2, -1, -1):
        t.goto(px[i] + flyttaX, py[i] + flyttaY)
    t.end_fill()
    t.pu()
    
def cirkel(fylld, X, Y, maxX, maxY):
    """Ritar en cirkel"""
    maxSt = 200 #>10
    
    radie = r.randrange(10, maxSt)
    
    #Kollar om punkterna behöver flyttas i x (flyttaX) och/eller i y (flyttaY) för att
    #inte ritas utanför kanten.
    flyttaX = 0
    if X + radie > maxX:
        flyttaX =  maxX - (X + radie)
    elif X - radie < -maxX:
        flyttaX = -maxX - (X - radie)
    flyttaY = 0
    if Y + radie > maxY:
        flyttaY =  maxY - (Y + radie)
    elif Y - radie < -maxY:
        flyttaY = -maxY - (Y - radie)
        
    #Går till rätt punkt och backar så att klicket blev i mitten av cirkeln:
    t.goto(X + flyttaX, Y + flyttaY)
    t.lt(90)
    t.bk(radie)
    t.rt(90)
    
    if fylld:
        t.begin_fill()
        
    #Rita
    t.pd()
    t.circle(radie)
    t.pu()
    
    t.end_fill()

def rita(x, y):
    """Väljer vilken figur som ska ritas"""
    #Alla figurernas funktioner finns i listan "figurer".
    #Om man vill lägga till en ny figur behöver man bara lägga till den funktionen i listan här.
    #Just nu finns det ingen funktion för streck men det skulle vara ganska lätt att lägga till om man vill.
    figurer = [fyrH, triangel, cirkel]
    farg()
    #Slumpar om figuren ska vara fylld (True) eller inte (False). Sannolikheten är 50% för båda.
    fylld = r.random() < 0.5
    #Programmet fungerar med olika storlekar på fönstret.
    #Man kan ändra variabeln maxSt för att ändra storleken för varje figur om de är för små.
    #Kanterna på fönstret.
    maxX, maxY = t.window_width()/2 - 10, t.window_height()/2 - 10
    #Väljer och anropar en funktion ur listan.
    r.choice(figurer)(fylld, x, y, maxX, maxY)
    t.update()


t.onscreenclick(rita)
t.done()