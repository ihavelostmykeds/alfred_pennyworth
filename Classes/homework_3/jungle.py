from __future__ import annotations, print_function

from typing import Dict
import uuid
import random
import abc
import sys


class Animal(abc.ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid.uuid4())
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abc.abstractmethod
    def eat(self, jungle: Jungle):
        pass

    def check_power(self):
        if self.current_power <= 0:
            return False
        return True

    def check_max_power(self):
        if self.current_power > self.max_power:
            self.current_power = self.max_power


class Predator(Animal):

    def eat(self, jungle: Jungle):

        prey = random.choice(list(jungle.animals.values()))
        if prey.check_power():
            if self.id == prey.id:
                self.current_power -= 0.3 * self.current_power
            elif self.speed > prey.speed and self.current_power > prey.current_power:
                self.current_power += 0.4 * self.max_power
                jungle.remove_animal(prey)
                self.check_max_power()
            else:
                self.current_power -= 0.3 * self.max_power
                prey.current_power -= 0.3 * prey.max_power
                if not self.check_power():
                    jungle.remove_animal(self)
                if not prey.check_power():
                    jungle.remove_animal(prey)

        else:
            jungle.remove_animal(prey)


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.check_power():
            self.current_power += 0.4 * self.max_power
            self.check_max_power()
        else:
            jungle.remove_animal(self)


class Jungle:

    def __iter__(self):
        return self.animals.values().__iter__()

    def __init__(self):
        self.animals: Dict[str, Animal] = dict()

    def add_animal(self, animal: Animal):
        self.animals[(animal.id)] = animal

    def remove_animal(self, animal: Animal):
        self.animals.pop(animal.id)


def animal_generator():
    any_animal = [Predator, Herbivorous]
    number_of_iterations = 10
    for i in range(number_of_iterations):
        power, speed = random.randint(20, 100), random.randint(20, 100)
        yield any_animal[random.randint(0, 1)](power, speed)  # any_animal = Predator() or Herbavirous()


if __name__ == "__main__":
    jungle = Jungle()
    for animal in animal_generator():
        jungle.add_animal(animal)

    while jungle.animals:

        print('--------------HERE COMES THE DINNER--------------')
        for animal in jungle.animals.values():
            print(
                f"CLASS:{animal.__class__.__name__:11} ID:{animal.id} POWER: {str(animal.current_power):.4} SPEED {str(animal.speed):.3}")
        predator_alive = bool([a for a in jungle.animals.values() if isinstance(a, Predator)])
        if predator_alive and len(jungle.animals) > 1:
            hunter = random.choice(list(jungle.animals.values()))
            if hunter.check_power():
                hunter.eat(jungle)
            else:
                jungle.remove_animal(hunter)
        else:
            print('DINNER FINISHED')
            print()
            sys.exit()
