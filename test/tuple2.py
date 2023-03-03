myTup = () # use Tuple
while True:
    inp = input("enter number: ")
    if (inp == 'done' or inp == ""): break
    myTup += (float(inp),)

print(f'average: {sum(myTup) / len(myTup)}')
