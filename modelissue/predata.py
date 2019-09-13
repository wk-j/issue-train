def savefile(dttitle,dtdescription,dtlabel,name):
    import csv
    with open(name, mode='w') as csv_file:
        fname = ['Label', 'Title', 'Description']
        writer = csv.DictWriter(csv_file, fieldnames=fname)
        writer.writeheader()
        i = 0
        while i<len(dttitle):
            writer.writerow({'Label': dtlabel[i], 'Title': dttitle[i], 'Description': dtdescription[i]})
            i = i+1
    print("Save success")

#ลบ <>
def deltag(msg):
    item = msg.split("<")
    if len(item)>1:
        msg = item[0]
        for i in item:
            dt = i.split(">")
            j = 1
            while j<len(dt):
                msg = msg+dt[j]
                j = j+1
    return msg

#ลบ รูป
def delimg(msg):
    item = msg.split("![")
    if len(item)>1:
        msg = item[0]
        for i in item:
            dt = i.split(")")
            j = 1
            while j<len(dt):
                msg = msg+dt[j]
                j = j+1
    return msg

def clean_msg(msg):
    import re
    import string
    #ลบ image
    msg = delimg(msg)
    #ลบ <>
    msg = deltag(msg)
    # ลบ text ที่อยู่ในวงเล็บ <> ทั้งหมด
    msg = re.sub(r'<.*?>','', msg)
    # ลบ hashtag
    msg = re.sub(r'#','',msg)
    # ลบ เครื่องหมายคำพูด (punctuation)
    for c in string.punctuation:
        msg = re.sub(r'\{}'.format(c),'',msg)
    # ลบ separator เช่น \n \t
    #msg = ' '.join(msg.split())
    return msg

def checkstandardlabel(label):
    result = "No"
    item = label.split("-")
    for i in item:
        if i == "bug" or i == "documentation" or i == "duplicate" or i == "enhancement" or i == "good first issue" or i == "help wanted" or i == "invalid":
            result = i
            break
    return result
def cutDes(preDescription):
    i = 0
    for dt in preDescription:
        if len(dt)>100:
            preDescription[i] = dt[:-(len(dt)-100)]
        i = i+1
    return preDescription
def data(DataTitle,DataDescription,DataLabel):
    preTitle = []
    preDescription = []
    preLabel = []
    i = 0
    while(i<len(DataLabel)):
        label = checkstandardlabel(DataLabel[i])
        if label != "No":
            preTitle.append(clean_msg(DataTitle[i]))
            preDescription.append(clean_msg(DataDescription[i]))
            preDescription = cutDes(preDescription)
            preLabel.append(label)
        i = i+1
    
    savefile(preTitle,preDescription,preLabel,"Documents/data.csv")
    return preTitle,preDescription,preLabel