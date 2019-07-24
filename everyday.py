


num =7.9 

print("The num is %f " % num)         # %f  是 浮点型 输出结果为7.900000
print (' The num is %d ' % num)       # %d   整数型 输出结果为 7
#格式  为 print ("xxx %f" % xx )

num2=9.13
print("The nums are %d and %f "%(num,num2))
print("The nums are %d and %f "%(num,3.14))
#格式 为 print ( "xxx %d and %f " % (xx,xxxx))    #   ""后面一定要有%

name ="jerry"
print (" The name is %s "% name  )          # 用""或'' 括 起来的都是 字符串string
# 给字符串赋值的时候 要这样 name="字符串"
#  字符串 用%s 引用
   
input("\n\n按下 enter 键后退出。")
# input 为 等待用户输入

name = "ada lovelace"
print (name.title())        # name.title()是将name中的字符串   首字母大写title() 
                            # name 后加.    title 后加()
                            #  upper()  全部大写   lower 全部小写  title()首字母大写

print("Languages:\n\tPython\n\tC\n\tJavaScript")  # \n 是换行   \t是制表符(就是前面空几格)

import this 
#    hhh一个彩蛋 python之禅 格言  

    # 第二部分  列表

bicycles = ['trek', 'cannondale', 'redline', 'specialized']                     #  列表格式  list=["apple","banana"]
print(bicycles[1].title())                   #输出为   Cannondale                #            print(list[1]) 
print(bicycles[-1])                         #输出为    specialized               #  一定要在输出的1 加[]
#用方括号([])来表示列表，并用逗号,来分隔其中的元素。
# 第一个列表元素的索引为0，  eg:bicycle[0] 为trek

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)              # 输出为   ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')    # 用 append 增加了元素（在最后面）                                  #增加元素  .append("xx")   最后增加元素"xx"
# 用qppend 还可以在空列表motorcycles=[]中增加元素                                                          .insert(0,"xx") 在第一个位置增加"xx"(任意位置)
print(motorcycles)              # 输出为   ['honda', 'yamaha', 'suzuki', 'ducati']

motorcycles.insert(0,"ducati")  # 用 insert 在列表任何位置增加元素 格式为：.insert(0,"xx")
print(motorcycles)              #输出为    ['ducati', 'honda', 'yamaha', 'suzuki', 'ducati']


del motorcycles[0]         #删除元素，[删除元素的位置]                                              删除元素   del   xxxx[数字]  任意位置删除元素
print(motorcycles)              #输出为    ['honda', 'yamaha', 'suzuki', 'ducati']                       .pop(数字)          任意位置删除元素并且弹出
                                                                                                    #     .remove("元素名称") 根据元素名字来删除 该元素
first_owned = motorcycles.pop(0)     # 删除，用pop()删除任意位置的元素，并且最后弹出这个元素                    但是remove只删除第一个指定的值
print (first_owned)                 #输出为 honda  # 剩余的列表元素为['yamaha', 'suzuki', 'ducati']

motorcycles.remove('ducati')        #不从位置，从具体什么值来删除 元素                      
print(motorcycles)

# 排序 
cars = ['bmw', 'audi', 'toyota', 'subaru']  
cars.sort()                                 # 用.sort() 进行排序，按字母顺序
print(cars)         

cars.sort(reverse=True )                     #用 .sort(reverse=Ture) 倒序字母排序
print(cars) 

print("\nHere is the sorted list:")        #用 "print(sorted(cars))"  一次顺序排序，不影响下面的print
print(sorted(cars))
print (sorted(cars,reverse=True))     # 字母倒序排序，同时不修改

print(cars)
legth=len(cars)                           #用len(赋值的变量)   计算列表的长度
print(legth)

# 第三部分      操作列表
# (1)for循环
cats = ['alice', 'david', 'carolina']
for cat in cats:                   # for 随便起个名 in  变量:(:要是英文的)
    print(cat)

for value in range(1,7):            #  rang(数字，数字)  一个range()函数，左开右闭
    print(value)

numbers=list(range(1,7))            #  函数list()  输出为[]    
print(numbers)

three_numbers = list(range(2,11,3))     # 可指定步长,就是range()第三个数
print(three_numbers)

7.21

kongjihe=[]                               # 输出0-12的集合并用列表的形式 (善用 for 循环)                名称=[]
for value in range(0,12):                   # #将值依次平方    #  ** 代表的是这个值的几次方             for 值 in range(数字，数字)：
    kongjihe.append(value**2)             #增加这个平方的值在空集空，然后输出空集                           名称.append(值**2)
print (kongjihe)                                            #                                        print(名称)   

squares = [value**2 for value in range(1,11)]          #                名称 =[值**2 for 值 in range(数字，数字)]
print(squares)                                          #                print(名称)

