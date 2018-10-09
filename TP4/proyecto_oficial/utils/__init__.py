from random import randrange

def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256),randrange(256))
