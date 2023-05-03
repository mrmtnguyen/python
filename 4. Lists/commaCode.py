def addAND(andList):
    if (len(andList)==0):
        print('this is an empty list')
    else:
        addList=''
        for i in range(len(andList)-1):
            addList += andList[i] +', '
        print (addList + 'and ' +andList[i+1])

andAND = ['apples', 'bananas', 'tofu', 'cats', 'test']
addAND(andAND)
