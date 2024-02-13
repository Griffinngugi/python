class person:
    def James(self):
        print("can talk")

    def Tom(self):
            print("speaks english")

# per = person()
#
# print(per.James)
#

class parrot(person):
    def garfield(self):
        print("can walk")

gar = parrot()

print(gar.James()),gar.Tom()