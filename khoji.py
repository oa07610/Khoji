from tkinter import * 
import math

def out_edges(G,y):
    pp = []
    x = G[y]
    for p in x:
        pp.append(p)
    return pp

def addNodes(graph,x):
  G ={}
  for i in graph:
    G[i] = x
  return G

def enqueue(queue,node,value):
  check = False
  for i in range(len(queue)):
    if queue[i][0] == node:
      if queue[i][1] > value:
        queue[i] = (node,value)
        check = True
        break
  if check == False:
    queue.append((node,value))
  queue.sort(key = lambda x: x[1])

#file reading and making graph

data = []   #does not have any empty entry
file = open("graphing.csv", "r") 

#the keys are the places
dtype = {'Fruit Vendors': 'fruits', 'New Quetta Hotel': 'dhaba', 'Mehran Lab': 'Laboratory', 'Aga Khan Lab': 'Laboratory', 'Khan Electronics': 'electric repair', 'Jabbar Oil Change': 'Oil change', 'Vital H2O RO plant': 'Water', 'Quetta Al Naseeb Hotel': 'Hotel', 'Hamza Sweets': 'confectionery', 'Al Hafiz Stationery': 'Stationery', 'Berry Line': 'Icecream', 'Talha Medical Supply': 'Medical', 'Makkah Plastics': 'Plastics', 'Masha Allah Burger': 'Burger', 'Lasani Hotel ': 'Hotel', 'Lasani Chawal Cholay': 'Hotel', 'Tyre Shop': 'puncture', 'Pan stall': 'pan', 'Irfan Sabzi Shop': 'vegetables', 'Geo Hair Salon': 'salon', 'Lahori Pakora': 'pakoray', 'Tire Shop 1': 'puncture', 'Tire Shop 2': 'puncture', 'Mumtaz Steel Works': 'steel', 'Level Up Gaming Zone': 'gaming zone', 'Quetta Star Blessings Hotel': 'Hotel', 'Al Rehman Autos': 'autos', 'Medical SubhanAllah': 'Medical', 'One Ten Communication': 'Mobile', 'Masha Allah General Store': 'store', 'Panaflex Printing': 'Stationery', 'Dollar Gaming Zone': 'gaming zone', 'Lucky Autos': 'autos', 'New Bilal Hardware': 'hardware', 'Chabi Maker': 'key maker', 'Pan shop': 'pan', 'Pakeeza Juice Center': 'juice', 'Afghan Seekh boti center': 'Hotel', 'Afghan Seekh boti': 'Hotel', 'Garment Stall': 'garment', 'sunglasses stall': 'sunglasses', 'Farhan Biryani': 'biryani', 'Adnan Chapal Wala': 'shoes', 'Pak Nagori Milk Shop': 'milk', 'Farhan Biryani 2': 'biryani', 'Sun Beam Apartments': 'Appartments', 'Habib University': 'University', 'Al Raheem Avenue': 'Appartments'}

# the keys are the types
key_type = {'fruits': ['Fruit Vendors'], 'dhaba': ['New Quetta Hotel', 'Quetta Al Khyber Hotel','Quetta Al Naseeb Hotel', 'Quetta Star Blessings Hotel'], 'Laboratory': ['Mehran Lab', 'Aga Khan Lab'], 'electric repair': ['Khan Electronics'], 'Oil change': ['Jabbar Oil Change'], 'Mobile': ['One Ten Communication'], 'Water': ['Vital H2O RO plant'], 'Stationery': ['Al Hafiz Stationery', 'Panaflex Printing'], 'Icecream': ['Berry Line'], 'Medical': ['Talha Medical Supply', 'Medical SubhanAllah'], 'Plastics': ['Makkah Plastics'], 'Burger': ['Masha Allah Burger'], 'Hotel': ['Lasani Hotel ', 'Lasani Chawal Cholay', 'Afghan Seekh boti center', 'Afghan Seekh boti', 'Quetta Star Blessings Hotel', 'Quetta Al Naseeb Hotel'], 'puncture': ['Tyre Shop', 'Tire Shop 1', 'Tire Shop 2'], 'pan': ['Pan stall', 'Pan shop'], 'vegetables': ['Irfan Sabzi Shop'], 'salon': ['Geo Hair Salon'], 'pakoray': ['Lahori Pakora'], 'steel': ['Mumtaz Steel Works'], 'gaming zone': ['Level Up Gaming Zone', 'Dollar Gaming Zone'], 'autos': ['Al Rehman Autos', 'Lucky Autos'], 'store': ['Masha Allah General Store'], 'hardware': ['New Bilal Hardware'], 'key maker': ['Chabi Maker'], 'juice': ['Pakeeza Juice Center'], 'garment': ['Garment Stall'], 'sunglasses': ['sunglasses stall'], 'biryani': ['Farhan Biryani', 'Farhan Biryani 2'], 'shoes': ['Adnan Chapal Wala'], 'milk': ['Pak Nagori Milk Shop'], 'hotel': ['Quetta Al Naseeb Hotel'], 'methai': ['Hamza Sweets'], 'Appartments': ['Sun Beam Apartments', 'Al Raheem Avenue'], 'University': ['Habib University']}

def addnodes(G,nodes):
    for i in nodes:
        G[i] = []
    return G

def addEdges(G,edges):
    for p in edges:
        G[p[0]] = G[p[0]] + [(p[1],p[2])]
        G[p[1]] = G[p[1]] + [(p[0],p[2])]
    return G

