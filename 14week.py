from tkinter import*

global page
page = 1

##
def delete():
    global wordlist
    global page

    wordlist.remove(wordlist[page*3-1])
    wordlist.remove(wordlist[page*3-2])
    wordlist.remove(wordlist[page*3-3])
    with open("PhoneBook.txt", "w", encoding='UTF-8') as infile:
        for i in range(0, len(wordlist), 3):   
            if i ==0:
                inputlist = wordlist[i] + ' ' + wordlist[i+1] + ' ' + wordlist[i+2]
                infile.write(str(inputlist))
            else:
                inputlist = '\n' + wordlist[i] + ' ' + wordlist[i+1] + ' ' + wordlist[i+2]
                infile.write(str(inputlist))
                
    read()
    per(page)
    
##
    
def read():
    global words
    global wordlist
    global person_num
    infile = open("PhoneBook.txt", "r", encoding='UTF-8')
    wordlist =[]
    person_num = []
    for line in infile: #한줄씩 읽어오기
        line = line.rstrip() #\n기호 삭제하고 읽어오기
        words = line.split() #공백문자로 단어들 분리
    
        t= tuple(words)
        person_num.append(t)
    
        for word in words: #분리된 단어 wordlist에 저장
            wordlist.append(word)
    infile.close()

def save():
    newName = nameEntry.get()
    newCall = callEntry.get()
    newJob = jobEntry.get()
    new = '\n' + newName + ' ' + newCall + ' ' + newJob
    with open("PhoneBook.txt", "a", encoding='UTF-8') as infile:
        infile.write(str(new))
    read()
    per(page)

def plus():
    global page
    page =len(person_num)+1
    index.config(text ="%s/%s" %(page, page))
    initialization()

def initialization():
        nameEntry.delete(0, END)
        callEntry.delete(0, END)
        jobEntry.delete(0, END)

def per(num):
    initialization()
    nameEntry.insert(END, wordlist[num*3-3])
    callEntry.insert(END, wordlist[num*3-2])
    jobEntry.insert(END, wordlist[num*3-1])
    index.config(text ="%s/%s" %(page, len(person_num)))


def left():
    global page   
    if page == 1:
        page = len(person_num)
        per(page)       
    else:
        page -=1
        per(page)
    
def right():
    global page    
    if page >= len(person_num):
        plus()
    else:
        page += 1
        per(page)

    
window = Tk()

name = Label(window, text = "이름")
name.grid(row = 0, column = 1)
call = Label(window, text = "전화번호")
call.grid(row = 1, column = 1)
job= Label(window, text = "직장")
job.grid(row = 2, column = 1)

nameEntry = Entry(window)
nameEntry.grid(row = 0, column = 2, columnspan=2)
callEntry = Entry(window)
callEntry.grid(row = 1, column = 2, columnspan=2)
jobEntry = Entry(window)
jobEntry.grid(row = 2, column = 2, columnspan=2)

leftButton = Button(window, text = "<", padx=5, pady=5, command=left)
leftButton.grid(row = 1, column = 0, padx=20)

rightButton = Button(window, text = ">", padx=5, pady=5, command=right)
rightButton.grid(row = 1, column = 4, padx=20)

index = Label(window)
index.grid(row = 4, column = 1, columnspan=3)

saveButton = Button(window, text="삭제하기", command=delete)
saveButton.grid(row = 3, column = 1)
saveButton = Button(window, text="저장하기", command=save)
saveButton.grid(row = 3, column = 2)
plusButton = Button(window, text="추가하기", command=plus)
plusButton.grid(row = 3, column = 3)

read()
per(1)
