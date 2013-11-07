import json
import os

class Thing(object):

	def __init__(self, name=None, description=None, grabbable=False, edible=False, taste=None, home=None, alive=False, dead_description=None, hidden=False, containing=[], detail=None, secret_detail=None, ref_name=None):
		self.name = name
		self.description = description
		self.detail = "You notice nothing of interest."
		self.grabbable = grabbable
		self.edible = edible
		self.taste = taste
		self.home = home
		self.alive = alive
		self.dead_description = dead_description
		self.hidden = hidden
		self.containing = containing
		self.secret_detail = secret_detail
		self.ref_name = ref_name

	def setprops(self, **attrs):
		if attrs is not None:
			for attrib, val in attrs.iteritems():
				setattr(self, attrib, val)
		
	def examine(self):
		print self.detail
		if self.containing is not []:
			for thing in self.containing:
				objectlist[thing].hidden = False

	def examine_special(self):
		print self.secret_detail
		if self.containing is not []:
			for thing in self.containing:
				objectlist[thing].hidden = False
				
def make_things_from_json(gamename):
	global objectlist
	objectlist = {}
	try:
		things = json.load(open(os.getcwd()+'/'+gamename+"/things.json"))
		for name, thing_data in things.iteritems():
			objectlist[name] = Thing()
			objectlist[name].__dict__.update(thing_data)
	except IOError:
		pass

make_things_from_json("example")





