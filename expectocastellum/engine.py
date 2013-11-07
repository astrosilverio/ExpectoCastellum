import rooms
import thesaurus
import errors
import things
import people
import add_words
import json
import os
import dictionary

class Engine(object):

	def __init__(self, name):
		self.name = name
		rooms.make_rooms_from_json(self.name)
		things.make_things_from_json(self.name)
		people.make_people_from_json(self.name)
		self.player = rooms.Player()
		self.death = rooms.Death()
		self.start_location = ''
		self.roomdict = rooms.phonebook
		self.thingdict = things.objectlist
		self.npcdict = people.npclist
		self.mirror_paths = True
		
	def new(self, type, **attrs):
	
		if type.lower() == 'room':
			to_build = rooms.Room()
			dictname = self.roomdict
		elif type.lower() == 'thing':
			to_build = things.Thing()
			dictname = self.thingdict
		elif type.lower() == 'npc':
			to_build = people.Person()
			dictname = self.npcdict
		else:
			errors.unknown_type(type)
			return
	
		if not attrs or 'name' not in attrs.keys():
			to_build.name = errors.nameless_item(type.lower())
			
		to_build.setprops(**attrs)
		dictname[to_build.name] = to_build
		
		if (type.lower() == 'thing' or type.lower() == 'npc') and not to_build.ref_name:
			defaultname = to_build.name.replace(' ','')
			to_build.ref_name = defaultname
			errors.no_ref_name(defaultname)
		
		self.save_type(type.lower())
		
		return to_build
		
	def update_game_dictionary(self,type):
		if type.lower() == 'room':
			dictname = self.roomdict
		elif type.lower() == 'thing':
			dictname = self.thingdict
		elif type.lower() == 'npc':
			dictname = self.npcdict
		else:
			errors.unknown_type()
		for name, instance in dictname.iteritems():
			if name != instance.name:
				dictname[instance.name] = instance			
				del dictname[name]
	
	def update_game_dictionaries(self):
		self.update_game_dictionary('room')
		self.update_game_dictionary('thing')
		self.update_game_dictionary('npc')
		
	def save_type(self, type):	
	
		existing = dict()
		
		if type.lower() == 'room':
			pathextend = 'rooms'
			dictname = self.roomdict
			if self.mirror_paths:
				rooms.mirror_paths()
		elif type.lower() == 'thing':
			pathextend = 'things'
			dictname = self.thingdict
		elif type.lower() == 'npc':
			pathextend = 'people'
			dictname = self.npcdict
		else:
			errors.unknown_type()
			return
			
		try:
			with open(os.getcwd()+'/'+self.name+'/'+pathextend+'.json') as json_repo:
				existing = json.load(json_repo)
		except:
			pass
		for name, instance in dictname.iteritems():
			if dictname == self.thingdict or dictname == self.npcdict:
				if not instance.ref_name:
					defaultname=instance.name.replace(' ','')
					instance.ref_name = defaultname
					errors.no_ref_name(defaultname)
				else:
					self.parser_words_update(type, instance)
			existing[name] = { k : v for k,v in instance.__dict__.iteritems() if v }
		
		with open(os.getcwd()+'/'+self.name+'/'+pathextend+'.json', 'w') as json_repo:
			json.dump(existing, json_repo)
			
	def save(self):
		self.save_type('room')
		self.save_type('thing')
		self.save_type('npc')
	
	def parser_words_update(self, type, gameobject):
		if type.lower() == 'thing':
			add_words.add_noun(gameobject.ref_name)
		elif type.lower() == 'npc':
			add_words.add_people(gameobject.ref_name)
		elif type.lower() == 'room':
			errors.adding_room_to_parser_dict()
		else:
			errors.unknown_type()
	
	def new_room(self, **attrs):
		newroom = self.new('room',**attrs)
		return newroom
				
	def new_thing(self, **attrs):
		newthing = self.new('thing',**attrs)
		return newthing
		
	def new_npc(self, **attrs):
		newnpc = self.new('npc',**attrs)
		return newnpc
		
	def play(self):
		thesaurus.canonwords.extend([item for item in dictionary.directions if item not in thesaurus.canonwords])
		thesaurus.canonwords.extend([item for item in dictionary.nouns if item not in thesaurus.canonwords])
		thesaurus.canonwords.extend([item for item in dictionary.people if item not in thesaurus.canonwords])
		thesaurus.canonwords.extend([item for item in dictionary.spells if item not in thesaurus.canonwords])
		
		self.start_location = [room.name for room in rooms.phonebook.values() if room.start_location]
		if len(self.start_location) > 1:
			errors.too_many_start_locations(self.start_location[0])
		elif self.start_location == '':
			errors.no_start_location()
		else:
			self.player.location = self.start_location[0]
			rooms.phonebook[self.player.location].look(self.player)
			rooms_to_init = [room.name for room in rooms.phonebook.values() if room.stairrooms]
			for room in rooms_to_init:
				rooms.phonebook[room].shuffle_stairs()
			while True:
				user_input = raw_input("> ").lower()
				next = thesaurus.process(user_input, self.player, self.name)
				if next == 'break':
					break