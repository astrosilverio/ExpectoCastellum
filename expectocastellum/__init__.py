# dump main functions here?

import subprocess
import engine
import rooms
import things
import people
import json
from random import randint

current_gamename = 'example'
rooms_to_add = {}
things_to_add = {}
npcs_to_add = {}

def make_new(type, name=None):
	type = type.lower()
	global current_gamename	
	if type == 'game':
		if name is not None:
			gamename = name
		else:
			gamename = "new_game"+str(randint(0,10000))
		if gamename != current_gamename:
			subprocess.call(["mkdir", gamename])
			current_gamename = gamename			
		
	if type == 'room':
		to_build = rooms.Room()
		to_build.name = name
		global rooms_to_add
		rooms_to_add[name] = to_build
		return to_build
	
	if type == 'thing':
		to_build = things.Thing()
		to_build.name = name
		global things_to_add
		things_to_add[name] = to_build
		return to_build
		
	if type == 'npc':
		to_build = people.Person()
		to_build.name = name
		global npcs_to_add
		npcs_to_add[name] = to_build
		return to_build
		
def edit_game(name):
	global current_gamename
	current_gamename = name
	
def play(gamename=None):
	if gamename is None:
		gamename = current_gamename
	eng = engine.Engine()
	eng.play(gamename)	
	
def set_start(gamename = None):
	if gamename is None:
		gamename = current_gamename
		
def refresh_game(gamename=None):

	if gamename is None:
		gamename = current_gamename

	existing_rooms = dict()
	existing_things = dict()
	existing_npcs = dict()
	
	try:	
		rooms_file = open(gamename+'/rooms.json')
		existing_rooms = json.load(rooms_file)
		rooms_file.close()
	except IOError:
		print "no file yet"
	for name, room in rooms_to_add.iteritems():
		existing_rooms[name] = { k : v for k,v in room.__dict__.iteritems() if v }
	if existing_rooms:
		rooms_file = open(gamename+'/rooms.json', 'w')
		json.dump(existing_rooms, rooms_file)
		rooms_file.close()
		
	try:
		things_file = open(gamename+'/things.json')
		existing_things = json.load(things_file)
		things_file.close()
	except IOError:
		pass
	for name, thing in things_to_add.iteritems():
		existing_things[name] = { k : v for k,v in thing.__dict__.iteritems() if v }
	if existing_things is not None:
		things_file = open(gamename+'/things.json', 'w')
		json.dump(existing_things, things_file)

	try:
		npcs_file = open(gamename+'/npcs.json')
		existing_npcs = json.load(npcs_file)
		npcs_file.close()
	except IOError:
		pass
	for name, npc in npcs_to_add.iteritems():
		existing_npcs[name] = { k : v for k,v in npc.__dict__.iteritems() if v }
	if existing_npcs is not None:
		npcs_file = open(gamename+'/npcs.json', 'w')
		json.dump(existing_npcs, npcs_file)
		
	rooms.phonebook = rooms.make_rooms_from_json(gamename)
	print rooms.phonebook
	test = rooms.make_rooms_from_json(gamename)
	print test
	things.objectlist = things.make_things_from_json(gamename)
	people.npclist = people.make_people_from_json(gamename)
		


		