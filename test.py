from models.base_model import BaseModel

instance = type("BaseModel", (), {})()

print(instance.id)
