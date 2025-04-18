import pytest
import pygame
from ghost import Ghost


@pytest.fixture
def ghost():
    return Ghost(50, 50, (255, 0, 0))


@pytest.fixture
def walls():
    return [
        pygame.Rect(0, 0, 20, 600),  # Left wall
        pygame.Rect(200, 200, 20, 20),  # Small obstacle
        pygame.Rect(780, 0, 20, 600),  # Right wall
    ]


@pytest.fixture
def test_ghost_initialization(ghost):
    assert ghost.x == 50
    assert ghost.y == 50
    assert ghost.color == (255, 0, 0)
    assert ghost.speed == 1
    assert ghost.radius == 10
    assert ghost.direction in ["right", "left", "up", "down"]
    assert not ghost.scared
    assert ghost.scared_timer == 0


@pytest.fixture
def test_ghost_movement(ghost, pacman, walls):
    orig_x, orig_y = ghost.x, ghost.y
    ghost.move(walls, pacman)
    assert (ghost.x != orig_x or ghost.y != orig_y)
