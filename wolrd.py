listy_mclistface = ["ade", 2, True]
name = "asfdgd"
print(len(listy_mclistface[1:]))
part_list = listy_mclistface[1:]
listy_mclistface.append(None)
print(list(range(2, 5)))
print(str(3))

for i in range(2, 5):
    print(i)


class Country():
    def __init__(self, name_of_king, name_of_country):
        self.king = name_of_king
        self.country = name_of_country

    def __str__(self):

        countryprint = f"The king of {self.country} is {self.current_king()}"
        return countryprint

    def execute(self):
        self.king = None

    def current_king(self):
        if self.king:
            return self.king
        else:
            return "dead"


belgium = Country("Paul", "Belgium")
print(belgium.current_king())
belgium.execute()
print(belgium.current_king())


countrylist = [Country("Sven", "Sweden"),
               Country("Svon", "Norway"),
               Country("Svin", "Denmark"),
               belgium]

for state in countrylist:
    state.execute()

print(countrylist[0])


def printout():
    airspeed = input("What is the airspeed velocity of an unloaden swallow?")[0:6]
    if airspeed == "africa":
        return False
    else:
        return True


foo = printout()
print(foo)
