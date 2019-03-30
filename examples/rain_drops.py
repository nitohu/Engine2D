import random

from engine2d import *

def generateRainDrops(count = 500):
    drops = []

    for i in range(0, count):
        p0 = [random.randint(0, 600), random.randint(0,600/4)]
        l = Line().fromLists(p0, direction=[0,5])
        drops.append(l)
    
    return drops

def main(): 
    engine = Engine2D()
    background_color = (255, 255, 255)
    # Color of rain drops
    line_color = (0,180,150)
    # Change this variable to change the count of rain drops
    rain_drop_count = 900

    engine.setWindowTitle("Rain Drop Effect")
    engine.fillScreen(background_color)

    # rain_drops = generateRainDrops(rain_drop_count)
    rain_drops = []

    for i in range(0, rain_drop_count):
        p0 = [random.randint(0, 600), random.randint(0,600)]
        l = Line().fromLists(p0, direction=[0,5])
        rain_drops.append(l)

    while True:

        engine.fillScreen(background_color)

        for drop in rain_drops:
            engine.drawLine(drop, line_color)

            drop.p0.y += 3
            drop.p1.y += 3

            if drop.p0.y > 600:
                rain_drops.remove(drop)
            
            lost_rain_drops = rain_drop_count - len(rain_drops)
            print("Lost rain drops: " + str(lost_rain_drops))

            if(lost_rain_drops > 10):
                print("Generate new drops")
                rain_drops += generateRainDrops(lost_rain_drops)

        engine.update()

main()