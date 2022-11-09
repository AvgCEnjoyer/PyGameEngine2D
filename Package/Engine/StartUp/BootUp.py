from pygame import display


def bootUp(width : int , height : int) -> dict:

    window = getWindow(width, height)

    return {"window" : window}


def getWindow(width : int, height : int) -> display:

    return display.set_mode([width, height])

def getUserOptions():

    pass