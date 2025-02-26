import arcade
import enum
import game_state
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Mahna Mahna Do doo be-do-do"

class RPCGAME(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LICORICE)
        self.player_point = 0
        self.ai_point = 0
        self.turn_square = 0
        self.ai_face = arcade.Sprite("assets/compy.png", 1.5, SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/2 + 20)
        self.player_face = arcade.Sprite("assets/faceBeard.png", 0.3, SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 + 20)
        self.rock = arcade.Sprite("assets/srock.png", 0.5, SCREEN_WIDTH/2 - 350, SCREEN_HEIGHT/2 - 80)
        self.paper = arcade.Sprite("assets/spaper.png", 0.5, SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 80)
        self.cissors = arcade.Sprite("assets/scissors.png", 0.5, SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 80)
        self.players_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.paper_list = arcade.SpriteList()
        self.cissors_list = arcade.SpriteList()
        self.players_list.append(self.ai_face)
        self.players_list.append(self.player_face)
        self.rock_list.append(self.rock)
        self.paper_list.append(self.paper)
        self.cissors_list.append(self.cissors)
        self.state = game_state.GameState.NOT_STARTED
    def on_draw(self):
        self.clear()
        self.turn_square += 5
        if self.turn_square == 90:
            self.turn_square = 0
        game_title = arcade.Text("Roche - Papier - Ciseau",
                                 SCREEN_WIDTH/2, SCREEN_HEIGHT - 100,
                                 arcade.color.ROYAL_YELLOW, 50, bold= True,
                                 anchor_x= "center")
        game_subtitle = arcade.Text("Appuyer sur une image pour faire une attaque!",
                                    SCREEN_WIDTH/2, SCREEN_HEIGHT - 150,
                                    arcade.color.LIGHT_BLUE, 25,
                                    bold= True, anchor_x= "center")
        player_text = arcade.Text(f"Vous avez {self.player_point} points",
                                  SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/10, arcade.color.LIBERTY,
                                  20, bold= True, anchor_x= "center")
        ai_text = arcade.Text(f"L'ia a {self.ai_point} points",
                              SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/10,
                              arcade.color.LIBERTY, 20,
                              bold= True, anchor_x= "center")
        game_title.draw()
        game_subtitle.draw()
        player_text.draw()
        ai_text.draw()

        for i in range(0,3):
            arcade.draw_circle_outline(SCREEN_WIDTH/2 - 160 - i*100, SCREEN_HEIGHT/2 - 85, 60, arcade.color.ROYAL_AZURE, tilt_angle= self.turn_square, num_segments= 4)
        arcade.draw_circle_outline(SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT / 2 - 85, 55,
                                   arcade.color.ROYAL_AZURE, tilt_angle=self.turn_square, num_segments=4)
        self.players_list.draw()
        self.rock_list.draw()
        self.paper_list.draw()
        self.cissors_list.draw()
    def do_attack(self):
        print('I am sexy and I know it')
    def on_key_press(self, symbol: int, modifiers: int):
        if self.state == game_state.GameState.NOT_STARTED or self.state == game_state.GameState.GAME_OVER and arcade.key.SPACE:
            self.do_attack()

def main():
    rpc = RPCGAME(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
