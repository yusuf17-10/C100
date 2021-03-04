class Car(object):
    def __init__(self,maxSpeed,modelName,paint,companyName):
        self.maxSpeed=maxSpeed
        self.modelName=modelName
        self.paint=paint
        self.companyName=companyName
    def start(self):
        print("Car Started")
    def stop(self,):
        print("Car Stopped")    
    def atAverageSpeed(self,maxSpeed):
        print("Car Is At AverageSpeed :  " +str(maxSpeed/2))

car1=Car(2,"c20","blue","KIA")

car1.start()
car1.stop()
car1.atAverageSpeed(car1.maxSpeed)

    