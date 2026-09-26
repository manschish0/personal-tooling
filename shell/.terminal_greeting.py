import random
import subprocess

dogen_quotes = [
    "Practice and enlightenment are one.",
    
    "To study the Way is to study the self. To study the self is to forget the self.",
    
    "When you find your place where you are, practice occurs, actualizing the fundamental point.",
    
    "Do not think you will necessarily be aware of your own enlightenment.",
    
    "If you cannot find the truth right where you are, where else do you expect to find it?",
    
    "A day of sitting is a day of being Buddha.",
    
    "Do not seek the truth. Only cease to cherish opinions.",
    
    "Time itself is being, and all being is time.",
    
    "When one side is illuminated, the other side is dark.",
    
    "Nothing in the universe is hidden from you; nothing is separate."
]

animals = [
    "apt",
    "bud-frogs",
    "bunny",
    "calvin",
    "cheese",
    "cock",
    "cower",
    "daemon",
    "default",
    "dragon",
    "dragon-and-cow",
    "duck",
    "elephant",
    "elephant-in-snake",
    "eyes",
    "flaming-sheep",
    "fox",
    "ghostbusters",
    "gnu",
    "hellokitty",
    "kangaroo",
    "kiss",
    "koala",
    "kosh",
    "luke-koala",
    "mech-and-cow",
    "milk",
    "moofasa",
    "moose",
    "pony",
    "pony-smaller",
    "ren",
    "sheep",
    "skeleton",
    "snowman",
    "stegosaurus",
    "stimpy",
    "suse",
    "three-eyes",
    "turkey",
    "turtle",
    "tux",
    "unipony",
    "unipony-smaller",
    "vader",
    "vader-koala",
    "www",
]

quotes = [
    "Take it easy. You’re doing fine.",
    "One step at a time.",
    "Code slow. Think deep.",
    "Today counts.",
    "You don’t need a fresh start to begin.",
]

animal = [
    "default",
    "tux",
    "ghost",
    "stegosaurus",
]

animal = random.choice(animals)
quote = random.choice(dogen_quotes)

subprocess.run(
    ["cowsay", "-f", animal, quote],
    check=False
)

