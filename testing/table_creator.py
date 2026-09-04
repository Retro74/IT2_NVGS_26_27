def plasserContent(data, formatering):
    try:
        if float(data)%1 ==0:
            tall= int(data)
        else:
            tall = float(data)
        return f'{str(tall):>{formatering}}'
    except:
        return f'{data:{formatering}}'

def crateTable(tableList, caption = False):
    leftUpperCorner = f'\u250C'
    horizontalLine = f'\u2500'
    rightUpperCorner = f'\u2510'
    upperTcross = f'\u252C'
    pole = f'\u2502'
    leftTcross = f'\u251C'
    rightTcross = f'\u2524'
    midCross = f'\u253C'
    leftLowerCorner = f'\u2514'
    rightLowerCorner = f'\u2518'
    lowerTcross = f'\u2534'
    leftUpperCornerCaption = f'\u2552'
    rightUpperCornerCaption = f'\u2555'
    horizontalLineCaption = f'\u2550'
    leftTcrossCaption = f'\u255E'
    rightTcrossCaption = f'\u2561'
    upperTcrossCaption = f'\u2564'
    midCrossCaption = f'\u256A'
    #Analyze colonWidts
    tableColWidts = [0]*(len(tableList[0]))
    for i in range(0,len(tableList)):
        for j in range(0,len(tableList[i])):
            if len(str(tableList[i][j])) > tableColWidts[j]:
                tableColWidts[j]=len(str(tableList[i][j]))
    if caption:
        topLine =leftUpperCornerCaption
        for i in range(0,len(tableColWidts)):
            topLine += horizontalLineCaption*tableColWidts[i]
            if i == (len(tableColWidts)-1):
                topLine += rightUpperCornerCaption + '\u000A'
            else:
                topLine += upperTcrossCaption
    else:
        topLine =leftUpperCorner
        for i in range(0,len(tableColWidts)):
            topLine += horizontalLine*tableColWidts[i]
            if i == (len(tableColWidts)-1):
                topLine += rightUpperCorner + '\u000A'
            else:
                topLine += upperTcross

    bottomLine =leftLowerCorner
    for i in range(0,len(tableColWidts)):
        bottomLine += horizontalLine*tableColWidts[i]
        if i == (len(tableColWidts)-1):
            bottomLine += rightLowerCorner + '\u000A'
        else:
            bottomLine += lowerTcross

    midLine =leftTcross
    for i in range(0,len(tableColWidts)):
        midLine += horizontalLine*tableColWidts[i]
        if i == (len(tableColWidts)-1):
            midLine += rightTcross + '\u000A'
        else:
            midLine += midCross
    if caption:
        midLineCaption =leftTcrossCaption
        for i in range(0,len(tableColWidts)):
            midLineCaption += horizontalLineCaption*tableColWidts[i]
            if i == (len(tableColWidts)-1):
                midLineCaption += rightTcrossCaption + '\u000A'
            else:
                midLineCaption += midCrossCaption


    returnstring = topLine
    #make table
    for i in range(0,len(tableList)):
        returnstring += pole
        for j in range(0,len(tableList[i])):
            #returnstring+= f'{str(tableList[i][j]):>{tableColWidts[j]}}'
            returnstring+= f'{plasserContent(tableList[i][j],tableColWidts[j])}'

            returnstring += pole
        returnstring +='\u000A'
        if i == (len(tableList)-1):
            returnstring += bottomLine
        else:
            if i == 0 and caption:
                returnstring += midLineCaption
            else:
                returnstring += midLine
    return returnstring

def setContent(content, width):
    try:
        content = float(content)
        #Is number right pos
        return content + ":>" + width
    except:
        return content + ":" + width


#Eksempel
#tabell = [
#    ["Norge", "Sverige", "Dannmark", "Finland"],
#    ["Oslo", "Stockholm", "Kjøbenhavn", "Helsinki"],
#    ["NOK", "SEK", "DK", "Mark"],
#    [6.1, 12.0, 7.2, 4.9]]
#
#print(crateTable(tabell, True))
##     ╒═════╤═════════╤══════════╤════════╕
#     │Norge│Sverige  │Dannmark  │Finland │
#     ╞═════╪═════════╪══════════╪════════╡
#     │Oslo │Stockholm│Kjøbenhavn│Helsinki│
#     ├─────┼─────────┼──────────┼────────┤
#     │NOK  │SEK      │DK        │Mark    │
#     ├─────┼─────────┼──────────┼────────┤
#     │  6.1│     12.0│       7.2│     4.9│
#     └─────┴─────────┴──────────┴────────┘

