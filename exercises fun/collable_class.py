class Adam:
    def __init__(self):
        print("Instance Created")

    def __call__(self):
        print("Instance is called via special method")

a = Adam()

a()