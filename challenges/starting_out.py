"""
This file will be for practicing using git and getting basics running a script.
"""

class autopilotMember:
    def __init__(self,
                name: str,
                major: str,
                year: float,
                interests: str,
                ):
        self.name = name
        self.major = major
        self.year = year
        self.interests = interests

name = ""
major = ""
year = 0
interests = ""

you = autopilotMember(name, major, year, interests)

print('Name: ', you.name)
print('Major: ', you.major)
print('Year: ', you.year)
print('Interests: ', you.interests)
