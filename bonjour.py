import random

def hello():
    return random.choices(["salut", "bo", "gosse", "mange", "mon", "zob"], k=2)

def random_choice(l: list or str):
    return l[random.randint(0, len(l)-1)]

print(random_choice("jqksdhqjishd"))