
class Car(object):
    
    def __init__(self, name=None, model=None, vehicle_type=None):

        self.speed = 0

        if name is not None and (name == 'Porshe' or name == 'Koenigsegg'):
            self.num_of_doors = 2
        elif name is not None and (name != 'Porshe' or name != 'Koenigsegg'):
            self.num_of_doors = 4
        else:
            pass

        if name is None:
            self.name = 'General'
            self.num_of_doors = 4
        else:
            self.name = name

        if model is None:
            self.model = 'GM'
        else:
            self.model = model

        if vehicle_type is None:
            self.vehicle_type = 'saloon'
        else:
            self.vehicle_type = vehicle_type

        if vehicle_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4



    def is_saloon(self):

        if self.vehicle_type == 'saloon':
            return True
        else:
            return False

    def drive(self,moving_speed ):
        if self.vehicle_type == 'saloon':
           self.speed = 10 ** moving_speed
        else:
           self.speed = 77
