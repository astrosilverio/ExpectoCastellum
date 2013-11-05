# dump main functions here?

import subprocess
import engine
from random import randint

def game(name):
	subprocess.call(["mkdir", name])
	game_engine = engine.Engine(name)
	return game_engine

