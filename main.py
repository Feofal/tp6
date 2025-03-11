import arcade
from enum import Enum
import game_state
import random
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Mahna Mahna Do doo be-do-do"
class RPCGAME(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LICORICE)
        self.player_point = 0
        self.ai_point = 0
        self.ai_face = arcade.Sprite("assets/compy.png", 1.5, SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/2 + 20)
        self.player_face = arcade.Sprite("assets/faceBeard.png", 0.3, SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 + 20)
        self.rock = arcade.Sprite("assets/srock.png", 0.5, SCREEN_WIDTH/2 - 350, SCREEN_HEIGHT/2 - 80)
        self.paper = arcade.Sprite("assets/spaper.png", 0.5, SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 - 80)
        self.cissors = arcade.Sprite("assets/scissors.png", 0.5, SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 80)
        self.ai_rock = arcade.Sprite("assets/srock.png", 0.5, SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT / 2 - 80)
        self.ai_paper = arcade.Sprite("assets/spaper.png", 0.5, SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT / 2 - 80)
        self.ai_cissors = arcade.Sprite("assets/scissors.png", 0.5, SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT / 2 - 80)
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
        self.player_attack = 3
        self.ai_attack = None
        self.attack_list = {
            0: "rock",
            1: "paper",
            2: "cissors",
            3: "choice not made"
        }
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
        player_text = arcade.Text(f"Vous avez {self.player_point} points",
                                  SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/10, arcade.color.LIBERTY,
                                  20, bold= True, anchor_x= "center")
        ai_text = arcade.Text(f"L'ia a {self.ai_point} points",
                              SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/10,
                              arcade.color.LIBERTY, 20,
                              bold= True, anchor_x= "center")
        self.victory_text = arcade.Text("VICTOIRE", SCREEN_WIDTH/2, SCREEN_HEIGHT - 200, arcade.color.GOLD, 50, bold= True, anchor_x= "center")
        self.loose_text = arcade.Text("DÉFAITE", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200, arcade.color.RED_DEVIL, 50,
                                        bold=True, anchor_x="center")
        self.retry_text = arcade.Text("Appuyer sur ÉSPACE pour recommencer", SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250, arcade.color.LIGHT_BLUE, 20,
                                        bold=True, anchor_x="center")
        game_title.draw()
        if self.state == game_state.GameState.GAME_OVER:
            if self.player_point == 3:
                self.victory_text.draw()
            else:
                self.loose_text.draw()
            self.retry_text.draw()
        else:
            game_subtitle.draw()
        player_text.draw()
        ai_text.draw()

        for i in range(0,3):
            arcade.draw_circle_outline(SCREEN_WIDTH/2 - 150 - i*100, SCREEN_HEIGHT/2 - 85, 60, arcade.color.ROYAL_AZURE, tilt_angle= 45, num_segments= 4)
        arcade.draw_circle_outline(SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT / 2 - 85, 55,
                                   arcade.color.ROYAL_AZURE, tilt_angle=45, num_segments=4)
        self.players_list.draw()
        self.rock_list.draw()
        self.paper_list.draw()
        self.cissors_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if self.state == game_state.GameState.NOT_STARTED or self.state == game_state.GameState.GAME_OVER and arcade.key.SPACE:
            self.state = game_state.GameState.ROUND_ACTIVE
            self.player_point = 0
            self.ai_point = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if (self.rock.collides_with_point((x,y))
            or self.paper.collides_with_point((x,y))
                or self.cissors.collides_with_point((x,y))):
            if self.state == game_state.GameState.ROUND_DONE:
                self.state = game_state.GameState.ROUND_ACTIVE
            if self.rock.collides_with_point((x,y)):
                self.player_attack = 0
            elif self.paper.collides_with_point((x,y)):
                self.player_attack = 1
                print(self.player_attack)
            elif self.cissors.collides_with_point((x,y)):
                self.player_attack = 2
                print(self.player_attack)


    def on_update(self, delta_time: float):
        if self.player_point == 3 or self.ai_point == 3:
            self.state = game_state.GameState.GAME_OVER
        self.ai_attack = random.randint(0,2)
        if self.state == game_state.GameState.ROUND_ACTIVE and self.attack_list[self.player_attack] != "choice not made":
            self.both_attack = [self.attack_list[self.player_attack], self.attack_list[self.ai_attack]]
            match self.both_attack:
                case ["rock", "cissors"]:
                    self.player_point += 1
                case ["paper", "rock"]:
                    self.player_point += 1
                case ["cissors", "paper"]:
                    self.player_point += 1
                case ["cissors", "rock"]:
                    self.ai_point += 1
                case ["rock", "paper"]:
                    self.ai_point += 1
                case ["paper", "cissors"]:
                    self.ai_point += 1
                case _:
                    pass
            if self.ai_rock in self.rock_list:
                self.rock_list.remove(self.ai_rock)
            elif self.ai_paper in self.paper_list:
                self.paper_list.remove(self.ai_paper)
            elif self.ai_cissors in self.cissors_list:
                self.cissors_list.remove(self.ai_cissors)

            match self.attack_list[self.ai_attack]:
                case "rock":
                    self.rock_list.append(self.ai_rock)
                case "paper":
                    self.paper_list.append(self.ai_paper)
                case "cissors":
                    self.cissors_list.append(self.ai_cissors)
            self.state = game_state.GameState.ROUND_DONE
def main():
    rpc = RPCGAME(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
