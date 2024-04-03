# 1)
object_size = 10
if object_size > 5:
    print("We need to keep an eye on this object")
else:
    print("object poses no threat")


# 2)
object_size = 10
proximity = 9000
if object_size > 5 and proximity < 1000:
    print("Evasive maneuvers required")
else:
    print("Object poses no threat")