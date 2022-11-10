import platform, struct

print(platform.architecture())
print(platform.architecture()[0])

print(struct.calcsize("P") * 8)
