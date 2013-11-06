import commands
import dictionary

commands = commands.Commands()

canonwords = []
canonwords.extend(dictionary.directions)
canonwords.extend(dictionary.nouns)
canonwords.extend(dictionary.people)
canonwords.extend(dictionary.spells)

noncanonicals = {'north': 'n', 'south': 's', 'west': 'w', 'east': 'e', 'northwest': 'nw',
			'northeast': 'ne', 'southwest': 'sw', 'southeast': 'se', 'up': 'u', 'down': 'd',
	'move': 'go', 'get': 'take', 'put': 'drop', 'examine': 'x', 'ride': 'fly', 'exit': 'quit', 'inventory': 'invent',
			'nimbus': 'broom', 'erised': 'mirror', 'cup': 'tea', 'tree': 'willow', 'whizbees': 'candy', 'skeleton': 'bones', 'toad': 'trevor', 'paper': 'scrap of paper', 'scrap': 'scrap of paper', 'jar': 'spider', "candles": "candle", "tapestries": "tapestry",
			'patronum': 'patronus', 'avada': 'avada_kedavra'}

def process(user_input, player, gamename):

	commands.name = gamename
	commands.makemap()
	
	if user_input.count('s') >= 11:
		command = 'speak_parseltongue'
		args = [player]
		
	else:
		words = user_input.split()
		words = [word if (word in dir(commands) or word in canonwords) else noncanonicals.get(word, None) for word in words]
		words = [word for word in words if word is not None]
# 		print words

		if words:
			command = words[0]
			args = words[1:]
			nargs = len(words) - 1	
	
			if command in dictionary.directions:
				args = [command]
				command = 'go'
		
			if command in dictionary.spells:
				args = []
				args.append(command)
				command = 'cast'
		
			args.append(player)
	
			if nargs > 2:
				print "I don't do very well with long instructions. Try typing 'help' to learn how to talk to me."
				
		else:
			print "I didn't understand any of that."
			return
				
	try:
		return commands.__getattribute__(command)(*args)
	except AttributeError:
		print "What do you want me to do with %s?" % command
#	except TypeError:
#		print "What do you want to me to %s?" % command
	
				

	
	
	