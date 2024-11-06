# Define a Mad Libs story template
mad_libs_template = "Once upon a time, in a {adjective} {place}, there lived a {animal}. It was a {adjective} and {color} {animal}. One day, the {animal} {verb} to the {place} and met a {adjective} {person}. They became fast friends and went on an adventure to {verb} the {noun}."

# Create a dictionary to store user inputs
user_inputs = {}

# Function to get user inputs
def get_user_input(prompt):
    value = input(prompt + ": ")
    return value

# Replace placeholders in the story template with user inputs
def generate_mad_libs_story(template, inputs):
    story = template.format(**inputs)
    return story

# Get user inputs for the Mad Libs
for placeholder in ["adjective", "place", "animal", "color", "verb", "person", "noun"]:
    user_inputs[placeholder] = get_user_input(f"Enter a {placeholder}")

# Generate the Mad Libs story
mad_libs_story = generate_mad_libs_story(mad_libs_template, user_inputs)

# Display the generated story
print("\nHere's your Mad Libs story:")
print(mad_libs_story)