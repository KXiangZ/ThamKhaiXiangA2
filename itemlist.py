from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class ItemHire(App):
    def build(self):
        self.title="Equipment Hire"
        self.root=Builder.load_file("item.kv")#load file item.kv
        self.show_item()
        return self.root

    def show_item(self):
        self.list={}
        for data in itemList:#get data that store in itemList
            content=data.split(',')#split the data by ,
            for info in content:#append all the element into temp_storage
                temp_storage.append(info)
            if content[3] == "in":
                color_code = [0, 0, 1, 1]#blue
            else:
                color_code = [0, 1, 0, 1]#green
            self.list[content[0]]=Button(text=content[0],background_color=color_code)#add this button attribute into dictionary
            self.list[content[0]].bind(on_press=lambda a:self.button_condi())#add on press function
            self.root.ids.item.add_widget(self.list[content[0]])#add the button on to the GUI

    def label_detail(self):
        itemname = []
        available=False
        for data in itemList:#get data that store in itemList
            content = data.split(',')#split the data by ,
            itemname.append(content[0])#append item name into itemname
        if self.root.ids.hire.state == "down":#if the hire item button is pressed
            self.root.ids.label1.text = "Select available items to hire"#change the label text
            for item in itemname:#get the item name in itemname
                if self.list[item].background_color == [0,0,1,1]:#if the colour = blue
                    available=True
                if available!=True:#if available is False
                    self.root.ids.label1.text = "Hiring: no items for $0.00"#change the label text
        elif self.root.ids.list.state == "down":#if list item button is pressed
            self.root.ids.label1.text = "Choose action from the left menu, then select items on the right"#change the label text
            i=3
            for item in itemname:#get the item name in itemname
                if self.list[item].background_color==[1,0,1,1]:#change the button background colour from purple back to previous state
                    if temp_storage[i]=="in":
                        self.list[item].background_color=[0,0,1,1]
                    elif temp_storage[i]=="out":
                        self.list[item].background_color = [0, 1, 0, 1]
                i+=4
        elif self.root.ids.ret.state == "down":#if the return item button is pressed
            self.root.ids.label1.text = "Select available items to return"#change the label text
            for item in itemname:#get the item name in itemname
                if self.list[item].background_color == [0, 1, 0, 1]:
                    available = True
                if available != True:#if available is False
                    self.root.ids.label1.text = "Returning: no items"#change the label text

    def button_condi(self):
        if self.root.ids.hire.state == "down":#if the hire item button is on down state
            self.hire_item()#execute hire.item()
        elif self.root.ids.list.state == "down":#if the list item button is on down state
            self.item_detail()#execute item_detail()
        elif self.root.ids.ret.state == "down":#if the return item button is on down state
            self.ret_item()#execute ret.item()

    def hire_item(self):
        itemname = []
        for data in itemList:#get data that store in itemList
            content = data.split(',')#split the data by ,
            itemname.append(content[0])#append item name into itemname
        i=2
        price=0.0
        hiredname=""
        j=2
        record=""
        available=False
        for name in itemname:#get the item name in itemname
            if self.list[name].state=="down":#if the button is pressed
                if self.list[name].background_color==[0, 0, 1, 1]:#if the button background colour is blue
                    for item in itemname:#get the item name in itemname
                        if self.list[item].background_color==[1,0,1,1]:#if the button background colour is purple
                            if record == "":#save the item name in record
                                record += item
                            else:
                                record += ',' + item
                    if record!="":#if record is not empty
                        self.list[name].background_color = [1, 0, 1, 1]#set the button background colour as purple
                        data=record.split(',')
                        for element in data:#get the item name in record
                            if hiredname=="":#get the item price and text of purple background button
                                price+=float(temp_storage[j])
                                hiredname+=self.list[element].text
                                j+=4
                            else:
                                hiredname+=","+self.list[element].text
                                price += float(temp_storage[j])
                                j+=4
                        price += float(temp_storage[i])#get the item price and text of the button pressed
                        hiredname += "," + self.list[name].text
                        self.root.ids.label1.text="Hiring:{} for ${:.2f}".format(hiredname,price)#change the label text
                        break
                    elif record=="":
                        self.list[name].background_color = [1, 0, 1, 1]
                        price += float(temp_storage[i])#get the item price and text of the button pressed
                        hiredname += self.list[name].text
                        self.root.ids.label1.text = "Hiring:{} for ${:.2f}".format(hiredname, float(price))#change the label text
                        break
                        j+=4
                elif self.list[name].background_color==[0, 1, 0, 1]:#if green colour button is pressed
                    self.root.ids.label1.text="Hiring: no items for {:.2f}".format(price)#change the label text
                elif self.list[name].background_color==[1,0,1,1]:#if the pressed button background is purple
                    self.list[name].background_color=[0,0,1,1]#set the button pressed background to blue
                    for item in itemname:#get the item name in itemname
                        if self.list[item].background_color == [1, 0, 1, 1]:#if the button is purple background
                            available=True
                            break
                    if available==False:#if available is False
                        self.root.ids.label1.text="Hiring: no items for $0.00"#change the label text
                        break
                    else:
                        for item in itemname:#get the item name in itemname
                            if self.list[item].background_color == [1, 0, 1, 1]:#if button is purple
                                if hiredname == "":#get the item price and text of the purple background button
                                    price += float(temp_storage[j])
                                    hiredname += self.list[item].text
                                else:
                                    hiredname += "," + self.list[item].text
                                    price += float(temp_storage[j])
                            j+=4
                        self.root.ids.label1.text = "Hiring:{} for ${:.2f}".format(hiredname, float(price))#change the label text
            i+=4

    def ret_item(self):
        itemname = []
        available=False
        for data in itemList:#get data that store in itemList
            content = data.split(',')#split the data by ,
            itemname.append(content[0])#append item name into itemname
        retname = ""
        record = ""
        for name in itemname:#get the item name in itemname
            if self.list[name].state == "down":#if the button is pressed
                if self.list[name].background_color == [0, 1, 0, 1]:#if the background colour is green
                    for item in itemname:#get the item name in itemname
                        if self.list[item].background_color == [1, 0, 1, 1]:
                            if record == "":#get item name of purple background button
                                record += item
                            else:
                                record += ',' + item
                    if record != "":#if record is not empty
                        self.list[name].background_color = [1, 0, 1, 1]#set the background colour to purple
                        data = record.split(',')
                        for element in data:#get the item name in the record
                            if retname == "":#get the item name that have purple background
                                retname += self.list[element].text
                            else:
                                retname += "," + self.list[element].text
                        retname += "," + self.list[name].text#get the item name of button pressed
                        self.root.ids.label1.text = "Returning:{}".format(retname)#change the label text
                        break
                    elif record == "":#if record is empty
                        self.list[name].background_color = [1, 0, 1, 1]#set the background colour to purple
                        retname += self.list[name].text#get item name of button pressed
                        self.root.ids.label1.text = "Returning:{}".format(retname)#change the label text
                        break
                elif self.list[name].background_color == [0, 0, 1, 1]:#if blue colour button is pressed
                    self.root.ids.label1.text = "Returning: no items"#change the label text
                elif self.list[name].background_color == [1, 0, 1, 1]:#if the button pressed is purple background
                    self.list[name].background_color = [0, 1, 0, 1]#set the button pressed background to green
                    for item in itemname:#get the item name in itemname
                        if self.list[item].background_color==[1,0,1,1]:#if button is purple
                            available=True
                            break
                    if available==False:#if availabe is False
                        self.root.ids.label1.text="Returning: no items"#change the label text
                        break
                    else:
                        for item in itemname:#get the item name in itemname
                            if self.list[item].background_color == [1, 0, 1, 1]:#if button is purple
                                if retname == "":#get the item name of button
                                    retname += self.list[item].text
                                else:
                                    retname += "," + self.list[item].text
                                self.root.ids.label1.text = "Returning:{}".format(retname)#change the label text


    def item_detail(self):
        itemname = []
        for data in itemList:#get data that store in itemList
            content = data.split(',')#split the data by ,
            itemname.append(content[0])#append item name into itemname
        i=0
        for name in itemname:#get the item name in itemname
            a=i
            b=i+1
            c=i+2
            d=i+3
            if self.list[name].state=="down":#if the button is presed
                self.root.ids.label1.text="{},({}),${:.2f} is {}".format(temp_storage[a],temp_storage[b],float(temp_storage[c]),temp_storage[d])#change the label text
                break
            i+=4

    def confirm(self):
        itemname = []
        for data in itemList:#get data that store in itemList
            content = data.split(',')#split the data by ,
            itemname.append(content[0])#append item name into itemname
        i = 3
        if self.root.ids.hire.state == "down":#if the hire item button is on down state
            for item in itemname:#get the item name in itemname
                if self.list[item].background_color == [1, 0, 1, 1]:#if the button is purple background
                    self.list[item].background_color = [0, 1, 0, 1]#set the button background to green
                    temp_storage[i]="out"#change the item state from in to out
                i+=4

            self.root.ids.list.state="down"
            self.root.ids.hire.state="normal"
            self.root.ids.ret.state="normal"
            self.root.ids.label1.text = "Choose action from the left menu, then select items on the right"#change the label text
        elif self.root.ids.ret.state == "down":#if the return item button is on down state
            for item in itemname:#get the item name in itemname
                if self.list[item].background_color == [1, 0, 1, 1]:#if the button is purple background
                    self.list[item].background_color = [0, 0, 1, 1]#set the button background to blue
                    temp_storage[i] = "in"#change the item state from out to in
                i+=4
            self.root.ids.list.state = "down"
            self.root.ids.hire.state = "normal"
            self.root.ids.ret.state = "normal"
            self.root.ids.label1.text = "Choose action from the left menu, then select items on the right"#change the label text

    def add_item(self):
        addItem={}
        #setup the popup GUI
        box=BoxLayout(orientation="vertical")
        addItem['name_input']=TextInput(text="")
        addItem['desc_input']=TextInput(text="")
        addItem['price_input']=TextInput(text="")
        addItem['label']=Label(text="Enter detail for new item")
        box.add_widget(Label(text="Item Name:"))
        box.add_widget(addItem['name_input'])
        box.add_widget(Label(text="Description:"))
        box.add_widget( addItem['desc_input'])
        box.add_widget(Label(text="Price Per Day:"))
        box.add_widget(addItem['price_input'])
        box.add_widget(Button(text="Save Item",id="save",on_press=lambda a:self.item_check(popup,addItem)))
        box.add_widget(Button(text="Cancel",id="cancel",on_press=lambda a:self.cancel(popup)))
        box.add_widget(addItem['label'])
        popup=Popup(title="Add item",content=box)
        popup.open()#open the popup

    def cancel(self,popup):
        popup.dismiss()#close the popup

    def item_check(self,popup,item):
        try:
            if item['name_input'].text == "":  # if name_innput is empty
                item['label'].text = "Input cannot be blank"
            elif item['desc_input'].text == "":  # if description_input is empty
                item['label'].text = "Input cannot be blank"
            elif item['price_input'].text == "":
                item['label'].text = "Input cannot be blank"
            elif float(item['price_input'].text) < 0:  # if price_input is negative
                item['label'].text = "Price must be >= $0"
        except(ValueError):  # price_input is not number
            item['label'].text = "Invalid input; enter valid number"
        if item['name_input'].text != "" and item['desc_input'].text != "" and item['price_input'].text != "":#if none of the input is empty
            self.list[item['name_input'].text] = Button(text=item['name_input'].text, background_color=[0, 0, 1, 1])
            self.list[item['name_input'].text].bind(on_press=lambda a: self.button_condi())
            self.root.ids.item.add_widget(self.list[item['name_input'].text])#add the button to the GUI
            itemData = "{},{},{},in".format(item['name_input'].text, item['desc_input'].text,
                                            item['price_input'].text)  # sort the new data into this format
            itemDetail=[item['name_input'].text, item['desc_input'].text,item['price_input'].text,"in"]
            for element in itemDetail:
                temp_storage.append(element)#append the new data element into temp_storage
            itemList.append(itemData)  # append the new data into itemList

            popup.dismiss()#popup close
            self.root.ids.list.state = "down"
            self.root.ids.hire.state = "normal"
            self.root.ids.ret.state = "normal"
            self.root.ids.label1.text = "Choose action from the left menu, then select items on the right"#change the label text

input_file = open("inventory.csv","r+") #open the file
storage = input_file.read()#read the data in the file
itemList = storage.split('\n')#turn the file into list
input_file.close()#close the file
temp_storage=[]
inventory=""
box=""
counter=0
ItemHire().run()#run the GUI
for element in temp_storage:#get the updated data in temp_storage
    if box=="":#append the data into inventory
        box+=element
        counter+=1
    else:
        box += "," + element
        if (counter-3)%4==0:
            if inventory=="":
                inventory+=box
                box=""
                counter=0
            else:
                inventory+="\n"+box
                box=""
                counter=0
        else:
            counter+=1
input_file = open("inventory.csv","w")#open the csv file
input_file.write(inventory)  # overwrite the file with the new data
input_file.close()  # file close
data=inventory.split('\n')
for info in data:#count how many item had saved in the csv file
    counter+=1
print("{} items saved to items.csv)".format(counter))







