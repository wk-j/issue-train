
def splitclass(preTitle,preDescription,preLabel):
    listbug = []
    listdoc = []
    listdup = []
    listenh = []
    listgood = []
    listhelp = []
    listinv = []
    i = 0
    for data in preLabel:
        if data == 'bug': listbug.append(preTitle[i]+preDescription[i])
        elif data == 'documentation': listdoc.append(preTitle[i]+preDescription[i])
        elif data == 'duplicate': listdup.append(preTitle[i]+preDescription[i])
        elif data == 'enhancement': listenh.append(preTitle[i]+preDescription[i])
        elif data == 'good first issue': listgood.append(preTitle[i]+preDescription[i])
        elif data == 'help wanted': listhelp.append(preTitle[i]+preDescription[i])
        elif data == 'invalid': listinv.append(preTitle[i]+preDescription[i])
        i = i +1
    print('bug : '+str(len(listbug)))
    print('documentation : '+str(len(listdoc)))
    print('duplicate : '+str(len(listdup)))
    print('enhancement : '+str(len(listenh)))
    print('good first issue : '+str(len(listgood)))
    print('help wanted : '+str(len(listhelp)))
    print('invalid : '+str(len(listinv)))
    return listbug,listdoc,listdup,listenh,listgood,listhelp,listinv