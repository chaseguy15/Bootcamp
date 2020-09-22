class autopilotMember:
    def __init__(self,
                nm: str,
                mjr: str,
                yr: float,
                ints: str,
                ):
        self.name = nm
        self.major = mjr
        self.year = yr
        self.interests = ints

name = "Chase"
major = "Aerospace"
year = 4
interests = "Programming, propulsion, anime, music"

you = autopilotMember(name, major, year, interests)

print('Name: ', you.name)
print('Major: ', you.major)
print('Year: ', you.year)
print('Interests: ', you.interests)
