def arithmetic_arranger(problems, valProcess=False):
    # check = Error: Too many problems.
    if len(problems) > 5:
        return "Error: Too many problems."

    tups = () # use tuple for fast iteration later

    for problem in problems:
        lst = problem.split()

        # check = Error: Operator must be '+' or '-'.
        if not (lst[1] == "+" or lst[1] == "-"):
            return "Error: Operator must be '+' or '-'."

        try:
            # check =  Error: Numbers cannot be more than four digits.
            if (len(lst[0]) > 4 or len(lst[2]) > 4):
                return "Error: Numbers cannot be more than four digits."

            # check =  Error: Numbers must only contain digits.
            lst[0] = int(lst[0])
            lst[2] = int(lst[2])
        except ValueError:
            return "Error: Numbers must only contain digits."

        # all error check passed
        tups += (tuple(lst),)

    finalTuples = () # use tuple for fast iteration later

    for t in range(len(tups)):
        operation = 0

        if (tups[t][1] == "+"):
            operation = tups[t][0] + tups[t][2]
        if (tups[t][1] == "-"):
            operation = tups[t][0] - tups[t][2]

        # remove space between negative operation sign value
        operation = \
            str(operation).replace(" ","") \
            if operation < 0 else str(operation)

        lenArg1 = len(f"{tups[t][0]}")
        lenArg2 = len(f"{tups[t][1]}")
        lenArg3 = len(f"{tups[t][2]}")
        lenOperation = len(str(operation))

        len1 = lenArg1 + lenArg2 + 1
        len2 = lenArg2 + lenArg3 + 1

        standardLen = len1 if len1 > len2 else len2

        spacePrefixFirst = " " * (standardLen - lenArg1)
        spaceBetweenSecond = " " * (standardLen - (lenArg2 + lenArg3))
        dashes = "-" * standardLen
        spacePrefixSol = " " * (standardLen - lenOperation)

        line1 = f"{spacePrefixFirst}{tups[t][0]}"
        line2 = f"{tups[t][1]}{spaceBetweenSecond}{tups[t][2]}"
        line3 = f"{dashes}"
        line4 = ""

        if (valProcess):
            line4 = f"{spacePrefixSol}{operation}"

        if (t <= (len(tups) - 2)):
            line1 += (" " * 4)
            line2 += (" " * 4)
            line3 += (" " * 4)
            if (valProcess):
                line4 += (" " * 4)

        tps = (line1, line2, line3, )
        if (valProcess):
            tps += (line4,)

        finalTuples += (tps,)

    formatted = {} # use dictionary to format each value from tuple
    if (valProcess):
        formatted = { 0:"", 1:"", 2:"", 3:""}
    else:
        formatted = { 0:"", 1:"", 2:""}

    for l in finalTuples:
        for v in range(4 if valProcess else 3):
            formatted[v] += l[v]

    return (f"{formatted[0]}"
            f"\n{formatted[1]}"
            f"\n{formatted[2]}") + (f"\n{formatted[3]}" if valProcess else "")