from random import shuffle, randint

quiz = [("Which door do you try to open?",
		[("Lion", "The banged-up door with mysterious creaks and clanks coming from it"),
		("Eagle", "The door to the Restricted Area of the library"),
		("Badger", "The plain door with snuffling and squeaking noises coming from it"),
		("Snake", "The fancy door with Merlin's name and odd runes on it")]),
		("Which would you most like to be known for?",
		[("Lion", "Your exploits"),
		("Eagle", "Your achievements"),
		("Badger", "Being a good friend"),
		("Snake", "Being powerful")]),
		("What's your favorite class?",
		[("Lion", "...Does flying count?"),
		("Eagle", "I can't pick! They're all great!"),
		("Badger", "Herb Studies or Magical Animals"),
		("Snake", "Anything that I'm good at")]),
		("What WizardSport position do you play?",
		[("Lion", "All of them! I love flying!"),
		("Eagle", "Does spectating count?"),
		("Badger", "I am an excellent Finder!"),
		("Snake", "Any position! I'm better than you at all of them!")]),
		("Which potion would you drink?",
		[("Lion", "Golden liquid luck"),
		("Eagle", "Sparkling wisdom froth"),
		("Badger", "Plain hot chocolate"),
		("Snake", "Thick black ooze that lets you read minds")])]
				
class SortingQuiz(object):

	def __init__(self, questions):
		self.questions = questions
		self.answers = []

	def try_to_enter(self, you):
		
		print "::insert sorting song here:: Let's get you sorted!"
		for q in self.questions:
			print q[0]
			
			shuff = shuffle(q[1])
			letters = ['a', 'b', 'c', 'd']
			key = {'a': q[1][0][0], 'b': q[1][1][0], 'c': q[1][2][0], 'd': q[1][3][0]}
			for i in range(0,4):			
				print letters[i] + '. ' + q[1][i][1]
			run = 1
			while run:			
				a = raw_input("(pick one!) ")
				a = a.lower()
				if a == 'a' or a == 'b' or a == 'c' or a == 'd':
					h = key[a]
					self.answers.append(h)
					run = False
				else:
					print "Enter a letter a-d!"
			
				
		counts = [self.answers.count('Lion'), self.answers.count('Eagle'), self.answers.count('Badger'), self.answers.count('Snake')]
		houses = ['Lion', 'Eagle', 'Badger', 'Snake']
		if counts.count(max(counts)) > 1:
			print """You're a hatstall! You had %d Lion responses, %d Eagle responses, %d Badger responses, and %d Snake responses. What house do you want to be in?
					a. Lion
					b. Eagle
					c. Badger
					d. Snake""" % (counts[0], counts[1], counts[2], counts[3])
			run = 1
			while run:
				a = raw_input("(pick one!) ")
				if a == 'a' or a == 'b' or a == 'c' or a == 'd':
					houses = {'a': 'Lion', 'b': 'Eagle', 'c': 'Badger', 'd': 'Snake'}
					house = houses[a]
					run = False
				else:
					print "Enter a letter a-d!"
		else:
			house = houses[counts.index(max(counts))]
		
		print "Congratulations! You are in %s House!" % house
		if house == 'Lion':
			print "Your Common Room password is Pig Snout."
		elif house == 'Snake':
			print "Your Common Room password is Giant Squid."
			
		patronuses = ["octopus", "chameleon", "bear", "stag", "badger", "fox", "elephant", "mosquito"]
		temp = randint(0, len(patronuses)-1)
		patronus = patronuses[temp]
		
		name = raw_input("What's your name?  ")
		name = name.lower()
		if name == 'juliette':
			house = 'SPARKLYPOO'
			print "Actually...you're in %s!!!" % house
			patronus = "raccoon"
		elif name == 'erika':
			patronus = "hedgehog"
			print "Your patronus is a %s!" % patronus
		else:
			pass
		

		you.house = house
		you.name = name
		you.patronus = patronus
		
#		you.location.look()

sortingquiz = SortingQuiz(quiz)
		
