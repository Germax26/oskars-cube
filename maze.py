import functools
from os import system

"""
This code was written in a very rushed way because I wanted to get a solution to the problem as fast as possible. In future I might clean it up and make it more streamlined and more SOLID, maintainable, usable, etc... But that's a job for future me.
"""

# Dimensions of x, y, z
X = 11
Y = 11
Z = 11

planes: dict[str, list[str]] = {}

for plane in ["xy", "xz", "yz"]:
	with open(f"planes/{plane}.txt", "r") as f:
		# the first in the pair is the rows, and the second in the pair is the column.
  		# i.e., for "xy", x is going down and y is going right.
		planes[plane] = (f.read().split('\n'))
	
@functools.cache
def is_valid(x: int, y: int, z: int) -> bool:
	"""
	Whether or not a given x,y,z point is a valid place for the center of the bars
	"""
	if x < 0 or x >= X or y < 0 or y >= Y or z < 0 or z >= Z: return False
	for (plane, a, b) in [("xy", x, y), ("xz", x, z), ("yz", y, z)]:
		try:
			if planes[plane][a][b] == "@": return False
		except IndexError: assert False, (plane, a, b, planes[plane])
	return True

start = (9, 1, 5)
end = (3, 7, 3)

file_name = "graph"

def node_name(x: int, y: int, z: int) -> str:
	return f'"{x},{y},{z}"'

with open(f"{file_name}.dot", "w") as f:
	f.write("digraph {\n")
	f.write(f'\tlayout=neato;\n')
	for i in range(X):
		for j in range(Y):
			for k in range(Z):
				if not is_valid(i, j, k): continue
				if (i, j, k) == start: f.write(f'\t{node_name(i,j,k)} [label=start, color=red]\n')
				if (i, j, k) == end: f.write(f'\t{node_name(i,j,k)} [label=end, color=green]\n')
				for new in [(i+1,j,k), (i-1,j,k), (i,j+1,k), (i,j-1,k), (i,j,k+1), (i,j,k-1)]: # TODO: Make this better
					ni, nj, nk = new
					if is_valid(ni, nj, nk): f.write(f'\t{node_name(i,j,k)} -> {node_name(ni,nj,nk)}\n')

	f.write("}\n")

system(f"dot -Tsvg {file_name}.dot > {file_name}.svg &")
