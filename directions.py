from maze import start, end, is_valid

# i manually just looked at the graph output and entered in all the values. In future maybe I can automate this. I just wanted to verify that my answer was correct and automate getting a set of directions for it.
path = [start, 
		(9, 1, 9),
		(7, 1, 9),
		(7, 7, 9),
		(9, 7, 9),
		(9, 7, 7),
		(9, 9, 7),
		(9, 9, 3),
		(9, 7, 3),
		(7, 7, 3),
		(7, 7, 5),
		(7, 3, 5),
		(7, 3, 3),
		(7, 1, 3),
		(5, 1, 3),
		(5, 1, 1),
		(3, 1, 1),
		(3, 1, 3),
		(3, 3, 3),
		(1, 3, 3),
		(1, 3, 5),
		(5, 3, 5),
		(5, 5, 5),
		(1, 5, 5),
		(1, 7, 5),
		(1, 7, 3),
		(1, 9, 3),
		(1, 9, 1),
		(1, 5, 1),
		(1, 5, 3),
		(3, 5, 3),
		(3, 5, 1),
		(3, 9, 1),
		(3, 9, 3),
		end
]
prev_diff_ix = -1
with open("graph.dot", "r") as f:
	graph = f.read()

	for i in range(1,len(path)):
		a = path[i-1]
		b = path[i]

		# verify that there is only one difference in x, y, or z and gets the index thereof
		diff_ix = -1
		for j in range(3):
			if a[j] != b[j]:
				assert diff_ix == -1
				diff_ix = j
		assert diff_ix != -1
		sign = 2*(a[diff_ix]<b[diff_ix])-1
		step = [(sign,0,0),(0,sign,0),(0,0,sign)][diff_ix] # difference as tuple for each step from a to b
		assert prev_diff_ix != diff_ix, i
		# ensures that every step from a to b is valid by checking that there is a line in the .dot file for every step from a to b
		# not the best way but it works
		current = a
		while current != b:
			new_current = tuple(x+y for x,y in zip(current, step)) # adds step to current
			assert f'"{current[0]},{current[1]},{current[2]}" -> "{new_current[0]},{new_current[1]},{new_current[2]}"' in graph, (i, a, b, current, new_current, diff_ix, step)
			current = new_current

		direction = {
			(0, 1): "right",
			(0, -1): "left",
			(1, 1): "down",
			(1, -1): "up",
			(2, 1): "forward",
			(2, -1): "backward"
		}[diff_ix, sign]

		print(f"{abs(a[diff_ix]-b[diff_ix])} {direction},", end=' ')
		prev_diff_ix = diff_ix
	print()

			
