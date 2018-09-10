class ProgrammingLanguage:
    def __init__(self, name, is_dynamic, is_reflection, year):
        self.name = name
        self.is_dynamic = is_dynamic
        self.is_reflection = is_reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.is_dynamic,
                                                                           self.is_reflection, self.year)
