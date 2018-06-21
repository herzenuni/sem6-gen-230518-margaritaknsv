#генерирование UUID
import uuid

def uuid_generator():
    g1 = uuid.uuid4()
    g2 = uuid.uuid4().int
    print(g1)
    print(g2)

uuid_generator()