def get_data(path):
	with open(path) as file:
		data = file.read().split("\n")

	departure_time = int(data[0])
	buses = data[1].split(",")
	
	return departure_time, buses

def part_one():
	departure_time, buses = get_data("input.txt")
	buses = [int(id_) for id_ in buses if id_ != "x"]

	print(departure_time, buses)

	shortest_wait = departure_time + 1
	bus_id = -1
	for bus in buses:
		last_missed_bus_diff = departure_time % bus
		depart_diff = bus - last_missed_bus_diff if last_missed_bus_diff != 0 else 0

		if depart_diff < shortest_wait:
			shortest_wait = depart_diff
			bus_id = bus

	print("Bus: %d, wait: %d, answer: %d" % (bus_id, shortest_wait, bus_id * shortest_wait))

# ====
# Naive was too slow
# ====

# def get_depart_diff(buses, timestamp):
# 	depart_diff = list()
# 	for bus in buses:
# 		last_missed_bus_diff = timestamp % bus
# 		depart_diff.append(bus - last_missed_bus_diff if last_missed_bus_diff != 0 else 0)

# 	return depart_diff	

# def part_two():
# 	_, buses = get_data("input.txt")
# 	buses = [int(id_) if id_ != "x" else None for id_ in buses]
# 	INCR = buses[0]

# 	filtered_buses = list()
# 	CORRECT_DEPART_DIFF = list()
# 	for i, bus in enumerate(buses):
# 		if bus is not None:
# 			filtered_buses.append(bus)
# 			CORRECT_DEPART_DIFF.append(i)

# 	print(buses)
# 	print(filtered_buses, CORRECT_DEPART_DIFF)

# 	timestamp = 0
# 	depart_diff = [0] * len(filtered_buses)
# 	while CORRECT_DEPART_DIFF != depart_diff:
# 		depart_diff = get_depart_diff(filtered_buses, timestamp)
# 		timestamp += INCR

# 	timestamp -= INCR
# 	print(timestamp, depart_diff)

def part_two():
	_, buses = get_data("smallInput.txt")
	buses = [int(id_) if id_ != "x" else None for id_ in buses]
	filtered_buses = list()
	CORRECT_DEPART_DIFF = list()
	for i, bus in enumerate(buses):
		if bus is not None:
			filtered_buses.append(bus)
			CORRECT_DEPART_DIFF.append(i)

	print(buses)
	print(filtered_buses, CORRECT_DEPART_DIFF)

if __name__ == '__main__':
	#part_one()
	part_two()