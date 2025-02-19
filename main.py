import arcade

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Mahna Mahna Do doo be-do-do"

class RPCGAME(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LICORICE)
    def on_draw(self):
        self.clear()
        game_title = arcade.Text("Roche - Papier - Ciseau",
                                 SCREEN_WIDTH/2, SCREEN_HEIGHT - 100,
                                 arcade.color.ROYAL_YELLOW, 50, bold= True,
                                 anchor_x= "center")
        game_subtitle = arcade.Text("Appuyer sur une image pour faire une attaque!",
                                    SCREEN_WIDTH/2, SCREEN_HEIGHT - 150,
                                    arcade.color.LIGHT_BLUE, 25,
                                    bold= True, anchor_x= "center")
        player_text = arcade.Text("Vous avez   points", SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/10, arcade.color.LIBERTY, 20, bold= True, anchor_x= "center")
        game_title.draw()
        game_subtitle.draw()
        player_text.draw()
def main():
    rpc = RPCGAME(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.run()

if __name__ == "__main__":
    main()