digits = [1,2,3,4,5,7,8,9,0,]                                                       #名称=[]
print(min(digits))                                                              #    print(min(名称))   min  max sum 
print(max(digits))
print(sum(digits))

list=["a","b","c","d","e"]                                  
print (list[0:2])                                           #  列表 切片  名称[数字:数字]    [:数字]  [数字:]  [:]这是全都包含，有 复制 的意思
print (list[:2])
print (list[2:])
print(list[-3:])

dimensions = (200, 50)                                       # 名称=(数,数)                          带()的是元组tuple   不能赋值改变他
print(dimensions[0])                                        #print (名称[数字])                      但是可以将一 个新元组 存储到 变量名称 中
print(dimensions[1])

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)                                                                         #但是可以将一 个新元组 存储到 变量名称 中
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

7.22
requested_toppings = ['mushrooms', 'onions', 'pineapple']       #检查元素是否在列表中，  用  in
'mushrooms' in requested_toppings

age=20
if age<=3:                                                                                      #if-elif-else
    print ("Your admission cost is $0")
elif age<=18:
    print("Your admission cost is $10")
else:
    print("Your admission cost is $20")

# if age <=3:
#     price=0                                                                   #      第二种方法
# print("Your admission cost is $" + str(price) + ".")

available_toppings = ['mushrooms', 'olives', 'green peppers',                       #  for 循环 + if 判断
'pepperoni', 'pineapple', 'extra cheese']                                           #检查列表为空    if 变量:
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:                                          #  for 代表一个变量元素名 in 变量名:   #(if同理)
        if requested_topping in available_toppings:                                 
            print("Adding " + requested_topping + ".")
else:
    print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

alien_0 = {'color': 'green', 'points': 5}                                           # 字典dict{"name":"other_name","two_name":5}
print(alien_0)                                                                      # 变量名["元素名"]=数字/ "str"/列表/字典
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

del alien_0['points']                                                               # 删除字典  del  dict_01["name_01"]
print(alien_0)

person={'name':'lizhong','age':'26','city':'BeiJing','blog':'www.jb51.net'}         #  变量名={}                            items()
for key,value in person.items():                                                # for 键，值 in 变量名  .items():        #该变量是将键和值  一一对应
    print( 'key=',key,'，value=',value)                                             #print ("随便写",键,"随便xie",值)


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in favorite_languages.keys():                                             # keys()  用函数keys()只输出键，不输出值 同理的 values()
    print(name.title())                                                         

for name in sorted(favorite_languages.keys()):                                      #sorted() 按字母排序
    print(name.title() + ", thank you for taking the poll.")   

for language in set(favorite_languages.values()):                                     # 用 set() 得到集合，没有重复的
    print(language.title()) 

7.23

  # input() 和while循环

name = input("Please enter your name: ")                                              #   input() 用法
print("Hello, " + name + "!")                                                     # print(""+"")

height=input("你有多高？")
height=int(height)                             #用 Int() 将字符串变为整形
if height>=178:
    print("\n你比我高")
else:
    print ("\n你比我矮")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:                                     #求模运算符 （ % ）
    print("\nThe number " + str(number) + " is even.")  # str() 不要忘记
else:
    print("\nThe number " + str(number) + " is odd.")   

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "         # +=可以在input()多输出一行
message = ""
while message != 'quit':                            #当为quit时 结束while , 且不再打印 input()
    message = input(prompt)
    if message != 'quit':     
        print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True                   # 将一个变量 赋值为True  用True和False来结束while 
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

while True:                                     #一个简易的例子
    message=input("\n输入你想加入的配料\n按exit退出")        
    if message =="lajiao":
        print ("\n没有这个配料")
    elif message =="exit":
        break
    else:
        print("\n我们会在披萨李加"+str(message)+"这种配料")

7.24
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']      
print(pets)
while 'cat' in pets:
    pets.remove('cat')                   #使用 while 删除 列表多个重复元素
print(pets)


while True:
#  提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response  ## 这行程式输出为{"name的内容":"response的内容"}
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        break

#  调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():    # for key,value in names.items():
    print(name + " would like to climb " + response + ".")


# 函数
def greet_user(username):         #格式  def 名字():
    print ("Hello "+username+"!")       # username 是形参   World 是实参
greet_user("World")

def describe_pet(animal_type, pet_name):        #位置形参
""" 显示宠物的信息 """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')  
# ↑↑↑ 位置实参一定和形参的位置一一对应，
# 用关键字实参的方式直接将名称与值关联起来，位置顺序就没用了

def describe_pet(pet_name, animal_type='dog'):
  #还可以直接给形参赋值，可以省略实参
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('willie')                          #最简单
describe_pet(pet_name='harry', animal_type='hamster')

#  形参，实参的 综合

def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
#  一条名为 Willie 的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
#  一只名为 Harry 的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

