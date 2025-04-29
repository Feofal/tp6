"""
    Nom: Gabriel Foriel Fusier
    Groupe: 401
    Description: Un jeu de roche, papier, ciseaux
    
"""

from game_state import GameState
from attack_animation import *
import random
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
SCREEN_TITLE = "RPC"


class RPC(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LICORICE)
        self.player_point = 0
        self.ai_point = 0
        self.ai_face = arcade.Sprite("assets/compy.png", 1.5,
                                     SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/2 + 20)
        self.player_face = arcade.Sprite("assets/faceBeard.png", 0.3,
                                         SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/2 + 20)
        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock.center_x = SCREEN_WIDTH/2 - 350
        self.rock.center_y = SCREEN_HEIGHT/2 - 80
        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.center_x = SCREEN_WIDTH/2 - 250
        self.paper.center_y = SCREEN_HEIGHT/2 - 80
        self.cissors = AttackAnimation(AttackType.CISSORS)
        self.cissors.center_x = SCREEN_WIDTH / 2 - 150
        self.cissors.center_y = SCREEN_HEIGHT / 2 - 80
        self.ai_rock = AttackAnimation(AttackType.ROCK)
        self.ai_rock.center_x = SCREEN_WIDTH / 2 + 250
        self.ai_rock.center_y = SCREEN_HEIGHT / 2 - 80
        self.ai_paper = AttackAnimation(AttackType.PAPER)
        self.ai_paper.center_x = SCREEN_WIDTH / 2 + 250
        self.ai_paper.center_y = SCREEN_HEIGHT / 2 - 80
        self.ai_cissors = AttackAnimation(AttackType.CISSORS)
        self.ai_cissors.center_x = SCREEN_WIDTH / 2 + 250
        self.ai_cissors.center_y = SCREEN_HEIGHT / 2 - 80
        self.players_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()
        self.paper_list = arcade.SpriteList()
        self.cissors_list = arcade.SpriteList()
        self.players_list.append(self.ai_face)
        self.players_list.append(self.player_face)
        self.rock_list.append(self.rock)
        self.paper_list.append(self.paper)
        self.cissors_list.append(self.cissors)
        self.state = GameState.NOT_STARTED
        self.player_attack = 3
        self.ai_attack = None
        self.both_attack = None
        self.point_color = [arcade.color.LIBERTY, arcade.color.BLUE_VIOLET,
                            arcade.color.RAZZLE_DAZZLE_ROSE,
                            arcade.color.GOLD]
        self.subtitle = "Appuyez sur ESPACE pour commencer"
        self.round_subtitle = ""
        self.round_color = arcade.color.LICORICE
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
                                 arcade.color.ROYAL_YELLOW, 50, bold=True,
                                 anchor_x="center")
        game_subtitle = arcade.Text(self.subtitle,
                                    SCREEN_WIDTH/2, SCREEN_HEIGHT - 150,
                                    arcade.color.LIGHT_BLUE, 25,
                                    bold=True, anchor_x="center")
        player_text = arcade.Text(f"Vous avez {self.player_point} points",
                                  SCREEN_WIDTH/2 - 250, SCREEN_HEIGHT/10, self.point_color[self.player_point],
                                  20, bold=True, anchor_x="center")
        ai_text = arcade.Text(f"L'ia a {self.ai_point} points",
                              SCREEN_WIDTH/2 + 250, SCREEN_HEIGHT/10,
                              self.point_color[self.ai_point], 20,
                              bold=True, anchor_x="center")
        round_winner_text = arcade.Text(self.round_subtitle,
                                        SCREEN_WIDTH/2, SCREEN_HEIGHT - 200,
                                        self.round_color, 25,
                                        bold=True, anchor_x="center")
        victory_text = arcade.Text("VICTOIRE",
                                   SCREEN_WIDTH/2, SCREEN_HEIGHT - 200,
                                   arcade.color.GOLD, 50,
                                   bold=True, anchor_x="center")
        loose_text = arcade.Text("DÉFAITE",
                                 SCREEN_WIDTH / 2, SCREEN_HEIGHT - 200,
                                 arcade.color.RED_DEVIL, 50,
                                 bold=True, anchor_x="center")
        retry_text = arcade.Text("Appuyer sur ESPACE pour recommencer",
                                 SCREEN_WIDTH / 2, SCREEN_HEIGHT - 250,
                                 arcade.color.LIGHT_BLUE, 20,
                                 bold=True, anchor_x="center")
        for i in range(0, 3):
            arcade.draw_circle_outline(SCREEN_WIDTH/2 - 150 - i*100,
                                       SCREEN_HEIGHT/2 - 85, 60,
                                       arcade.color.ROYAL_AZURE,
                                       tilt_angle=45, num_segments=4)
        arcade.draw_circle_outline(SCREEN_WIDTH / 2 + 250, SCREEN_HEIGHT / 2 - 85,
                                   55, arcade.color.ROYAL_AZURE,
                                   tilt_angle=45, num_segments=4)

        if self.state == GameState.GAME_OVER:
            if self.player_point == 3:
                victory_text.draw()
            else:
                loose_text.draw()
            retry_text.draw()
        else:
            game_subtitle.draw()
            round_winner_text.draw()
        player_text.draw()
        ai_text.draw()
        game_title.draw()
        self.players_list.draw()
        self.rock_list.draw()
        self.paper_list.draw()
        self.cissors_list.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if self.state == GameState.NOT_STARTED or self.state == GameState.GAME_OVER and arcade.key.SPACE:
            self.subtitle = "Appuyer sur une image pour faire une attaque!"
            self.state = GameState.ROUND_ACTIVE
            self.player_point = 0
            self.ai_point = 0
            self.player_attack = 3
            self.round_subtitle = ""
        elif self.state == GameState.ROUND_DONE and arcade.key.SPACE:
            self.subtitle = "Appuyer sur une image pour faire une attaque!"
            self.round_subtitle = ""
            self.state = GameState.ROUND_ACTIVE
            self.player_attack = 3
        if self.ai_rock in self.rock_list:
            self.rock_list.remove(self.ai_rock)
        elif self.ai_paper in self.paper_list:
            self.paper_list.remove(self.ai_paper)
        elif self.ai_cissors in self.cissors_list:
            self.cissors_list.remove(self.ai_cissors)
        if self.rock not in self.rock_list:
            self.rock_list.append(self.rock)
        if self.paper not in self.paper_list:
            self.paper_list.append(self.paper)
        if self.cissors not in self.cissors_list:
            self.cissors_list.append(self.cissors)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.rock.collides_with_point((x, y)):
            self.player_attack = 0
        elif self.paper.collides_with_point((x, y)):
            self.player_attack = 1
        elif self.cissors.collides_with_point((x, y)):
            self.player_attack = 2

    def on_update(self, delta_time: float):
        if not self.state == GameState.GAME_OVER:
            self.rock.on_update()
            self.paper.on_update()
            self.cissors.on_update()
            self.ai_rock.on_update()
            self.ai_paper.on_update()
            self.ai_cissors.on_update()
        if self.player_point == 3 or self.ai_point == 3:
            self.state = GameState.GAME_OVER
        self.ai_attack = random.randint(0, 2)
        if self.state == GameState.ROUND_ACTIVE and self.attack_list[self.player_attack] != "choice not made":
            self.both_attack = [self.attack_list[self.player_attack], self.attack_list[self.ai_attack]]
            match self.both_attack:
                case ["rock", "cissors"]:
                    self.player_point += 1
                    self.round_subtitle = "Vous avez gagné la manche"
                    self.round_color = arcade.color.CHARTREUSE
                case ["paper", "rock"]:
                    self.player_point += 1
                    self.round_subtitle = "Vous avez gagné la manche"
                    self.round_color = arcade.color.CHARTREUSE
                case ["cissors", "paper"]:
                    self.player_point += 1
                    self.round_subtitle = "Vous avez gagné la manche"
                    self.round_color = arcade.color.CHARTREUSE
                case ["cissors", "rock"]:
                    self.ai_point += 1
                    self.round_subtitle = "L'ia a gagné la manche"
                    self.round_color = arcade.color.ELECTRIC_CRIMSON
                case ["rock", "paper"]:
                    self.ai_point += 1
                    self.round_subtitle = "L'ia a gagné la manche"
                    self.round_color = arcade.color.ELECTRIC_CRIMSON
                case ["paper", "cissors"]:
                    self.ai_point += 1
                    self.round_subtitle = "L'ia a gagné la manche"
                    self.round_color = arcade.color.ELECTRIC_CRIMSON
                case _:
                    self.round_subtitle = "Égalité"
                    self.round_color = arcade.color.WHITE
            match self.attack_list[self.ai_attack]:
                case "rock":
                    self.rock_list.append(self.ai_rock)
                case "paper":
                    self.paper_list.append(self.ai_paper)
                case "cissors":
                    self.cissors_list.append(self.ai_cissors)
            match self.attack_list[self.player_attack]:
                case "rock":
                    self.paper_list.remove(self.paper)
                    self.cissors_list.remove(self.cissors)
                case "paper":
                    self.rock_list.remove(self.rock)
                    self.cissors_list.remove(self.cissors)
                case "cissors":
                    self.rock_list.remove(self.rock)
                    self.paper_list.remove(self.paper)
            self.subtitle = "Appuyez sur ESPACE pour continuer"
            self.state = GameState.ROUND_DONE


def main():
    RPC(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
    
