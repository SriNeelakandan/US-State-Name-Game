import turtle
import pandas
screen = turtle.Screen()
screen.title("India States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) # shape of turtle (cursor) change to map
i=0
is_game_on = True
guessed_state= []

while i<50 and is_game_on: 
    answer_text = screen.textinput(title=f"{i}/50 States Correct",prompt="What's another state name?")
    states_data = pandas.read_csv("50_states.csv")
    chosen_state = states_data[states_data["state"] == answer_text.title()]
    if not chosen_state.empty and chosen_state not in guessed_state:
        i+=1
        x_cor = chosen_state['x'].values[0]
        y_cor = chosen_state['y'].values[0]
        state_name = chosen_state['state'].values[0]
        guessed_state.append(state_name)
        print(type(state_name))
        location = turtle.Turtle()
        location.hideturtle()
        location.penup()
        location.goto(x_cor,y_cor)
        location.write(f"{state_name}",align="center")

score =len(guessed_state)
screen.exitonclick()

# print(states_data.columns)