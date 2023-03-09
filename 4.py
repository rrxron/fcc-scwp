class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50: return "Too big for picture."
        strReturn = ""
        for _ in range(self.height):
            for _ in range(self.width):
                strReturn += "*"
            strReturn += "\n"
        return strReturn

    def get_amount_inside(self, shape):
        times = 0
        try:
            times = \
                int(self.width / shape.width) * int(self.height / shape.height)
        except:
            return 0
        return times

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)
        super().set_height(side)
        super().set_width(side)
        self.side = side

    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)
        self.side = side

    def set_width(self, width):
        super().set_width(width)
        self.side = width

    def set_height(self, height):
        super().set_height(height)
        self.side = height

    def __str__(self):
        return f"Square(side={self.side})"
