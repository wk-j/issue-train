import logging


def splitclass(preTitle, preDescription, preLabel):
    listbug = []
    listdoc = []
    listdup = []
    listenh = []
    listgood = []
    listhelp = []
    listinv = []
    i = 0
    for data in preLabel:
        if data == 'bug':
            listbug.append(preTitle[i]+preDescription[i])
        elif data == 'documentation':
            listdoc.append(preTitle[i]+preDescription[i])
        elif data == 'duplicate':
            listdup.append(preTitle[i]+preDescription[i])
        elif data == 'enhancement':
            listenh.append(preTitle[i]+preDescription[i])
        elif data == 'good first issue':
            listgood.append(preTitle[i]+preDescription[i])
        elif data == 'help wanted':
            listhelp.append(preTitle[i]+preDescription[i])
        elif data == 'invalid':
            listinv.append(preTitle[i]+preDescription[i])
        i = i + 1

    logging.info(f"bug - {len(listbug)}")
    logging.info(f"documentation {len(listdoc)}")
    logging.info(f"duplicate - {len(listdup)}")
    logging.info(f"enhancement - {len(listenh)}")
    logging.info(f"good first issue {len(listgood)}")
    logging.info(f"help wanted - {len(listhelp)}")
    logging.info(f"invalid - {len(listinv)}")

    return listbug, listdoc, listdup, listenh, listgood, listhelp, listinv
