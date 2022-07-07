# function of GUI

# set new scrreen and change to one of them
def changeScreen(screenManager, newscreen = None, currentScreen = None):
    if newscreen:
        screenManager.add_widget(newscreen)
    if currentScreen:
        screenManager.current = currentScreen