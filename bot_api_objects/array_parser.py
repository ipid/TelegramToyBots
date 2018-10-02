__all__ = ('array_of', 'array_of_array_of')

def array_of(cls, value):
    return [cls(x) for x in value]

def array_of_array_of(cls, value):
    return [[cls(y) for y in x] for x in value]