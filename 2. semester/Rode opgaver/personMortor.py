

class Motor():
    def __init__(self, motorType, direction=0, rpm=0):
        print("Initializing ", motorType)
        self.motorType = motorType
        self.direction = direction
        self.rpm = rpm

    def runMotor(self, direction, rpm):
        self.direction = direction
        self.rpm = rpm
        print("Løber moter vej", self.direction, "med", self.rpm)

servoMotor = Motor("Servo")
servoMotor.runMotor(1,100)

class Person():
    def __init__(self, firstname, lastname):
        print("initializing person: ", firstname, lastname)
        self.firstname = firstname
        self.lastname = lastname
        self.motorList = []

    def addMotor(self, motor):
        print("Adding motor to persons ownership")
        self.motorlist.append(motor)

