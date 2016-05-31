"""
Tham Khai Xiang 14/4/2016
This is a program that allow for hiring or returning multiple item.
github link:https://github.com/KXiangZ/ThamKhaiXiangA1
"""
#function load_item start
def load_item():
    itemList = storage.split('\n')#turn the file/updated file into list
    itemNo=0
    show=""
    for data in itemList:#loop data in the itemList
        content=data.split(',')#split the data with comma
        for i in range(0,4):
            content[i].strip()#strip any existing whitespace
        itemName=content[0]+ "(" +content[1]+")"#combine item name and its description into itemName
        if content[3] == "in":#change "in" to empty
            content[3] = ""
        elif content[3] == "out":#change "out" to *
            content[3] = "*"
        show += "{:3} - {:43}= $ {:.2f} {}\n".format(itemNo, itemName,float(content[2]), content[3])#sort the data inline
        itemNo+=1#itemNo+1
    print(show)#return the full data of the file
#load_item end

#function hire_item start
def hire_item():
    itemList = storage.split('\n')#turn the file/updated file into list
    itemNo = 0
    show = ""
    hiring=""
    record=""
    check=""
    global correct
    for data in itemList:#loop data in the itemList
        content = data.split(',')#split the data with comma
        for i in range(0, 4):
            content[i].strip()#strip any existing whitespace
        itemName = content[0] + "(" + content[1] + ")"
        if content[3] == "in":#change "in" to empty
            content[3] = ""
        elif content[3] == "out":#change "out" to *
            content[3] = "*"
        if content[3]=="":#if the data is "in"
            show += "{:3} - {:50}= $ {:.2f} {}\n".format(itemNo, itemName, float(content[2]), content[3])#store the data in show
            if record == "":#store the itemNo in record
                record += str(itemNo)
            else:
                record += "," + str(itemNo)
        itemNo += 1#itemNo+1
    if show == "":#if data do not have "in"
        correct=True
        return ("No item are currently can be hired")
    print(show)#display the item that can be hired
    while hiring == "":
        try:
            hiring = int((input("Enter the number of an item to hire\n")))#Enter the itemNo that want to hire
            if hiring>=0 and hiring<itemNo:#if the hiring >=0 and hiring< max value of itemNo
                for i in record.split(','):#loop the itemNo in record
                    if hiring == int(i):#check for a match itemNo
                        check = True
            else:#hiring not match
                print("Invalid item number")
                hiring = ""
        except(ValueError):
            print("Invalid input; enter a number")
    if check== True:#if there is something is hired
        for i in record.split(','):#loop the itemNo in record
            if hiring == int(i):#if get a match with record
                num = 0
                hired = ""
                itemData=""
                for data in itemList:#loop data in the itemList
                    content = data.split(',')#split the data with comma
                    for i in range(0, 4):
                        content[i].strip()#strip any existing whitespace
                    if num == hiring:#if num match with hiring(input itemNo)
                        hired = "{} hired for ${:.2f}".format(content[0], float(content[2]))#store the statement in hired
                        content[3] = "out"#change "in" to "out"
                        data="{},{},{},{}".format(content[0],content[1],content[2],content[3])#sort the data in this format
                    if num == 0:#if this is the first time to store in itemData
                        itemData += data
                    else:#not the first time store in itemData
                        itemData += "\n" + data
                    num += 1#num+1
                print(hired)#display the statement
        return (itemData)#return the data for overwrite
    else:
        correct=True
        return ("The item is not available on hire")
#hire_item end

#function return_item start
def return_item():
    itemList = storage.split('\n')#turn the file/updated file into list
    itemNo = 0
    show = ""
    retItem= ""
    record = ""
    check=""
    global correct
    for data in itemList:#loop data in the itemList
        content = data.split(',')#split the data with comma
        for i in range(0, 4):
            content[i].strip()#strip any existing whitespace
        itemName = content[0] + "(" + content[1] + ")"
        if content[3] == "in":#change "in" to empty
            content[3] = ""
        elif content[3] == "out":#change "out" to *
            content[3] = "*"
        if content[3] == "*":
            show += "{:3} - {:50}= $ {:.2f} {}\n".format(itemNo, itemName, float(content[2]), content[3])#store the data in show
            if record == "":#store the itemNo in record
                record += str(itemNo)
            else:
                record += "," + str(itemNo)
        itemNo += 1#itemNo+1
    if show == "":#if data do not have "out"
        correct=True
        return ("No item are currently on hire")
    print(show)
    while retItem == "":
        try:
            retItem = int((input("Enter the number of an item to hire\n")))#Enter the itemNo that want to return
            if retItem >= 0 and retItem < itemNo:#if the retItem >=0 and reTitem< max value of itemNo
                for i in record.split(','):#loop the itemNo in record
                    if retItem == int(i):#check for a match itemNo
                        check = True
            else:#retItem not match
                print("Invalid item number")
                retItem = ""
        except(ValueError):
            print("Invalid item number")
    if check==True:#if there is something can be returned
        for i in record.split(','):#loop the itemNo in record
            if retItem == int(i):#if get a match with record
                num = 0
                ret = ""
                itemData = ""
                for data in itemList:#loop data in the itemList
                    content = data.split(',')#split the data with comma
                    for i in range(0, 4):
                        content[i].strip()#strip any existing whitespace
                    if num == retItem:
                        ret = "{} returned".format(content[0])#store the statement in ret
                        content[3] = "in"#change "out" to "in"
                        data = "{},{},{},{}".format(content[0], content[1], content[2], content[3])#sort the data in this format
                    if num == 0:#if this is the first time to store in itemData
                        itemData += data
                    else:#not the first time store in itemData
                        itemData += "\n" + data
                    num += 1#num+1

                print(ret)#display the statement
        return(itemData)#return the data for overwrite
    else:
        correct=True
        return("The item is not available for return")
