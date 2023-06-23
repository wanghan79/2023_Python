def funcA():
    print("funcA")

def funcB():
    print("funcB")

def funcC():
    print("funcC")

def funcD():
    print("funcD")

def txtFileReader(file):
    print("hh")
    listfiles = []
    with open(file, encoding = 'utf-8') as f:
        for line in f:
            listfiles.append(line)
    f.close()
    return listfiles



def txtFileReader(file):
    print("HH")
    with open(file, encoding = 'utf-8') as f:
        for line in f:
            yield line
    f.close()

funcs = {"a": funcA, "b": funcB, "c": funcC, "d": funcD, "e": txtFileReader}

def callfuncs(action, *args):
    return funcs[action](*args)
    # eval(funcs[action])

# for line in txtFileReader('new.txt'):
#    print(line)

# for line in callfuncs("e", "new.txt"):
#    print(line)

print(callfuncs('e', 'new.txt'))
