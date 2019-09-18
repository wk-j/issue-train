import os


def save_file(title, description, label, name):
    import csv
    with open(name, mode='w') as csv_file:
        fname = ['Label', 'Title', 'Description']
        writer = csv.DictWriter(csv_file, fieldnames=fname)
        writer.writeheader()
        i = 0
        while i < len(title):
            writer.writerow(
                {'Label': label[i], 'Title': title[i], 'Description': description[i]})
            i = i + 1


def set_file_name(name, dir):
    itemname = name.split("/")

    if not os.path.isdir(dir):
        os.mkdir(dir)

    sname = f"{dir}/{itemname[1]}.csv"
    return sname


def to_single_line(lines):
    mystr = ''.join([line.strip() for line in lines])
    return mystr


def get_labels(labels):
    data1 = str(labels).split('name="')
    st = '")'
    data2 = data1[1].split(st)
    return data2[0]


def plus_label(datalabel):
    label = ""
    labelall = []
    for j in datalabel:
        labelall.append(to_single_line(get_labels(j)))
    for la in labelall:
        label = label+"-"+la
    return label


def load_single_repository(token, name, dir):
    from github import Github
    g = Github(token)
    dttitle = []
    dtdescription = []
    dtlabel = []
    repo = g.get_repo(name)
    item = repo.get_issues(state='all')
    for i in item:
        if len(i.labels) > 0:
            label = plus_label(i.labels)
            title = to_single_line(str(i.title))
            description = to_single_line(str(i.body))
            dttitle.append(title)
            dtdescription.append(description)
            dtlabel.append(label)
    save_file(dttitle, dtdescription, dtlabel, set_file_name(name, dir))
