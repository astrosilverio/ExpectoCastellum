from dictionary import *

def add_directions(s):
	if s not in directions:
		directions.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'verbs = ' + repr(verbs) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'stops = ' + repr(stops) + '\n')
		target.close()
	else:
		print "Already got it."	
		
		
def add_verb(s):
	if s not in verbs:
		verbs.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'verbs = ' + repr(verbs) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'stops = ' + repr(stops) + '\n')
		target.close()
	else:
		print "Already got it."
		
		
def add_noun(s):
	if s not in nouns:
		nouns.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'verbs = ' + repr(verbs) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'stops = ' + repr(stops) + '\n')
		target.close()
	else:
		print "Already got it."
		

def add_people(s):
	if s not in people:
		people.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'verbs = ' + repr(verbs) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'stops = ' + repr(stops) + '\n')
		target.close()
	else:
		print "Already got it."
		
		
def add_stop(s):
	if s not in stops:
		stops.append(s)
		target = open('dictionary.py', 'w')
		target.truncate()
		target.write('directions = ' + repr(directions) + '\n' +
						'verbs = ' + repr(verbs) + '\n' +
						'nouns = ' + repr(nouns) + '\n' +
						'people = ' + repr(people) + '\n' +
						'stops = ' + repr(stops) + '\n')
		target.close()
	else:
		print "Already got it."
		
