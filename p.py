class Point():
    def __init__(self, x = 0, y = 0):
        # Constructor to initialize the Point object with x and y coordinates
        self.__x = x
        self.__y = y

    def Get_x(self):
        # Getter method to retrieve the x-coordinate of the Point
        return self.__x

    def Get_y(self):
        # Getter method to retrieve the y-coordinate of the Point
        return self.__y

    def Set_x(self, x):
        # Setter method to set the x-coordinate of the Point
        self.__x = x

    def Set_y(self, y):
        # Setter method to set the y-coordinate of the Point
        self.__y = y

    def Distance(self, point1):
        # Method to calculate the Euclidean distance between two points
        d = ((point1.Get_x() - self.Get_x()) ** 2 + (point1.Get_y() - self.Get_y()) ** 2) ** 0.5
        return d

    def Norm(self):
        # Method to cGlculate the Euclidean norm of the Point
        n = (self.__x ** 2 + self.__y ** 2) ** 0.5
        return n

