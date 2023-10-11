import pandas
import turtle

screen = turtle.Screen()
screen.title("Guess the African Country")
image = "africa-map.gif"
screen.addshape(image)
turtle.shape(image)

guessed_countries = []
while len(guessed_countries) < 50:
    c_answer = screen.textinput(title=f"{len(guessed_countries)} / 54 Countries Guessed", prompt="Guess another country").title()

    country_data = pandas.read_csv("all african countries.csv")
    list_of_countries = country_data["country"].to_list()

    if c_answer == "Quit":
        break
    if c_answer in list_of_countries:
      guessed_countries.append(c_answer)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      data = country_data[country_data.country == c_answer]
      t.goto(int(data.x), int(data.y))
      t.write(c_answer)

s = turtle.Turtle()
s.hideturtle()
s.color("Black")
s.penup()
s.goto(0,0)
s.write(f"You guessed {len(guessed_countries)} / 54 coutries", align="center", font=("Courier", 20, "bold"))

countries_missed = []
for c in list_of_countries:
    if c not in guessed_countries:
        countries_missed.append(c)

remaining_c = pandas.DataFrame(countries_missed)
remaining_c.to_csv("Countries Missed.cvs")


screen.exitonclick()