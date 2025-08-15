# When to use Class method and when to use static method ?

class Example:
    @staticmethod
    def utility_function():
        # Use when logic is related to the class, 
        # but doesn't need 'self' or 'cls'
        pass

    @classmethod
    def from_string(cls, data):
        # Use when you need to access/modify class variables
        # or create instances using the class itself
        pass
