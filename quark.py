# CLI task tracking program created by Natsil

class Car():
  def __init__(self, brand, model, color):
    self.brand = brand
    self.model = model
    self.color = color

class Task():
    def __init__(self, id, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt