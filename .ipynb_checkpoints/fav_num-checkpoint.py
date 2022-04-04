import json

prompt = input("What is your fav number? ")

filename = 'num.json'
with open(filename, 'w') as f:
    json.dump(prompt, f)
    print(f"We'll remember your number. it's {prompt}.")