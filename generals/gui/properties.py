from dataclasses import dataclass
from typing import Any, Literal

from pygame.time import Clock

from generals.core import config as c
from generals.core.game import Game


@dataclass
class Properties:
    __game: Game
    __agent_data: dict[str, dict[str, Any]]
    __mode: Literal["train", "game", "replay"]
    __game_speed: int = 1
    __clock: Clock = Clock()

    def __post_init__(self):
        self.__grid_height: int = self.__game.grid_dims[0]
        self.__grid_width: int = self.__game.grid_dims[1]
        self.__display_grid_width: int = c.SQUARE_SIZE * self.grid_width
        self.__display_grid_height: int = c.SQUARE_SIZE * self.grid_height
        self.__right_panel_width: int = 4 * c.GUI_CELL_WIDTH

        self.__paused: bool = False

        self.__agent_fov: dict[str, bool] = {
            name: True for name in self.agent_data.keys()
        }

    @property
    def game(self):
        return self.__game

    @property
    def agent_data(self):
        return self.__agent_data

    @property
    def mode(self):
        return self.__mode

    @property
    def paused(self):
        return self.__paused

    @paused.setter
    def paused(self, value: bool):
        self.__paused = value

    @property
    def game_speed(self):
        return self.__game_speed

    @game_speed.setter
    def game_speed(self, value: float):
        new_speed = min(32.0, max(0.25, value))  # clip speed
        self.__game_speed = new_speed

    @property
    def clock(self):
        return self.__clock

    @property
    def agent_fov(self):
        return self.__agent_fov

    @property
    def grid_height(self):
        return self.__grid_height

    @property
    def grid_width(self):
        return self.__grid_width

    @property
    def display_grid_width(self):
        return self.__display_grid_width

    @property
    def display_grid_height(self):
        return self.__display_grid_height

    @property
    def right_panel_width(self):
        return self.__right_panel_width

    def update_speed(self, change: float) -> None:
        """change: multiplier how much to change, usually 2.0 or 0.5"""
        new_speed = self.game_speed * change
        self.game_speed = new_speed
