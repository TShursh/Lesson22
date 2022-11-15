from model.human import Human


class Converter:

    @staticmethod
    def convert_to_string(humans):
        s = "list of humans:\n"

        if not isinstance(humans, (list, tuple)):
            return "List is empty"

        for human in humans:
            if isinstance(human, Human):
                s += "\n" + str(human)

        return s