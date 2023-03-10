class Category:
    def computeLedgerFunds(self):
        totalCash = 0
        for i in self.ledger:
            totalCash += float(i["amount"])
        return round(totalCash,2)

    def __init__(self, categoryName):
        self.ledger = []
        self.categoryName = categoryName

    def __str__(self):
        titleLengthMax = 30
        categoryLength = len(self.categoryName)
        firstLine = (titleLengthMax - categoryLength) / 2
        secondLine = titleLengthMax - (categoryLength + firstLine)
        strFL = "*" * int(firstLine)
        strSL = "*" * int(secondLine)
        title = f"{strFL}{self.categoryName}{strSL}\n"
        strReturn = ""
        strReturn += title

        for i in self.ledger:
            desc = i["description"][0:23]
            amount = float(i["amount"])
            amount = f"{amount:.2f}"
            addSpace = titleLengthMax - (len(desc) + len(str(amount)))
            strSpace = " " * int(addSpace)
            strReturn += f"{desc}{strSpace}{amount}\n"

        strReturn += f"Total: {self.computeLedgerFunds():.2f}"

        return strReturn

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": float(amount),"description": desc})

    def withdraw(self, amount, desc=""):
        if (amount <= 0): return False
        if not self.check_funds(float(amount)): return False
        self.ledger.append({"amount": -1 * float(amount),"description": desc})
        return True

    def get_balance(self):
        return self.computeLedgerFunds()

    def transfer(self, cash, category):
        if not self.check_funds(float(cash)): return False
        try:
            self.ledger.append({
                "amount": -1 * float(cash),
                "description": f"Transfer to {category.categoryName}"
            })
            category.ledger.append({
                "amount": float(cash),
                "description": f"Transfer from {self.categoryName}"
            })
            return True
        except:
            return False

    def check_funds(self, amount):
        return amount <= self.computeLedgerFunds()


def calculateSpending(category):
    val = 0
    for i in category.ledger:
        if (float(i["amount"]) < 0):
           val += -1 * float(i["amount"])
    return val

def create_spend_chart(categories):
    cats = []
    grandTotal = 0
    # find grandTotal for percent calculation
    for i in categories:
        cats.append({"name": i.categoryName, "total": calculateSpending(i)})
        grandTotal += calculateSpending(i)

    # calculate percentages per category
    returnCats = [] # create array for position check on graph
    for i in cats:
        percent = round((float(i["total"]) / grandTotal) * 100)
        returnCats.append([i["name"], percent])
    cats = [] # we don't use this anymore

    # build mainGraph
    mainGraph = []
    for n in range(100, -10, -10):
        spaceBefore = " "*2 if n < 10 else " " if n < 100 else ""
        mainGraph.append(f"{spaceBefore}{n}|")

    # find width then add "o" if a certain category is within that height
    # if it exist, what position is it from array
    cntVal = 100
    cIdx = 0
    for _ in mainGraph:
        catCounter = 0
        for c in returnCats:
            strEnd = " " if catCounter == len(returnCats) -1 else ""
            mainGraph[cIdx] +=  \
                " o " + strEnd if c[1] >= cntVal else "   " + strEnd
            catCounter+=1
        cntVal-=10
        cIdx+=1

    # build bar
    strBarStart = " "* 4
    strBarEnd = "-" * (len(mainGraph[0]) - 4)
    mainGraph.append(strBarStart+strBarEnd)

    # find longest category label
    longestLen = 0
    for i in categories:
        lenCheck = len(i.categoryName)
        longestLen = lenCheck if lenCheck > longestLen else longestLen

    # build labels
    for count in range(longestLen):
        strInit = "    "
        catCount = 0
        for i in categories:
            strEnd = " " if catCount == len(categories)-1 else ""
            strInit += \
                " " + i.categoryName[count] + " " + strEnd \
                if len(i.categoryName) >= count+1 else "   " + strEnd
            catCount+=1
        mainGraph.append(strInit)

    # build final string
    strFinal = "Percentage spent by category\n"
    countLast = 0
    for g in mainGraph:
        lastPart = "" if countLast == len(mainGraph) -1 else "\n"
        strFinal += f"{g}{lastPart}"
        countLast += 1

    return strFinal