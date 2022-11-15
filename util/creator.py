import random
import string

from model.human import Human


class HumanCreator:
    @staticmethod
    def create(size):
        NAMES = ("Alex", "Kate", "Mary", "Benjamin", "Bernard", "Blake", "Brandon", "Brian", "Bruce", "Bryan",
                 "Gloria", "Gabriella", "Gabrielle", "Gladys", "Grace")
        ALFABET = string.ascii_uppercase
        MAX_AGE = 130
        MIN_AGE = 0
        ls = []

        for _ in range(size):
            firstname = random.choice(NAMES)
            surname = ALFABET[random.randrange(len(ALFABET))]
            age = random.randint(MIN_AGE, MAX_AGE)
            alive = bool(random.getrandbits(1))
            human = Human(firstname, surname, age, alive)
            ls.append(human)

        return ls
