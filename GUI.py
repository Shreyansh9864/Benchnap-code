from taipy import Gui

# Setting up the GUI
title = "# This is my page title"
page = '''<|{title}|>'''
if __name__ == '__main__' :
    Gui(page=title).run(use_reloader=True)
