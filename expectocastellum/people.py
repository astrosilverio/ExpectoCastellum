import json

class Person(object):

	def __init__(self, name=None, description=None, quest_item=None, quest_complete=None, reward=(), house_specific=None, out_house=()):
		self.name = name
		self.description = description
		self.dialogue = []
		self.quest_item = quest_item
		self.quest_complete = quest_complete
		self.reward = reward
		self.count = 0
		self.house_specific = house_specific
		self.out_house = out_house
		self.alive = True
		
	def setprops(self, **attrs):
		if attrs is not None:
			for attrib, val in attrs.iteritems():
				setattr(self, attrib, val)
		
	def add_dialogue(self, lines):
		self.dialogue.extend(lines)
	
	def talk(self, player, room_object):
	
		if self.alive or self.name == 'Myrtle':	
			if self.house_specific:
				if player.house == self.house_specific:
					if player.invisible == True:
						self.talk_invisibly()
					else:
						self.talk_visibly(player, room_object)
				else:
					if player.invisible == True:
						print self.out_house[1]
					else:
						print self.out_house[0]
		
			else:
				if player.invisible == True:
					self.talk_invisibly()		
				else:
					self.talk_visibly(player, room_object)				
		else:
			print "You can't talk to a corpse."
				
	def talk_invisibly(self):
		print "%s appears not to notice you." % self.name
		
	def talk_visibly(self, player, room_object):		
		if self.quest_item:
			if self.quest_item in player.invent:
				player.remove_invent(self.quest_item)
				print self.quest_complete
				print self.reward[0] + '\n'
				room_object.add_invent(self.reward[1])
				if len(self.dialogue) > 1:
					del self.dialogue[0]
			else:
				self.talk_normally()
		else:
			self.talk_normally()
	
	def talk_normally(self):
		if self.count < len(self.dialogue):
			print self.dialogue[self.count]
			self.count += 1
		else:
			self.count = 0
			print self.dialogue[self.count]
			self.count += 1



	
def make_people_from_json(gamename):
	npc = {}
	try:
		people = json.load(open('../'+gamename+"/people.json"))
		for name, person_data in people.iteritems():
			npc[name] = Person()
			npc[name].__dict__.update(person_data)
	except IOError:
		pass
	return npc

npc = make_people_from_json("example")
 
 