import itertools

def get_data(path):
	with open(path) as file:
		file_parts = file.read().split("\n\n")
		rules_data = file_parts[0].split("\n")
		received_messages = file_parts[1].split("\n")

	return rules_data, received_messages

def parse_rules(rules_string):

	# Fill dict
	rules = dict()
	for i, line in enumerate(rules_string):
		rule = line.split(": ")[1]

		if "\"" in rule:
			rules[i] = rule[1:-1]

		else:
			rule = rule.split(" | ")
			rules[i] = [[int(num) for num in sub_rule.split(" ")] for sub_rule in rule]

	# Link dict
	for key in rules:
		if isinstance(rules[key], list):
			for sub_rule in rules[key]:
				for i, rule_key in enumerate(sub_rule):
					sub_rule[i] = rules[rule_key]

	return rules


def part_one():
	rules_string, received_messages = get_data("smallInput.txt")
	rules = parse_rules(rules_string)

	for sub_rule in rules[0][0]:
		print(sub_rule)

	for message in received_messages:
		pass


def part_two():
	pass

if __name__ == '__main__':
	part_one()