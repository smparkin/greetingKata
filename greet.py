def greet(name):
    if name == None:
        name = "my friend"
    upperStr = None
    if isinstance(name, list):
        names = name
        name = ""
        upperNames = []
        lenN = len(names)
        print(names)
        for j in range(len(names)):
            i = names[j]
            if "\"" in i:
                names.remove(i)
                i = i.replace('\"', '')
                names.insert(j, i)
            elif "," in i:
                names.remove(i)
                i = [j.strip() for j in i.split(',')]
                names.append(i[0])
                names.append(i[1])
        print(names)
        for i in names:
            if i.isupper():
                names.remove(i)
                upperNames.append(i)
        if lenN == len(upperNames):
            returnStr = "AND HELLO "
            if len(upperNames) == 1:
                name = upperNames[0]
            elif len(upperNames) == 2:
                name = upperNames[0] + " AND " + upperNames[1]
            else:
                for i in range(len(upperNames)):
                    if i == len(upperNames)-1:
                        name = name + "and " + upperNames[i]
                    else:
                        name = name + upperNames[i] + ", "
            returnStr = returnStr + name + "!"
            return returnStr
        if len(names) == 2:
            name = names[0] + " and " + names[1]
        else:
            for i in range(len(names)):
                if i == len(names)-1:
                    name = name + "and " + names[i]
                else:
                    name = name + names[i] + ", "
        if upperNames != []:
            upperStr = greet(upperNames)
    returnStr = "Hello, " + name + "."
    if name.isupper():
        returnStr = returnStr.upper()
    if upperStr != None:
        returnStr = returnStr + " " + upperStr
    return returnStr

if __name__ == "__main__":
    greet(["Amy", "BRIAN", "Charlotte"])
