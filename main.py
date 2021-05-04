class Car(object):
  """
    blueprint for car
  """

  def __init__(self, model, color, company, speed_limit):
    self.color = color
    self.company = company
    self.speed_limit = speed_limit
    self.model = model

  def start(self):
    print("(-: car has been started")

  def stop(self):
    print(")-: can has been stopped")

  def accelarate(self):
    print("accelarating...")
    "accelarator functionality here"

  def change_gear(self, gear_type):
    print("gear changed")
    " gear related functionality here"


audi = Car("A6", "red", "audi", 80)

print(audi.stop())
