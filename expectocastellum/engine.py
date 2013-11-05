import rooms
import thesaurus
import errors

class Engine(object):

	def __init__(self):
		self.player = rooms.Player()
		self.death = rooms.Death()
		self.start_location = ''

	def play(self, gamename):
		if self.start_location == '':
			errors.no_start_location()
		else:
			rooms.phonebook = rooms.make_rooms_from_json(gamename)
			things.objectlist = things.make_things_from_json(gamename)
			people.npclist = people.make_people_from_json(gamename)
			you.location = self.start_location
			rooms.phonebook[you.location].look(you)
			rooms_to_init = [room.name for room in rooms.phonebook.iteritems() if room.stairrooms]
			for room in rooms_to_init:
				rooms.phonebook[room].shuffle_stairs()
		while True:
			user_input = raw_input("> ").lower()
			next = thesaurus.process(user_input, you)