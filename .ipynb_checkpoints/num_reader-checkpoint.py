import json

filename = 'num.json'
try:
    with open(filename) as f:
        usernum = json.load(f)
except FileNotFoundError:
    prompt = input("What is your fav number? ")
    with open(filename, 'w') as f:
        json.dump(prompt, f)
        print(f"We'll remember your number. it's {prompt}.")
else:
    print(f"I know your favorite number. It's {usernum}.")