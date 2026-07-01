class ElectronicDevice:
    _protected=79
    __private=69
    def __init__(self, dName):
        self.deviceName = dName

    def printDetails(self):
        print("Device Name: ", self.deviceName)

    def isElectronic(self):
        return "all are electronic devices"


class PocketDevices(ElectronicDevice):
    current = 3

    def music(self):
        return "I can play music"


class Phone(PocketDevices):

    def cam(self):
        return "I can click photos"

    @staticmethod
    def games():
        return "I can play video games too!"

s25ultra = Phone("Samsung Galaxy S25 Ultra")
print(s25ultra.cam())
print(s25ultra.games())
print(s25ultra.isElectronic())
print(s25ultra.printDetails())
print(s25ultra.current)
e1=ElectronicDevice("Nitro-AN515-57")
print("protected variable:",e1._protected)
print("private variable:",e1._ElectronicDevice__private)