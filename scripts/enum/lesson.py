import enum


class Status(enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    RUNNING = 3


print(Status.ACTIVE)
print(repr(Status.ACTIVE))
print(Status.ACTIVE.name)
print(Status.ACTIVE.value)

for s in Status:
    print(s)

print(Status(1))
