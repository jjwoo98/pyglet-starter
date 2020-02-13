import pyglet # import the library
win = pyglet.window.Window() # create the window

# Load the image
img = pyglet.image.load('assets/hero/Old hero.png')

# spr = pyglet.sprite.Sprite(img, x=50, y=50)

# Start the event loop
def update(dt):
  pass

@win.event
def on_draw():
    win.clear()
    img.blit(200, 100)
    # spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()




