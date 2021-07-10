from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return list([(c.name, c.value) for c in cls])

    @classmethod
    def value_choices(cls) -> tuple:
        return tuple(c.name for c in cls)


class Currency(ChoiceEnum):
    USD = 'USD'
    CAD = 'CAD'
    UAH = 'UAH'
