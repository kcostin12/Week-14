
class Camper:

    def __init__(self, owner, model, length):
        self.model = model
        self.length = length
        self.owner = owner

    def camping(self):

        print(f"{self.owner} is a {self.model} and is {self.length} feet long.")

if __name__ == '__main__':
    camper = Camper("My camper","Rockwood Minilite", 26)
    neighbors_camper = Camper("My neighbor's camper","Jayco Eagle", 35)
    best_friends_camper = Camper("My best friend's camper", "Forest River Sabre", 31)


    camper.camping()
    neighbors_camper.camping()
    best_friends_camper.camping()