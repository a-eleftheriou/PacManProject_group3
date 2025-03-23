import pytest
import pygame
from item import Pellet
from item import PowerPellet


@pytest.fixture
def pellet():
    return Pellet(5, 5)

@pytest.fixture
def power_pellet():
    return PowerPellet(50, 50)

@pytest.fixture
def walls():
    return [
        pygame.Rect(0, 0, 20, 600),  # Left wall
        pygame.Rect(200, 200, 20, 20),  # Small obstacle
        pygame.Rect(780, 0, 20, 600),  # Right wall
    ]


def test_pellet_initialization(pellet, power_pellet):
    #check default values of pellets set correctly 
    assert pellet.x == 5
    assert pellet.y == 5
    assert pellet.radius == 2
    assert pellet.collected == False 
    
    assert power_pellet.x == 50
    assert power_pellet.y == 50
    assert power_pellet.radius == 8
    assert power_pellet.collected == False

def test_draw(pellet, power_pellet):
    WINDOW_WIDTH = 750
    WINDOW_HEIGHT = 500
    
    test_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pellet.draw(test_screen)
    power_pellet.draw(test_screen)
