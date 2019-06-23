class Animals:
    name = 'unknown'  # Animal name
    voice = 'unknown'  # Animal's voice
    need_for_food = 'hungry'  # Need for food
    weight = 0  # Animal's weight, kg

    def __init__(self, name='unknown'):
        self.name = name

    # def givname(self):
    #     self.name = input('Enter mame: ')

    def feed(self):
        self.need_for_food = 'full'

    def weigh(self, value):
        self.weight += value



class Birds(Animals):
    eggs = 0  # Count of eggs
    need_for_eggs = 'not gathered'  # Eggs gathered or not

    def gather_eggs(self):
        self.need_for_eggs = 'gathered'

    def lay_eggs(self, value):
        self.eggs += value


class Geese(Birds):
    pass

goose1 = Geese('Серый')
goose2 = Geese('Белый')
goose1.weigh(10)
goose1.weigh(8)

class Ducks(Birds):
    pass

duck1 = Ducks('Кря-кря')

class Hens(Birds):
    pass

hen1 = Hens('Ко-ко')
hen2 = Hens('Кукареку')


class Cattle(Animals):
    need_for_milk = 'not milked'  # Cattle milked or not

    def milk(self):
        self.need_for_milk = 'milked'


class Goats(Cattle):
    pass

goat1 = Goats('Рога')
goat2 = Goats('Копыта')

class Cows(Cattle):
    pass

cow1 = Cows('Манька')


class Sheeps(Animals):
    need_for_shear = 'not sheared'  # Sheeps sheared or not

    def shear(self):
        self.need_for_shear = 'sheared'

sheep1 = Sheeps('Барашек')
sheep2 = Sheeps('Кудрявый')


animal_list = [goose1, goose2, duck1, hen1, hen2, goat1, goat2, cow1, sheep1, sheep2]
cattle_list = [goat1, goat2, cow1]
sheeps_list = [sheep1, sheep2]
birds_list = [goose1, goose2, duck1, hen1, hen2]


def feed_all(an_list):
    for item in an_list:
        item.feed()
        print(item.name, item.need_for_food)

feed_all(animal_list)


def milk_all(an_list):
    for item in an_list:
        item.milk()
        print(item.name, item.need_for_milk)

milk_all(cattle_list)

def shear_all(an_list):
    for item in an_list:
        item.shear()
        print(item.name, item.need_for_shear)

shear_all(sheeps_list)

def gather_eggs_all(an_list):
    for item in an_list:
        item.gather_eggs()
        print(item.name, item.need_for_eggs)

gather_eggs_all(birds_list)



# map(lambda animal_list:animal_list.feed(),all)
# print(animal_list)

# print(animal_list[0].feed())
# print(animal_list.name())

# goose1.feed()
# print(goose1.need_for_food)


print(goose1.weight + goose2.weight)


#
# class Cattle(Animals):
#     need_for_milk = 'not milked'  # Cattle milked or not
#
#     def milk(self):
#         self.need_for_milk = 'milked'
#
# goats = Cattle()
# cows = Cattle()
#
# class Sheeps(Animals):
#     need_for_shear = 'not sheared'  # Sheeps sheared or not
#
#     def shear(self):
#         self.need_for_shear = 'sheared'

# muttons = Sheeps()



# Animals.feed()
# print(geese.need_for_food)

# print(geese.need_for_food)
# geese.feed()
# print(geese.need_for_food)
#
# print(geese.need_for_eggs)
# geese.gather_eggs()
# print(geese.need_for_eggs)
#
# print(geese.weight)
# geese.weigh(10)
# print(geese.weight)
#
# print(geese.eggs)
# geese.lay_eggs(15)
# print(geese.eggs)

# print(geese.name)
# geese.givname()
# print(geese.name)

# ducks = Birds('Серый')
# print(ducks.name)

# geese.weigh(20)
#
# print(geese.weight)
# print(ducks.weight)
#
# print(geese.__dict__)
# print(ducks.__dict__)
# print(Animals.__dict__)