#return_item end

#function add_item start
def add_item():
    name_input = ""
    description_input = ""
    price_check = True
    while name_input == "":#check for whether name_input is empty
        name_input = input("Item name: ")
        if name_input == "":#if name_innput is empty
            print("Input cannot be blank")
    while description_input == "":#check for whether description_input is empty
        description_input = input("Description: ")
        if description_input == "":#if description_input is empty
            print("Input cannot be blank")
    while price_check == True:#check for price_input is valid
        try:
            price_input = float(input("Price per day: $"))
            if price_input < 0:#if price_input is negative
                print("Price must be >= $0")
            else:
                price_check = False
        except(ValueError):#price_input is not number
            print("Invalid input; enter valid number")
    itemData="{},{},{},in".format(name_input,description_input,price_input)#sort the data into this format
    print("{}({}),${} now available for hire".format(name_input,description_input,price_input))#print this statement
    itemList.append(itemData)#append the new data into itemList
    num=0
    itemData=""#reset itemData
    for data in itemList:#loop updated data in the itemList
        content = data.split(',')#split the data with comma
        for i in range(0, 4):
            content[i].strip()#strip any existing whitespace
            data = "{},{},{},{}".format(content[0], content[1], content[2], content[3])#sort the data into this format
        if num == 0:#if this is the first time to store in itemData
            itemData += data
        else:#not the first time store in itemData
            itemData += "\n" + data
        num += 1#num+1
    return(itemData)#return the data for overwrite
#add_item end

#function Menu start
def Menu():
    user_input = input("""Menu:
(L)ist all items
(H)ire an item
(R)eturn an item
(A)dd new item to stock
(Q)uit\n""").lower()#get user_input and lowercase it
    return(user_input)
#Menu end

#program start here
input_file = open("inventory.csv", "r+")#open the file
storage = input_file.read()#read the data in the file
counter=0
itemList = storage.split('\n')#turn the file into list
for data in itemList:#count for how many item in the file
    counter+=1
input_file.close()#file close
user_input=""
correct=False

#Welcome message
print("""Items for Hire - by Tham Khai Xiang
{} items loaded from items.csv""".format(counter))
user_input=Menu()#get user input
while True:#loop the menu
    while user_input=="l" or user_input=="h" or user_input=="r" or user_input=="a" or user_input=="q":#loop if user_input is l/h/r/a/q
        if user_input=="l":
            load_item()#call function load_item
            user_input =Menu()#get user input
        elif user_input=="h":
            result=hire_item()#call function and store the return value in result
            if correct==False:#check function work properly or not
                storage=(result)#work, store in storage
            else:
                print(result)#not work, retun the statement
            user_input =Menu()#get user input
        elif user_input=="r":
            result=return_item()#call function and store the return value in result
            if correct == False:#check function work properly or not
                storage = (result)#work, store in storage
            else:
                print(result)#not work, retun the statement
            user_input =Menu()#get user input
        elif user_input=="a":
            result=add_item()#call function and store the return value in result
            storage=result#store result in storage
            user_input =Menu()#get user input
        elif user_input=="q":
            counter=0
            itemList = storage.split('\n')
            for data in itemList:#count for how many item in the new file
                counter += 1
            print("""{} items saved to items.csv
Have a nice day :)""".format(counter))

            input_file = open("inventory.csv", "w")#file open
            input_file.write(storage)#overwrite the file with the new data
            input_file.close()#file close
            quit()#exit the program
    while user_input!="l" and user_input!="h" and user_input!="r" and user_input!="a" and user_input!="q":#loop if user input not l/h/r/a/q
        print("Invalid menu choice")
        user_input=Menu()