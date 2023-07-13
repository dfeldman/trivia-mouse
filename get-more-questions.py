import openai
import json
import os
# Set your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the prompt
prompt = """
Please write trivia questions for a trivia game. 
Each question should be a unique question about a major celebrity like Beyonce or Barack Obama; a question about a famous country or city or place (like a sea or mountain); a question about a historical event like The American Revolution or Napoleon in Africa; or a question about scientific fact like what is a Watt or how far are we from the sun in light-minutes.
Each question should have a category and 4 possible answers. In each case, the FIRST answer should be the correct one. (They will be randomized later.)
Each question should be one that a highly intelligent American could probably answer correctly. They should vary in difficulty from easy to extremely challenging. 
Ideally, the questions should be funny or amusing by including puns, rhymes, funny false answers, etc.

Here are some examples:
Geography
What is the nickname of Philadelphia?
The City of Brotherly Love
The City of Cream Cheese
The City of Gritty
The City of Parks

What is the largest lake in North America?
Lake Superior
Lake Michigan
Salt Lake
Lake Los Angeles

Science
Who discovered the volt?
Alessandro Volta
Mars Volta
James Watt
Georg Ohm

People
Where was Barack Obama born?
Chicago
Kenya
Hawaii
Indonesia

History
Who was the last Emperor of Mexico?
Maximilian I
Penguin I
José I
Juan I

Science
How many major tectonic plates are there?
7
2
13
29

Notice that each question begins first with a category. Then on the next line is the question text. Then is the correct answer. Then 3 false answers. 
A few incorrect answers should be joke/fun answers. But most should be realistic and confusing for humans.
Answers should be short (1-5 words), including joke answers. 

Please generate 100 more questions. Thank you!
"""

# Call the API
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Get the assistant's reply
output = response['choices'][0]['message']['content']

# Append the output to a file
with open('output.txt', 'a') as f:
    f.write(output + '\n')
