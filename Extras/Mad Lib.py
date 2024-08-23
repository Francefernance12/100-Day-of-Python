
# Mad Libs game

# Create a Mad Libs story template with placeholders for words
story = """
Once upon a time in a {adjective} land, there lived a brave {noun}. 
One day, the {noun} decided to go on a {adjective} adventure. 
On the way, the {noun} encountered a {color} dragon. 
The {noun} and the dragon had a {adjective} {noun} for hours.
The end.
"""

# Prompt the user for words to fill in the placeholders
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
color = input("Enter a color: ")

# Replace the placeholders in the story with user input
completed_story = story.format(adjective=adjective, noun=noun, color=color)

# Display the completed Mad Libs story
print("\nHere's your Mad Libs story:")
print(completed_story)
