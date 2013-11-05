import help
import spells
import json
from rooms import phonebook, Player, Room
from things import objectlist, Thing
from quiz import sortingquiz
from people import npclist, Person

class Commands(object):

	def go(self, direction, player):
		return player.go(direction)
		
	def fly(self, player):
		return player.fly()
		
	def where(self, player):
		print "You are in " + player.location	
	
	def invent(self, player):
		return player.look()
		
	def look(self, player):
		return phonebook[player.location].look(player)
		
	def talk(self, person, player):
		if person in phonebook[player.location].people:
			return npc[person].talk(player, phonebook[player.location])
		else:
			print "I don't see %s here." % person.capitalize()
	
	def sort(self, player):
		return sortingquiz.try_to_enter(player)

	def help(self, args):
		print help.helpstatement

	def quit(self, player):
		save_or_not = raw_input("Leave without saving? (y/n)"  )
		if save_or_not == 'y':
			exit(0)
		elif save_or_not == 'n':
			self.save(player)
		else:
			pass	

	def save(self, player):
		if player.name:
			confirm = raw_input("Save as " + player.name + "? (y/n)  ")
			confirm = confirm.lower()
			if confirm == 'y':
				save_game = open(player.name.lower()+"_save.json", 'w')
			else:
				savename = raw_input("Save under what name? ")
				save_game = open(savename.lower()+"_save.json", 'w')
			save_game.truncate
			player_states = {}
			room_states = {}
			thing_states = {}
			npc_states = {}
			player_states[player.name] = {k:v for k,v in player.__dict__.iteritems() if v}
			for name, room in phonebook.iteritems():
				room_states[name] = {k:v for k,v in room.__dict__.iteritems() if v}
			for name, thing in objectlist.iteritems():
				thing_states[name] = {k:v for k,v in thing.__dict__.iteritems() if v}
			for name, person in npc.iteritems():
				npc_states[name] = {k:v for k,v in person.__dict__.iteritems() if v}
			states = [player_states, room_states, thing_states, npc_states]
			json.dump(states, save_game)

		else:
			player.name = raw_input("Save under what name? ")
			save_game = open(player.name.lower()+"_save.json", 'w')
			save_game.truncate
			player_states[player.name] = {k:v for k,v in player.__dict__.iteritems() if k}
			for name, room in phonebook.iteritems():
				room_states[name] = {k:v for k,v in room.__dict__.iteritems() if k}
			for name, thing in objectlist.iteritems():
				thing_states[name] = {k:v for k,v in thing.__dict__.iteritems() if k}
			for name, person in npc.iteritems():
				npc_states[name] = {k:v for k,v in person.__dict__.iteritems() if k}
			states = [player_states, room_states, thing_states, npc_states]
			json.dump(states, save_game)

		
	def load(self, player):		
		namefile = raw_input("What name did you save under? ")
		save_game = open(namefile.lower()+"_save.json")
		states = json.load(save_game)
		player_states = states[0]
		room_states = states[1]
		thing_states = states[2]
		npc_states = states[3]
		
		for att, player_data in player_states.iteritems():
			player.__dict__.update(player_data)
		for name, room_data in room_states.iteritems():
			phonebook[name] = Room()
			phonebook[name].__dict__.update(room_data)
		for name, thing_data in thing_states.iteritems():
			objectlist[name] = Thing()
			objectlist[name].__dict__.update(thing_data)
		for name, npc_data in npc_states.iteritems():
			npc[name] = Person()
			npc[name].__dict__.update(npc_data)

	
	def speak_parseltongue(self, player):
		if player.location == "Myrtle's Bathroom":
			print "The sinks creakily move upward and outward, and the floor tile swings up to reveal a dark chute."
			phonebook["Myrtle's Bathroom"].description = phonebook["Myrtle's Bathroom"].description + "\nThe sink circle has opened to reveal a dark chute."
			phonebook["Myrtle's Bathroom"].add_paths({'d': phonebook["Chute"]})
		if player.location == "Slytherin Common Room":
			print "The eyes on the many carved snake decorations glow green."
		else:
			print "Nothing happens."	
		
	def info(self, player):
		player.info()
			
	def drop(self, thing, player):
		player.drop(thing)
	
	def take(self, thing, player):
		if thing not in objectlist:
			print "You can't take %s!" % thing
			return			
		player.take(thing)
	
	def eat(self, thing, player):
		if thing not in objectlist:
			print "You can't eat %s!" % thing
			return
		player.eat(thing)
		
	def cast(self, incantation, player):
		if "wand" in player.invent:
			spellbook = spells.Spells(player, phonebook[player.location])
			spell = getattr(spellbook, incantation)
			spell()
		else:
			print "You need your wand to cast spells!"
			
	def find_distance(self, room, object, max_distance):
		dist = 0
		location = None
		linked = set([room])
		if object in room.invent:
			location = room
		accessible_things = set(room.invent)
		while object not in accessible_things and dist <= max_distance:
			dist += 1
			temp = set()
			for chamber in linked:
				tempstrings = chamber.paths.values()
				tempobjects = [phonebook[string] for string in tempstrings]
				temp.update(tempobjects)
			linked = linked.union(temp)
			for chamber in linked:
				if object in chamber.invent:
					location = chamber
				accessible_things.update(chamber.invent)
		return dist, location			

	def accio(self, thing, player):
		if thing not in objectlist:
			print "You can't accio %s!" % thing
			return
	
		if 'wand' in player.invent:
			if objectlist[thing].grabbable == True:
				if thing in player.invent:
					print "You already have that!"
				else:
					dist, thing_location = self.find_distance(phonebook[player.location], thing, 4)
					if dist <= 3:
						print "The %s flies toward you alarmingly quickly." % thing
						return thing_location.move(thing, player)
					else:
						print "You try and try, but are not strong enough to summon the %s." % thing
			else:
				print "You're not strong enough to move that."
		else:
			print "You can't cast spells without your wand!"


	def x(self, thing, player):
		if thing in player.invent or thing in phonebook[player.location].invent:
			if objectlist[thing].hidden == True and objectlist[thing].home == player.location:
				objectlist[thing].examine_special()
			else:
				objectlist[thing].examine()
			if thing == 'hat':
				dist, location = self.find_distance(phonebook[player.location], 'sword', 50)
				if location == None and'sword' not in player.invent:
					if player.house == 'Lion':
						print "A silver sword falls out of the hat. Congratulations! You are a true Gryffindor!"
						phonebook[player.location].add_invent('sword')
					elif player.location == "Gryffindor":
						print "A silver sword falls out of the hat. The Sorting Hat cannot tell the difference between someone in Gryffindor House and someone in Gryffindor Common Room."
						phonebook[player.location].add_invent('sword')
				else:
					return
		else:
			print "I don't see that here."

