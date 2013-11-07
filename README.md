What is `ExpectoCastellum`?
============================

`ExpectoCastellum` is a system designed to allow you to build text adventure games like Colossal Cave Adventure and Zork in Python. [The game around which `ExpectoCastellum` was designed] (https://github.com/astrosilverio/game) is witchcraft-and-wizardry themed, so there's a built-in framework for creating spells. 

To create a new blank game, do something like the following:

	import ExpectoCastellum as exp
	test_game = exp.game('gamename')
		
You have just created a game engine object, `test_game` that stores its data in a folder called `'gamename'`.

If you want to access your work in a new session, use

	test_game_round_two = exp.load('gamename')
	
You can name your game engine object whatever you like; it pulls its data from `'gamename'`.

Populating your game with rooms, objects, and non-player characters (NPCs) are methods on the game engine object.

Game Engines and Basic Map Construction
----------------------------------------

So now you have a game engine. The engine is how you build and run your game. To all intents and purposes, the engine IS the game. The main methods are `new`, `save`, and `play`. The full list of methods is below.

Let's add some rooms to `test_game`. We can add a room in one of two ways:

	corridor = test_game.new('room', name = 'Empty Corridor', description = "It echo-oes-oes-oes...")
	xyzzy = test_game.new_room(name = 'XYZZY')
	
**Both** methods are valid; `new_room` calls `new` with the first argument `'room'` and is present for convenience only. You can define attributes of your newly minted room with the optional arguments. **You must give your new rooms, things, and NPCs names**. This level of specification is necessary for how the engine stores its data. If you forget to give your room a name, the engine will call it `'newroom'` by default. Change the room's name and then use `test_game.update_game_dictionaries()` to ensure the room is stored properly. 

But wait! I forgot to add some attributes to my rooms. No worries! Both rooms are objects AND your engine keeps track of its rooms in the dictionary `self.roomdict` with `room.name` as the keys and `room` as the values. Therefore, **both** of the following are valid:

	corridor.start_location = True
	test_game.roomdict['XYZZY'].description = "You seem to be in a bad rip-off of Colossal Cave Adventure."

Right now, this is hardly a proper game map. We have two rooms and they're not even connected! Well, we can change that. Each room has an attribute called `paths` that is a dictionary with directions as keys and room **names** as values. 

	test_game.roomdict['Empty Corridor'].add_paths({'n': 'XYZZY'})
	xyzzy.paths = {'s': 'Empty Corridor'}
	
I'm being intentionally and willfully and possibly frustratingly inconsistent with style here because I want to emphasize that there are multiple ways to do things and you should think about the architecture in the way or ways that make the most sense to you. In the first line we access the room named `'Empty Corridor'` via the engine's `self.roomdict` and used the `add_paths` method on the room object to update `test_game.roomdict['Empty Corridor'].paths` with `paths['n'] = ['XYZZY']`. The second line just replaces the default empty room `path` dictionary with the appropriate key and value. In general, you probably want to use `add_paths` unless a room only has one connection or you know your map really well.

It's tedious to have to update *two* rooms every time you make *one* connection between rooms. Good news: you don't have to! Every new game engine automatically uses a method called `mirror_paths`, which assumes that if you get to Room B by going up from Room A, you should be able to get to Room A by going down from Room B, etc.

	final_message = test_game.new('room', name = "Quentulus Quazgar Mountains", description = "In letters of fire on the side of the mountains is spelled: 'We apologise for the inconvenience.'")
	shire = test_game.new('room', name = 'The Shire', description = "Here be hobbits.")
	
	final_message.add_paths({'e': 'XYZZY'})
	corridor.add_paths({'u': 'The Shire'})
	
	test_game.save()
	
The `save` method on `test_game` adds reverse paths so the player can get to the Quentulus Quazgar Mountains from The Shire by going down, north, and west, then saves your edits. If you want to disable path mirroring, just set `test_game.mirror_paths` to `False`. 

Putting Things and NPCs in your Rooms
---------------------------------------

Let's make some things that you can pick up and do things with, and NPCs to interact with. We make things and NPCs in a similar way to rooms:

	wand = test_game.new('thing', name = 'wand', description = "Your wand is here, and not with you, as it should be.")
	test_game.new_thing(name = 'arc reactor', description = "There is a cylinder here that glows blue.")
	
	marvin = test_game.new('npc', name = 'Marvin', description = "A Paranoid Android mutters to himself in the corner.")
	buffy = test_game.new_npc(name = 'Buffy', description = "Buffy is going through the motions (practice moves).")
	
	
Again, you **must** define things and NPCS with names. `yourthing` and `yournpc` are stored respectively as `test_game.thingdict[yourthing.name] = yourthing` and `test_game.npcdict[yournpc.name] = yournpc`. If you forget the names, `test_game` will dub them `'newthing'` and `'newnpc'`. Once you change their names, call `test_game.update_game_dictionaries()`; that adds the appropriate keys and deletes the default `newthing` or `newnpc`.

The locations of things are stored in the room objects, so to initially put your things in the map, add them to the rooms. Same goes for the NPCs:

	xyzzy.add_invent('wand')
	shire.add_invent('arc reactor')
	
	final_message.add_people('Marvin')
	corridor.add_people('Buffy')
	
Now when the player enters The Shire, the description of the arc reactor will be displayed, and when the player enters the Empty Corridor, Buffy's description will be displayed.

Things and NPCs differ from Rooms in that the parser needs to recognize their names as valid words. To this end, Thing() objects and Person() objects have a `ref_name` attribute should be a single word that you want the game parser to recognize. If you don't specify a `ref_name`, `test_game.new(type, **attrs)` will complain and then set `ref_name` to `name.replace(' ','').lower()` Therefore, all of our instantiations above would have prompted error messages, and `'wand'`, `'arcreactor'`, `'marvin'`, and `'buffy'` would have been added to the parser's list of valid words. To change a `ref_name`, reset the attribute and then save the game:

	test_game['arc reactor'].ref_name = 'reactor'
	test_game.save()
	
Now, your game will be able to process inputs such as

	> take reactor
	> drop wand
	> examine arc reactor
	> talk to marvin
	> talk to Buffy
	
(In the third line, the parser doesn't recognize `'arc'` as a valid word, skips over it, and recognizes `'reactor'`.)

And that's how you create things and people and put them in your map!

Playing Your Game
--------------------

Just call `test_game.play()` to try playing your game! If you're using `ExpectoCastellum` from the Python REPL, typing `quit` in-game will let you leave your game session and drop you back to the REPL.

Methods on Game Engine Objects
---------------------------------

* `new(self, type, **attrs)`
* `new_room(self, **attrs)`
* `new_thing(self, **attrs)`
* `new_npc(self, **attrs)`
* `update_game_dictionary(self, type)`: ensures that each instance of `type` is stored in `self.`type`dict` precisely once, under the key `instance.name`.
* `update_game_dictionaries(self)`: calls `self.update_game_dictionary` on each type of object.
* `parser_words_update(self, type, gameobject)`: adds `gameobject.ref_name` to the parser's list of acceptable words.
* `save_type(self, type)`: saves all objects of the given type to the appropriate `.json` and adds their references names to the parser's list of acceptable words by calling `self.parser_words_update`.
* `save(self)`: calls `self.save_type` on each type of object.
* `play(self)`

Additional Information
------------------------

I can't face the prospect of describing the Room(), Thing(), Person() attributes right now, or how the parsing works. If you have questions, email me at astrosilverio@gmail.com or dig through the source code or wait until I have more time on my hands :)
