from random import choice
from things import objectlist
from people import npc

class Spells(object):

	def __init__(self, player, room):
		self.you = player
		self.room = room
		
	def patronus(self):
		patronuses = ["octopus", "cup of tea", "chameleon", "bear", "stag", "badger", "fox", "elephant", "mosquito"]
		self.you.patronus = choice(patronuses)
		if self.you.patronus:	
			print "A silvery " + self.you.patronus + " jumps from the end of your wand and scurries around before disappearing!"
		else:
			print "You can't cast that yet!"

	def lumos(self):
		if self.you.light == False:
			print "The tip of your wand glows bright blue!"
			self.you.light = True
		else:
			pass

	def nox(self):
		if self.you.light == True:
			print "The glowing point of light at the tip of your wand winks out."
			self.you.light = False
		else:
			pass		
	
	def avada_kedavra(self):
		if self.room.people != []:
			if npc[self.room.people[0]].alive == True:
				npc[self.room.people[0]].alive = False
				npc[self.room.people[0]].description = "There is a peaceful-looking, but thoroughly dead body on the ground."
				print "A green shaft of light shoots from your wand and strikes %s, who crumples to the ground. You will never be forgiven." % npc[self.room.people[0]].name
			else:
				print "%s is already dead!" % npc[self.room.people[0]].name
				if npc[self.room.people[0]].name == 'Myrtle':
					print "Myrtle dives into her U-Bend in a huff."
			
		elif self.room.invent != []:
			killlist = [thing if objectlist[thing].alive == True else None for thing in self.room.invent]
			if killlist:
				print "A green shaft of light shoots from your wand and strikes the %s. You will never be forgiven." % objectlist[killlist[0]].name
				if objectlist[killlist[0]].name != "diary":
					objectlist[killlist[0]].alive = False
					objectlist[killlist[0]].name = "dead " + objectlist[killlist[0]].name
					objectlist[killlist[0]].description = objectlist[killlist[0]].dead_description
					objectlist[killlist[0]].detail = "Nothing to see. It's dead. Hope you sleep well at night."
				else:
					return
			else:
				print "There's nothing here to kill."		
		else:
			print "There's nothing here to kill."