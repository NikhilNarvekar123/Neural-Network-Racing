import pygame as pyg


class MainGame:

        def __init__(self):
            print('starting game...')

        def run_game(self):
            pyg.init()
            game_window = pyg.display.set_mode((800,600))
            pyg.display.set_caption('NN Racing')

            car_crash = False
            while not car_crash:
                for event in pyg.event.get():
                    if event.type == pyg.QUIT:
                        car_crash
                pyg.display.update()

            pyg.quit()
            quit()



m = MainGame()
m.run_game()