def get_data(string):
    cups = [int(char) for char in string]
    return cups


class CycleNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        string = f"({self.value})"
        next_node = self.next_node
        while next_node != self and next_node is not None:
            string += f", {next_node.value}"
            next_node = next_node.next_node

        return string

    def to_list(self):
        nodes = [self]
        next_node = self.next_node
        while next_node != self and next_node is not None:
            nodes.append(next_node)
            next_node = next_node.next_node

        return nodes

    def uncouple(self, num_nodes=3):
        removed = self.next_node
        self.next_node = self.next_node.next_node.next_node.next_node
        removed.next_node.next_node.next_node = None

        return removed

    def couple(self, node):
        node.next_node.next_node.next_node = self.next_node
        self.next_node = node


def move(node):
    current = node
    # print(current)
    uncoupled = current.uncouple()
    next_current = current.next_node
    # print(uncoupled)
    # print(current)
    
    coupled_nodes = current.to_list()
    coupled_values = {node.value for node in coupled_nodes}
    destination = None
    target = current.value - 1
    while destination is None:
        if target in coupled_values:
            destination = target

        else:
            target -= 1
            if target < min(coupled_values): 
                target = max(coupled_values)

    # print(destination)
    while current.value != destination:
        current = current.next_node
    
    current.couple(uncoupled)
    # print(current)
    # print()

    return next_current


def part_one():
	# cups = get_data("389125467")
	cups = get_data("186524973")
	cups = [CycleNode(value) for value in cups]
	for idx, node in enumerate(cups):
		node.next_node = cups[(idx + 1) % len(cups)]

	current = cups[0]
	num_moves = 100
	for _ in range(num_moves):
		current = move(current)

		# print(current)
		# print()

	print(current)
	while current.value != 1:
		current = current.next_node
	current = current.next_node

	values = (node.value for node in current.to_list())
	string = "".join(str(num) for num in values)
	print(string[:-1])
    
def part_two():
	cups = get_data("389125467")
	# cups = get_data("186524973")
	cups += list(range(max(cups) + 1, 14))
	cups = [CycleNode(value) for value in cups]
	for idx, node in enumerate(cups):
		node.next_node = cups[(idx + 1) % len(cups)]

	current = cups[0]
	states = {tuple(current.to_list())}
	num_moves = 100000
	for turn in range(num_moves):
		current = move(current)
		state = tuple(current.to_list())
		if state in states:
			print(turn)
			break
		states.add(state)
	return

	print(current)
	while current.value != 1:
		current = current.next_node
	current = current.next_node



if __name__ == '__main__':
    # part_one()
	part_two()
