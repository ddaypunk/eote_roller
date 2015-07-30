import dice
import sys
import random
"""
A user should input the number of dice in the format on the command line as args:

#letter #letter #letter

letters:

a/A = ability
b/B = boost
c/C = challenge
d/D = difficulty
f/F = force
p/P = proficiency
s/S = setback

Could use colors instead to make it easier
"""

def roll_all(dice_to_roll):
	"""
	Takes in the argument dice list
	Decides which dice to roll
	Rolls them via roll single
	Tabulates full list of results and returns as list
	How will this use the resource file? Will the helper function use it?
	"""

	all_results = []

	for each_roll in dice_to_roll:
		times = int(each_roll[0])
		die_short = each_roll[1].lower()

		if die_short == 'a':
			single_result = roll_single(8,times,"ability")

		elif die_short == 'b':
			single_result = roll_single(6,times,"boost")

		elif die_short == 'c':
			single_result = roll_single(12,times,"challenge")

		elif die_short == 'd':
			single_result = roll_single(8,times,"difficulty")

		elif die_short == 'f':
			single_result = roll_single(12,times,"force")

		elif die_short == 'p':
			single_result = roll_single(12,times,"proficiency")

		elif die_short == 's':
			single_result = roll_single(6,times,"setback")

		# save to list as single strings, not as list of strings
		for each_single_roll in single_result:
			all_results.append(each_single_roll)

	return all_results

def roll_single(sides, times, die_type):
	"""
	Takes in a single die and number to roll
	Returns a list of single die type results
	"""
	results = []

	sides = check_dice_resource(die_type)

	for i in range(1,times):
		roll_outcome = random.choice(sides.values())
		results.append(roll_outcome)

	return results

def check_dice_resource(die_type):

	if die_type == "ability":
		return dice.ability_die

	elif die_type == "boost":
		return dice.boost_die

	elif die_type == "challenge":
		return dice.challenge_die

	elif die_type == "difficulty":
		return dice.difficulty_die

	elif die_type == "force":
		return dice.force_die

	elif die_type == "proficiency":
		return dice.proficiency_die

	elif die_type == "setback":
		return dice.setback_die	


def calc_result(roll_results_list):
	"""
	Takes in the list of all dice rolled results
	Calculates totals of each results type
	Calculates final results by cancelling out
	Uses funny results like Succeeds like a baws, Fails but looks great doing so
	"""

	total_success = 0
	total_advantage = 0
	total_triumph = 0
	total_failure = 0
	total_threat = 0
	total_despair = 0
	total_white = 0
	total_black = 0

	# these only need to be created if there is a net so they can be moved
	net_success = 0
	net_advantage = 0
	net_triumph = 0
	net_failure = 0
	net_threat = 0
	net_despair = 0
	net_white = 0
	net_black = 0
	
	# count up the occurances of each
	for each_result in roll_results_list:

		if each_result.equals("success"):
			total_success += 1

		elif each_result.equals("advantage"):
			total_advantage += 1

		elif each_result.equals("triumph"):
			total_triumph += 1

		elif each_result.equals("failure"):
			total_failure += 1

		elif each_result.equals("threat"):
			total_threat += 1

		elif each_result.equals("despair"):
			total_despair += 1

		elif each_result.equals("white"):
			total_white += 1

		elif each_result.equals("black"):
			total_black += 1

	# cancel out what can be cancelled
	# if success > fail create net success and assign success - fail
	# else create net fail and assign fail - success or 0
	# and so on (although the logic might be more interesting when things count as other things)

			

if __name__ == '__main__':
	test_values = ["2A","1P","2D"]
	print roll_all(test_values)
