class PlotData:
    def __init__(self, a, min_x, max_x, number_of_dots):
        self.a = a
        self.min_x = min_x
        self.max_x = max_x
        self.numer_of_dots = number_of_dots

    def get_a(self):
        return self.a

    def get_min_x(self):
        return self.min_x

    def get_max_x(self):
        return self.max_x

    def get_number_of_dots(self):
        return self.numer_of_dots
