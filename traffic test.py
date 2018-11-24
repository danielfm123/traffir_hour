import game
import numpy as np

import importlib
game = importlib.reload(game)

brd = game.Board()
b0 = game.Block(1,1,3,True)
b1 = game.Block(0,0,3,False)
b2 = game.Block(1,1,0,False)
target = game.Block.makeTarget(2)


print(brd.toMatrix())
print(brd.isValid())


brd.moveBlock(0,-1)
print(brd.toMatrix())
print(brd.getBoardVector())
a = brd.getMoveFeedback(0,-1)
b = brd.getMoveFeedback(0,1)
c = [a]
c.append(b)

