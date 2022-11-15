
from model.analyst import Analyst
from util.creator import HumanCreator
from util.converter import Converter


def main():
    ls = HumanCreator.create(5)
    print(Converter.convert_to_string(ls))

    count_adults = Analyst.count_adults(ls)
    count_alive = Analyst.count_alive(ls)

    print(f"Count is adults: {count_adults}")
    print(f"Count is alive: {count_alive}")


if __name__ == '__main__':
    main()
