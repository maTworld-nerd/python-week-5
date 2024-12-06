# Base class
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Derived classes
class Dog(Animal):
    def move(self):
        return "The dog runs on four legs. 🐕"

class Bird(Animal):
    def move(self):
        return "The bird flies gracefully in the sky. 🦅"

class Fish(Animal):
    def move(self):
        return "The fish swims through the water. 🐟"

# Testing polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    print(animal.move())
