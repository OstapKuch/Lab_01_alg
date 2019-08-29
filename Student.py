class Student:
  def __init__(self, name_surname, rating, growth):
    self.name_surname = name_surname
    self.rating = rating
    self.growth = growth
  def __repr__(self):
    return str(self.__dict__)
