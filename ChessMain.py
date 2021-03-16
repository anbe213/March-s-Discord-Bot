import pygame as p
import ChessEngine

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

running = True

def GameMain():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('White'))
    gs = ChessEngine.GameState()

    while running():
      drawGameState(screen, gs)
      p.display.flip()

def drawGameState(screen, gs):
  drawBoard(screen)

def drawBoard(screen):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
          if (r + c) % 2 == 0:
            p.draw.rect(screen, p.Color('white'), p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
          else: 
            p.draw.rect(screen, p.Color('brown'), p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == '__main__':
  GameMain()