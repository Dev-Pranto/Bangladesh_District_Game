from turtle import Turtle, Screen
import pandas

IMAGE = 'bd_district_blank_map.gif'

sc = Screen()
sc.setup(width=720, height=980)
sc.title('Name the Bangladesh District')
sc.addshape(IMAGE)

image = Turtle()
image.shape(IMAGE)
image.penup()

my_pen = Turtle()
my_pen.hideturtle()
my_pen.penup()

data = pandas.read_csv('district_list.csv')
district = data['District_Name'].tolist()
xcor = data['X'].tolist()
ycor = data['Y'].tolist()
guessed_district = []
missed_district = []


condition = True
count = 0
while condition:
    user_input = sc.textinput(title=f'{count}/64 District correct',
                              prompt="What's the another District name: ")
    for item in district:
        if item == user_input.title():
            index = district.index(item)
            my_pen.goto(x=xcor[index] - 20, y=ycor[index])
            my_pen.write(arg=item, move=False, font=('Arial', 8, 'normal'))
            guessed_district.append(item)
            count += 1

    if count > 64 or user_input.title() == 'Exit':
        condition = False
        for item in district:
            if item not in guessed_district:
                missed_district.append(item)
        pandas.DataFrame(missed_district).to_csv('district_to_learn.csv')
