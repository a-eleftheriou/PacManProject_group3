import pytest
import pygame
from game_board import GameBoard
from item import Pellet, PowerPellet


@pytest.fixture
def game_board():
    return GameBoard()


@pytest.fixture
def walls():
    return [
        pygame.Rect(0, 0, 20, 600),  # Left wall
        pygame.Rect(200, 200, 20, 20),  # Small obstacle
        pygame.Rect(780, 0, 20, 600),  # Right wall
    ]


def test_game_board_initialization(game_board):
    # check that the default values are set correctly.
    assert game_board.width == 800
    assert game_board.height == 600
    # since we don't set 'values,' check the list has been created.
    assert isinstance(game_board.walls, list)
    assert isinstance(game_board.pellets, list)
    assert isinstance(game_board.power_pellets, list)


def test_walls(game_board):
    # check outer walls first.
    # top wall.
    assert any(
        wall.x == 0
        and wall.y == 0
        and wall.width == game_board.width
        and wall.height == 20
        for wall in game_board.walls
    )
    # left wall.
    assert any(
        wall.x == 0
        and wall.y == 0
        and wall.width == 20
        and wall.height == game_board.height
        for wall in game_board.walls
    )
    # bottom wall.
    assert any(
        wall.x == 0
        and wall.y == game_board.height - 20
        and wall.width == game_board.width
        and wall.height == 20
        for wall in game_board.walls
    )
    # right wall.
    assert any(
        wall.x == game_board.width - 20
        and wall.y == 0
        and wall.width == 20
        and wall.height == game_board.height
        for wall in game_board.walls
    )

    # check inner walls.
    assert any(
        wall.x == 100 and wall.y == 100 and wall.width == 20 and wall.height == 200
        for wall in game_board.walls
    )
    assert any(
        wall.x == 300 and wall.y == 100 and wall.width == 200 and wall.height == 20
        for wall in game_board.walls
    )
    assert any(
        wall.x == 600 and wall.y == 100 and wall.width == 20 and wall.height == 400
        for wall in game_board.walls
    )
    assert any(
        wall.x == 300 and wall.y == 350 and wall.width == 200 and wall.height == 20
        for wall in game_board.walls
    )


def test_pellets(game_board):
    # check no regular pellets are placed on walls.
    for pellet in game_board.pellets:
        assert not any(
            wall.collidepoint(pellet.x, pellet.y) for wall in game_board.walls
        )

    # check that only four power pellets were created.
    assert len(game_board.power_pellets) == 4

    # check the position of created power pellets.
    power_pellet_positions = [
        (50, 50),
        (game_board.width - 50, 50),
        (50, game_board.height - 50),
        (game_board.width - 50, game_board.height - 50),
    ]

    for power_pellet in game_board.power_pellets:
        assert any(
            power_pellet.x == pos[0] and power_pellet.y == pos[1]
            for pos in power_pellet_positions
        )


def test_draw(game_board):
    # run through drawing the game board.
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600

    test_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    game_board.draw(test_screen)
