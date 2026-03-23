import random
import webbrowser

websites = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.github.com",
    "https://www.stackoverflow.com",
    "https://www.linkedin.com"
]

input("Press Enter to open a random website...")

random_site = random.choice(websites)

print(f"Opening: {random_site}")
webbrowser.open(random_site)
