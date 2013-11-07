def unknown_type(type):
	print "I support objects of type room, thing, or npc, not %s. Sorry!" % type

def nameless_item(type):
	print "You haven't specified a name for your object. Without a name I can't keep track of your object. I'm calling it 'new%s' for now. Use <object>.name = 'WhatYouWantTheNameToBe' and then call <game>.update_game_dictionaries() to make sure it's stored as 'WhatYouWantTheNameToBe'." % type
	newname = 'new'+type
	return newname
	
def no_ref_name(refname):
	print "You haven't specified your object's ref_name, the name by which you want the game's language processor to recognize this object. I'm setting it to %s, change it if you like with <object>.ref_name = 'YourPreferredName' and then save that change with <game>.save(). See the README for more details." 
	
def adding_room_to_parser_dict():
	print "I'm not going to bother putting your room's name in the parser because your player will never need to refer to it."
	
def too_many_start_locations(room):
	print "You have multiple rooms set as your player's starting room. Make sure that <roomobject>.start_location is set to True only once. Use <game>.start_location to view the list of rooms with start_location == True. For now, I'm starting your player off in %s." % room

def no_start_location():
	print '''You have not yet set the room where you want the player to start. Use <game>.start_location = 'NameOfStartingRoom' to set the start_location.'''
	
