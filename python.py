import random
import more_itertools as mit

def Car(fuel,health):
    if fuel > 100:
        print("The maximum fuel limit for a car is 100")
    if health > 100:
        print("The maximum health limit for a car is 100")
    road = random.randint(15,50)
    car = "🚗"
    def carReplacer(index, nofail=False):
        if not nofail and index not in range(len(full_road)):
            raise ValueError("Index outside given string") # https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index/41753038
        if index < 0:
            return car + full_road
        if index > len(full_road): 
            return full_road + car
        return full_road[:index] + car + full_road[index + 1:]
    bump_icon = "n"
    road_icon = "_"
    full_road = "".join([bump_icon if not random.randint(0, 1) else road_icon for x in range(1, road)])
    car_fuel = 100 - (full_road.count(bump_icon) * 1)
    car_health = 100 - (full_road.count(bump_icon) * 1.25)
    car_fuel = car_fuel - (full_road.count(road_icon) * 0.1)
    car_health = car_health - (full_road.count(road_icon) * 0.125)
    needed_fuel = 100 - car_fuel
    needed_health = 100 - car_health
    print("Current fuel: ", fuel)
    print("Current health: ", health)
    print("Needed fuel: ", needed_fuel)
    print("Needed health: ", needed_health)
    if fuel > needed_fuel and health >= needed_health:
        conclusion = "We won without dies!"
        print(carReplacer(len(full_road)-1))
        print("Car fuel: ", car_fuel)
        print("Car health: ", car_health)
    elif fuel > needed_fuel and health <= needed_health:
        conclusion = "Car is dead"
        print(carReplacer(list(mit.locate(list(full_road), lambda x: x == 'n'))[int(health/full_road.count(bump_icon))]))
    elif fuel <= needed_fuel and health >= needed_health:
        conclusion = "Fuel is empty!"
        print(carReplacer(list(mit.locate(list(full_road), lambda x: x == 'n'))[int(fuel/full_road.count(bump_icon))]))
    elif fuel <= needed_fuel and health <= needed_health:
        conclusion = "We are dead"
        print(carReplacer(0)+ "_")

    
    print(conclusion)
Car(1,60)

