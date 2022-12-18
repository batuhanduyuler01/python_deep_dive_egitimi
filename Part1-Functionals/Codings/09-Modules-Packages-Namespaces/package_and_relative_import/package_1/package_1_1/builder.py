from package_2.helper import Helper

Helper.speak = lambda x : print(f"Hello with {x}")

class Builder:
    def __init__(self):
        self.helper = Helper()
        self.helper.speak()
        
