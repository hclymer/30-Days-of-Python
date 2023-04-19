import random

greetings = []
intros = []
links = []
expectations = []

greetings.append("Hello. ")
greetings.append("Hi, how are you. ")

intros.append("My name is Henry. ")
intros.append("Some call me Henry. ")

links.append("You may have seen me at Hopeworks. ")
links.append("I'm a software engineer intern. ")
links.append("You might have checked out my Github. ")

expectations.append("I'm here to learn python with you. ")
expectations.append("I create small python programs that are useful. ")
expectations.append("I will show you how to juggle. ")
expectations.append("If you want to survive come with me! ")

full_greeting = random.choice(greetings) + random.choice(intros) + random.choice(links) + random.choice(expectations)

print(full_greeting)