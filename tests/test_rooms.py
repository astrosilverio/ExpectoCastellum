import sys
sys.path.append('../expectocastellum')

import rooms

testplayer = rooms.Player()

def test_path_mirroring():
	room1 = rooms.Room(name = 'one', description='this is room one')
	room2 = rooms.Room(name = 'two', description = 'this is room two')
	room3 = rooms.Room(name = 'three', description = 'this is room three')
	
	rooms.phonebook={'one':room1, 'two':room2, 'three':room3}
	
	room1.add_paths({'e': 'two'})
	room2.add_paths({'s': 'three'})
	
	rooms.mirror_paths()
	
	testplayer.location = 'one'
	testplayer.go('e')
	testplayer.go('w')
	testplayer.go('e')
	testplayer.go('s')
	testplayer.go('n')
	testplayer.go('w')
	
def test_setprops():
	room = rooms.Room(name='helloroom')
	
	newthings = {'description': "this is a room", "invent": ["egg", "bacon"]}
	
	room.setprops(newthings)
	
	print room.__dict__
	
	
	