data = open("A-small-practice.in","r")

lines_string = []
lines_number = []

number_of_cases = data.readline()
print("number of cases : ",number_of_cases, "\n")
case = 1
for line in data:
    string , num = line.split()
    lines_string.append(string)
    lines_number.append(int(num))
    #print("case : ",case)
    # print(string," ",num)
    #level = len(string)
    #print("nodes by level")
    #nodes = [2 **x for x in range(level)]
    #print(nodes)
    #print("Total of nodes : ",sum(nodes),"\n")
    #case += 1
    #print(string, num)
print(lines_string,"\n")
print(lines_number,"\n")
data.close()

"""
level = 8
nodes = [2 **x for x in range(level)]
print(nodes)
print(sum(nodes),"\n")
print("root : ","+\n")
"""

"""
for x in nodes[1:len(nodes)-1]:
    for y in range(x):
        if (y)% 2 == 0:
            print("+",end =" ")
        else:
            print("-",end = " ")
    print("\n")
"""