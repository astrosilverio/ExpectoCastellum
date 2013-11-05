import rooms
import thesaurus
import errors
import things
import people
import json
import os

class Engine(object):

	def __init__(self, name):
		self.name = name
		self.player = rooms.Player()
		self.death = rooms.Death()
		self.start_location = ''
		
	def new(self, type, **attrs):
	
		existing = dict()
		
		if type.lower() == 'room':
			to_build = rooms.Room()
			pathextend = 'rooms'
		elif type.lower() == 'thing':
			to_build = things.Thing()
			pathextend = 'things'
		elif type.lower() == 'npc':
			to_build = people.Person()
			pathextend = 'people'
		else:
			errors.unknown_type_creation()
			return
		if not attrs or 'name' not in attrs.keys():
			to_build.name = errors.nameless_item(type.lower())
			
		to_build.setprops(**attrs)
		
		try:
			with open(os.getcwd()+'/'+self.name+'/'+pathextend+'.json') as json_repo:
				existing = json.load(json_repo)
		except IOError:
			pass
		existing[to_build.name] = { k : v for k,v in to_build.__dict__.iteritems() if v }
		
		with open(os.getcwd()+'/'+self.name+'/'+pathextend+'.json', 'w') as json_repo:
			json.dump(existing, json_repo)
		
	def new_room(self, **attrs):
		self.new('room',**attrs)
				
	def new_thing(self, **attrs):
		self.new('thing',**attrs)
		
	def new_npc(self, **attrs):
		self.new('npc',**attrs)
		
	def play(self):
		if self.start_location == '':
			errors.no_start_location()
		else:
			rooms.make_rooms_from_json(self.name)
			things.make_things_from_json(self.name)
			people.make_people_from_json(self.name)
			self.player.location = self.start_location
			rooms.phonebook[self.player.location].look(self.player)
			rooms_to_init = [room.name for room in rooms.phonebook.values() if room.stairrooms]
			for room in rooms_to_init:
				rooms.phonebook[room].shuffle_stairs()
			while True:
				user_input = raw_input("> ").lower()
				next = thesaurus.process(user_input, self.player)