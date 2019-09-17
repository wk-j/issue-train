import os


def savefile(dttitle, dtdescription, dtlabel, name):
    import csv
    with open(name, mode='w') as csv_file:
        fname = ['Label', 'Title', 'Description']
        writer = csv.DictWriter(csv_file, fieldnames=fname)
        writer.writeheader()
        i = 0
        while i < len(dttitle):
            writer.writerow(
                {'Label': dtlabel[i], 'Title': dttitle[i], 'Description': dtdescription[i]})
            i = i+1
    print("Save success")


def setfilename(name, dir):
    itemname = name.split("/")

    if not os.path.isdir(dir):
        os.mkdir(dir)

    sname = f"{dir}/{itemname[1]}.csv"
    return sname


def tosingleline(lines):
    mystr = ''.join([line.strip() for line in lines])
    return mystr


def getlabels(labels):
    data1 = str(labels).split('name="')
    st = '")'
    data2 = data1[1].split(st)
    return data2[0]


def pluslabel(datalabel):
    label = ""
    labelall = []
    for j in datalabel:
        labelall.append(tosingleline(getlabels(j)))
    for la in labelall:
        label = label+"-"+la
    return label


def loadSingleRepository(token, name, dir):
    from github import Github
    print("login.....")
    g = Github(token)
    print("Login success")
    print("Load Repository ....")
    dttitle = []
    dtdescription = []
    dtlabel = []
    repo = g.get_repo(name)
    item = repo.get_issues(state='all')
    for i in item:
        if len(i.labels) > 0:
            label = pluslabel(i.labels)
            title = tosingleline(str(i.title))
            description = tosingleline(str(i.body))
            dttitle.append(title)
            dtdescription.append(description)
            dtlabel.append(label)
    print("Load success")
    savefile(dttitle, dtdescription, dtlabel, setfilename(name, dir))


if __name__ == '__main__':
    print("import success")
