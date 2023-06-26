from dataclasses import dataclass, field
import re
from typing import List, TypeVar

"""
Data parsing
"""
def get_data(path):
	with open(path) as file:
		file_parts = file.read().split("\n\n")
		rules_data = file_parts[0].split("\n")
		received_messages = file_parts[1].split("\n")

	return rules_data, received_messages

def parse_rule_set(string):
	rule_set = string.split(" ")
	rule_set = list(map(int, rule_set))
	return rule_set

def parse_rule(string):
	rule = re.findall(r"[0-9]+: (.+)", string)[0]
	if re.findall(r"[a-z]+", rule):
		return rule[1:-1]

	else:
		first_level_split = rule.split(" | ")
		second_level_split = list(map(parse_rule_set, first_level_split))
		return second_level_split

def rule_sorter(string):
	return int(re.findall(r"^[0-9]+", string)[0])


def check_group(rule_group, string):
	rest_string = string
	for rule_step in rule_group:
		step_valid, rest_string = rule_step.is_valid(rest_string)
		if not step_valid:
			return None

	return rest_string


@dataclass
class Node:
	name: str
	

RuleNodeType = TypeVar("RuleNode")
@dataclass
class SubNode(Node):
	steps: List[RuleNodeType] = field(default_factory=lambda: list())

	def step_strings_to_nodes(self, rules):
		step_strings = self.steps
		self.steps = list()
		for string in step_strings:
			if "\"" in string:
				self.steps.append(la)

			else:
				self.steps.append(rules[string])


SubNodeType = TypeVar("SubNode")
@dataclass
class RuleNode(Node):
	groups: List[SubNodeType] = field(default_factory=lambda: list())


def part_one():
	rule_strings, received_messages = get_data("smallInput.txt")
	print(rule_strings, received_messages)

	rules = dict()
	sub_rules = dict()
	for string in rule_strings:
		num, rule_string = string.split(": ")
		rules[num] = RuleNode(num)

		for idx, sub_rule_string in enumerate(rule_string.split(" | ")):
			name = f"{num}.{idx}"
			sub_rule = SubNode(name)
			sub_rule.steps = sub_rule_string.split(" ")
			sub_rules[name] = sub_rule
			rules[num].groups.append(sub_rule)

	for sub_rule in sub_rules.values():
		sub_rule.step_strings_to_nodes(rules)


	print(rules)
	# print(sub_rules)


def part_two():
	pass

if __name__ == '__main__':
	part_one()