from random import choice, randint
from things import objectlist
from people import npclist
import json
import os


quips = [	"""Too bad you're not a cat. GAME OVER.""",
			"""You are dead. Sucks to be you."""]
					
class Scene(object):

	def __init__(self):
		self.invent = []
		
	def add_invent(self, stuff):
		self.invent.append(stuff)
		
	def remove_invent(self, stuff):
		i = self.invent.index(stuff)
		del self.invent[i]
			
	def move(self, thing, destination):
		if thing in self.invent:
			if thing not in destination.invent:
				destination.add_invent(thing)
				self.remove_invent(thing)
			else:
				print "That is already in %s's inventory." % destination.name
		else:
			print "I don't see that here."

class Player(Scene):

	def __init__(self):
		self.name = 'Player 1'
		self.house = ''
		self.patronus = ''
		self.flying = False
		self.light = False
		self.invent = []
		self.invisible = False
		self.alive = True

	def look(self):
		print "You are carrying:"
		for thing in self.invent:
			print objectlist[thing].name
	
	def info(self):
		if self.name:
			print "Your name is %s." % self.name
		if self.house:
			print "You are in %s House!" % self.house
		if self.patronus:
			print "Your patronus is a %s." % self.patronus
			
	def drop(self, thing):
		self.move(thing, phonebook[self.location])
		if thing == 'cloak':
			self.invisible = False
		
	def take(self, thing):
		if objectlist[thing].grabbable == True:
			phonebook[self.location].move(thing, self)
			if objectlist[thing].hidden == True:
				objectlist[thing].hidden = False
			if thing == 'cloak':
				self.invisible = True
		else:
			print "You can't take that."
			
	def eat(self, thing):
		if objectlist[thing].edible == True:	
			if thing in self.invent:
				print objectlist[thing].taste
				return self.move(thing, phonebook[objectlist[thing].home])
			elif thing in phonebook[self.location].invent:
				print objectlist[thing].taste
				if self.location != objectlist[thing].home:
					return phonebook[self.location].move(thing, phonebook[objectlist[thing].home])
				else:
					pass
			else:
				print "I don't see what you want me to eat."	
		else:
			print "I can't eat that!"
			
	def go(self, direction):
		#	if direction not in directions
		try:
			nextname = phonebook[self.location].paths[direction]
			next = phonebook[nextname]
		except KeyError:
			print "You can't go that way!"
		else:	
			if direction == 'd' and self.flying == True:
				if self.location == 'Flying':
					self.flying = False
					print "You have successfully dismounted.\n"
					self.location = 'Quidditch Pitch'
					return phonebook[self.location].look(self)
				else:
					self.flying = False
					print "You have successfully dismounted.\n"
					print self.location
					return phonebook[self.location].look(self)

			if next.password != None:
				next.look(self)
			else:
				self.location = next.name
				phonebook[self.location].look(self)

					
	def fly(self):
		self.flying = True

		if "broom" in self.invent:
			print "You are flying! Everything looks different up here."
		else:
			print "You're not He-Who-Must-Not-Be-Named. Broom is necessary."
		if "bludger" in phonebook[self.location].invent:
			print "An unsecured bludger clocks you in the head. You come to your senses painfully and your vision clears slowly.\n"
			self.flying = False
			self.location = "Hospital"
			return phonebook[self.location].look(self)
		if self.location == "Quidditch Pitch":
			self.location = "Flying"
			return phonebook["Flying"].look(self)
																	
class Death(object):
	
	def look(self):
		print quips[randint(0,len(quips)-1)]		
		exit(1)


class Room(Scene):

	def __init__(self, name=None, description=None, dark=False, dark_wakeup=None, stairrooms=None, password_prompt=None, password=None, wrong_password=None, first_time=None):
		self.name = name
		self.description = description
		self.paths = {}
		self.invent = []
		self.people = []
		self.dark = dark
		self.dark_wakeup = dark_wakeup
		self.stairrooms = stairrooms
		self.password_prompt = password_prompt
		self.password = password
		self.wrong_password = wrong_password
		self.first_time = first_time
		
	def setprops(self, **attrs):
		if attrs is not None:
			for attrib, val in attrs.iteritems():
				setattr(self, attrib.lower(), val)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
	def add_invent(self, things):
		self.invent.extend(things)
		
	def add_people(self, people):
		self.people.extend(people)

	def look(self, player):
		
		if self.stairrooms:
			self.shuffle_stairs()

		if self.dark:
			self.look_darkly(player)
			
		if self.first_time:
			self.first_time = False
			sortingquiz.try_to_enter(player)
		
		else:
			proceed = True
			
			if self.password and player.location != self.name:
				proceed = self.try_to_enter(player)

			if proceed == True:
				print player.location +'\n'
				output = self.description + '\n\n'
				stuff_to_print = [objectlist[thing].description+'\n' for thing in self.invent if objectlist[thing].hidden == False]
				for thing in stuff_to_print:
					output = output + thing
				print output
				for person in self.people:
					print npclist[person].description + '\n'

	def look_darkly(self, player):
		print self.description + '\n'

		if player.light == True:
			print "You can see by the faint blue light of your wand."
			for thing in self.invent:
				print objectlist[thing].description
			for person in self.people:
				print npclist[person].description
		else:
			print "You can't see a thing. You might fall in a hole."
			num = randint(0,1)
			if num == 0:
				print "\nYou seem to have been bitten by a bowtruckle. You pass out and wake up %s." % self.dark_wakeup.name
				player.location = self.dark_wakeup.name
				print player.location.name
				phonebook[player.location].look()
			else:
				pass						

	def shuffle_stairs(self):
		self.add_paths({'u': choice(self.stairrooms)})
		
	def try_to_enter(self, player):
		user_input = raw_input(self.password_prompt + '\n> ').lower()
		if user_input == self.password:
			player.location = self.name
			return True
		else:
			print self.wrong_password
			phonebook[player.location].look(player)
			return False
						
def mirror_paths():
	opps = [('n','s'), ('e','w'), ('ne', 'sw'), ('nw','se'), ('u','d')]
	for room in phonebook.values():
		for dir, dest in room.paths.iteritems():
			dirpair = [pair for pair in opps if dir in pair]
			if dirpair[0][0] == dir:
				oppdir = dirpair[0][1]
			else:
				oppdir = dirpair[0][0]
			if room.name not in phonebook[dest].paths.values():
				phonebook[dest].add_paths({oppdir: room.name})
#				print "mirroring " + dir + ',' + dest + ' with '+ oppdir + ',' + room.name

phonebook = {}

def make_rooms_from_json(gamename):
	global phonebook
	phonebook = {}
	try:
		rooms = json.load(open(os.getcwd()+'/'+gamename+'/rooms.json'))
		print 'rooms are ', rooms
		for name, room_data in rooms.iteritems():
			phonebook[name] = Room()
			phonebook[name].__dict__.update(room_data)
	except:
		raise

phonebook = make_rooms_from_json('example')
	
