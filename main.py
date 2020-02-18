import pyglet

win= pyglet.window.Window()

# Create a sprite so the game can keep track of coordinates
img= pyglet.image.load('assets/gfx/Old hero.png')
smol_img = img.get_region(x = 72, y = 130, width = 24, height = 25)
spr = pyglet.sprite.Sprite(smol_img, x = 200, y = 200)


# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys)             # update the keys object
    if keys[pyglet.window.key.LEFT]: # if the key is pressed...
        spr.x -= 5                             # change spr.x by -1
    if keys[pyglet.window.key.RIGHT]:
        spr.x += 5
    if keys[pyglet.window.key.UP]:
        spr.y += 5
    if keys[pyglet.window.key.DOWN]:
        spr.y -= 5

@win.event
def on_draw():
    win.clear()
    spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()