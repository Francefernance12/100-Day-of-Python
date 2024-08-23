import pandas

# dataset
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# selects furl color
squirrel_fur_color = squirrel_data["Primary Fur Color"]

# selects specific color
gray_squirrels_count = len(squirrel_fur_color[squirrel_fur_color == "Gray"])
cinnamon_squirrels_count = len(squirrel_fur_color[squirrel_fur_color == "Cinnamon"])
black_squirrels_count = len(squirrel_fur_color[squirrel_fur_color == "Black"])

# creating data frame
squirrel_color_count = {
    "Fur Color": ['gray', 'red', 'black'],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]

}
squirrel_data = pandas.DataFrame(squirrel_color_count)
squirrel_data.to_csv("squirrel_color_count.csv")

