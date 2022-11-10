import pygame as pg
 
# SETUP
pg.init()

display = (800, 600)
screen = pg.display.set_mode(display)
pg.display.set_caption("Tank Domination")

tick = pg.time.Clock()

tank_svg = pg.image.load("4_gamedev/tank.svg")
tank_sprite = pg.transform.scale(tank_svg, (75, 75))

config = {
    "sky": {
        "color": (105, 176, 245),
    },
    "grass": {
        "color": (100, 225, 50),
        "pos": {
            "x": 0,
            "y": 0.8 * display[1]
        }
    },
    "player": {
        "pos": (0.2 * display[0], 0.8 * display[1] - 75),
        "hp": 100
    },
    "cpu": {
        "pos": (0.8 * display[0] - tank_sprite.get_width(), 0.8 * display[1] - 75),
        "hp": 100
    }
}

# GAME LOOP
while True:
    # Check fo exit event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    # Movement
    
    # Tuples don't allow this :(
    if keys[pg.K_LEFT]:
        config["player"]["pos"][0] -= 5
    if keys[pg.K_RIGHT]:
        config["player"]["pos"][0] += 5

    print(config["player"]["pos"])

    # Draw background
    screen.fill(config["sky"]["color"])

    # Grass
    pg.draw.rect(screen, config["grass"]["color"], pg.Rect(config["grass"]["pos"]["x"], config["grass"]["pos"]["y"], display[0], display[1] * 0.2))
 
    # Draw tanks
    player_tank = tank_sprite
    screen.blit(tank_sprite, config["player"]["pos"])

    cpu_tank = tank_sprite
    cpu_tank = pg.transform.flip(cpu_tank, True, False)
    screen.blit(cpu_tank, config["cpu"]["pos"])

    pg.display.update()
    tick.tick(120)