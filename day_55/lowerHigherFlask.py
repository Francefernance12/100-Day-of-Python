from flask import Flask
from random import randint

app = Flask(__name__)
random_number = randint(0, 9)


# homepage
@app.route("/")
def hello_world():
    return ('<h1>Higher-Lower</h1>'
            '<h2>Guess a number between 0 and 9</h2></br >'
            '<iframe src="https://giphy.com/embed/qJ2a8MnK9MutrKSFNw" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/AppleTV-apple-tv-app-qJ2a8MnK9MutrKSFNw">via GIPHY</a></p>'
            )


# guessing the number between 0 and 9
@app.route('/guess/<int:guessed_number>')
def show_guess(guessed_number):
    if guessed_number < random_number:
        return (f'<h1>Number {guessed_number} is too low. Retry Program!</h1></br >' 
                f'<iframe src="https://giphy.com/embed/TgmiJ4AZ3HSiIqpOj6" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/gsimedia-bruh-thats-low-bro-TgmiJ4AZ3HSiIqpOj6">via GIPHY</a></p>'
                )
    elif guessed_number > random_number:
        return (f'<h1>Number {guessed_number} is too high. Retry Program!</h1></br >'
                f'<iframe src="https://giphy.com/embed/YKroe55zFMIwpmBCu6" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/fried-cooked-poker-dipshit-YKroe55zFMIwpmBCu6">via GIPHY</a></p>'
                )

    else:
        return (f'<h1>You Found Me! Number {guessed_number}</h1></br >'
                f'<iframe src="https://giphy.com/embed/3o7abKhOpu0NwenH3O" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/spongebob-cartoon-nickelodeon-thumbs-3o7abKhOpu0NwenH3O">via GIPHY</a></p>'
                )


if __name__ == "__main__":
    app.run(debug=True)