types = ['fruits', 'dhaba', 'Laboratory', 'electric repair', 'Oil change', 'Mobile', 'Water', 'Stationery', 'Icecream', 'Medical', 'Plastics', 'Burger', 'Hotel', 'puncture', 'pan', 'vegetables', 'salon', 'pakoray', 'steel', 'gaming zone', 'autos', 'store', 'hardware', 'key maker', 'juice', 'garment', 'sunglasses', 'biryani', 'shoes', 'milk', 'hotel', 'methai']
nodes = []

counter = 0
for line in file.readlines():
  column=line.split(",")
  if counter != 0:
    p = (column[0],column[1],int(column[2]),column[3])
    if column[0] not in nodes:
      nodes.append(column[0])
    if column[1] not in nodes:
      nodes.append(column[1])
    data.append(p)
  else:
    counter = counter + 1

starting_nodes = ["Sun Beam Apartments",'Habib University',"Aga Khan Lab", 'Farhan Biryani', 'Al Raheem Avenue', 'New Bilal Hardware', 'Afghan Seekh boti center']
G = {}
addnodes(G,nodes)
addEdges(G,data)
#print(G)

def sp(graph,s,e):
  PQ=[]
  enqueue(PQ,s,0)
  Dist=addNodes(graph,math.inf)
  Dist[s]=0
  visited = set()

  Prev=addNodes(graph, None)

  while len(PQ)>0:
    u=PQ.pop(0)
    children=out_edges(graph,u[0])

    for child,weight in children:
      if child in visited:
        continue
      alt=Dist[u[0]]+weight
      if alt<Dist[child]:
        Dist[child]=alt
        Prev[child]=u[0]
        enqueue(PQ,child,alt)
    visited.add(u[0])
  path=[]
  x=e
  #return Prev
  while x!=None:
      path.append(x)
      x=Prev[x] 
  path.reverse()
  return path,Dist[e]


#Main Windown
main_screen = Tk()
main_screen.title('KHOJI')
main_screen.geometry('940x601') 


#Size of canvas
canvas = Canvas(main_screen,width=950,height=601)


#BG Images
bg11 = PhotoImage(file="./bg1.png")
bg22= PhotoImage(file="./bg2.png")
bg3= PhotoImage(file="./bg3.png")
bg4= PhotoImage(file='./bg4.png')
bg4=bg4.zoom(1)
bg4=bg4.subsample(2)
bg_label=Label(main_screen, image=bg11) 
bg_label.place(x=0,y=0,relwidth=1,relheight=1) 
canvas.pack()     

loc= StringVar() 
loc.set('Enter Your Location:')

tar= StringVar()
tar.set('Enter the desired service:')

#Window2
def window2(): 
    bg_label_2=Label(main_screen, image=bg22) 
    bg_label_2.place(x=0,y=0,relwidth=1,relheight=1)  

    #Drop Down Boxes
    
    options=["Sun Beam Apartments",'Habib University',"Aga Khan Lab", 'Farhan Biryani', 'Al Raheem Avenue', 'New Bilal Hardware', 'Afghan Seekh boti center']
    drop = OptionMenu(main_screen,loc,*options)
    drop.place(x=390,y=160) 

    
    services=['fruits', 'dhaba', 'Laboratory', 'electric repair', 'Oil change', 'Mobile', 'Water', 'Stationery', 'Icecream', 'Medical', 'Plastics', 'Burger', 'Hotel', 'puncture', 'pan', 'vegetables', 'salon', 'pakoray', 'steel', 'gaming zone', 'autos', 'store', 'hardware', 'key maker', 'juice', 'garment', 'sunglasses', 'biryani', 'shoes', 'milk', 'hotel', 'methai', 'University']
    drop2 = OptionMenu(main_screen,tar,*services)
    drop2.place(x=380,y=345) 

    #Window2 buttons 
    b1 = Button(main_screen,text='Take Me There!',height=1,width = 13,fg='white',bg='orange',font=('open sans bold',14),command=window3,borderwidth=0)
    b1.place(x=390,y=425)


def map():
    
    top=Toplevel(main_screen)
    top.geometry('700x800')
    top.title('Map')
    bg_label_4=Label(top, image=bg4) 
    bg_label_4.place(x=0,y=0,relwidth=1,relheight=1)

def window3(): 
    s=loc.get()
    t=tar.get()  
    r = key_type[t]
    o = []
    for i in r:
        l,f = sp(G,s,i)
        enqueue(o,l,f)
    print(o[0][0])
    pp=o[0][0]
    q = ""
    for i in pp:
        q = q + i +"  "+'↓'+"\n"

    q = q +"DESTINATION REACHED!"

    bg_label_3=Label(main_screen, image=bg3) 
    bg_label_3.place(x=0,y=0,relwidth=1,relheight=1)
    label3=Label(main_screen,text=q,font=('open sans bold',14),bg='black',fg='white').place(x=320,y=100)
    b3=Button(main_screen, text='Show Map!',height=1,width = 9,fg='white',bg='orange',font=('open sans bold',14),command=map,borderwidth=0).place(x=420,y=520)
    

#HomePage Buttons
b1 = Button(main_screen,text='START!',height=1,width = 7,fg='white',bg='orange',font=('open sans bold',14),command=window2,borderwidth=0)
b1.place(x=420,y=490)






main_screen.mainloop()