x = [6,1,5,2,6,2,4,9,7,"hello",'i','paper',"sun","bread",'day']
def mass(x):
    num = []
    word = []
    for i in x:
        if type(i) == int:
            num.append(i)
            num.sort()
        elif type(i) == str:
            word.append(i)
            word.sort(key=len)
    file_1 = str(word + num)
    return file_1
with open("file.txt","w") as f:
    f.write(mass(x))
mass((x))

