import dictionary
import copy

directions = copy.deepcopy(dictionary.directions)
nouns = copy.deepcopy(dictionary.nouns)
people = copy.deepcopy(dictionary.people)
spells = copy.deepcopy(dictionary.spells)

def add_direction(s):
	if s not in directions:
		directions.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'spells = ' + repr(spells) + '\n')
		target.close()
		reload(dictionary)

		
		
def add_noun(s):
	if s not in nouns:
		nouns.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'spells = ' + repr(spells) + '\n')
		target.close()
		reload(dictionary)

		

def add_people(s):
	if s not in people:
		people.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'spells = ' + repr(spells) + '\n')
		target.close()
		reload(dictionary)
		
		
