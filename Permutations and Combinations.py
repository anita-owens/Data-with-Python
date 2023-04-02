# A Python program to print all
# permutations using library function
from itertools import permutations


# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])

# Print the obtained permutations
for i in list(perm):
	print (i)
	
#[print (i) for i in list(perm)]


# Get all permutations
perm = permutations(["route1", "route2", "route3"])

# Print the obtained permutations
for i in list(perm):
	print (i)


from itertools import permutations
lst= ['A to B', 'B to C', 'A to C', 
 'B to A', 'B to C']
#permutation of the list with r as 3
lst_com = permutations(lst,3)
# this list is to reduce redundancy
d=[]
for i in lst_com:
    t=list(i)
    # if statement to check the express routing and not include redundant values
    if t[0][0] == t[2][-1] and t[0][-1] == t[1][0] and t[1][-1]==t[2][0] and t not in d:
        d.append(t)
        print(t)
