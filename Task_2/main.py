from passenger_car import PassengerCar
from engine import Engine
from tank import Tank


if __name__ == '__main__':
    diesel_engine = Engine()
    tank = Tank(max_volume=50, volume=5)
    mersedes = PassengerCar(fuel=20,
                            engine=diesel_engine,
                            tank=tank,
                            model='W201',
                            vin='M810323F2',
                            name='Mersedes',
                            weight=2000,
                            carrying=500,
                            production_year=1990,
                            mileage=400000
                            )
    print(mersedes)
    print('Trip to Nikolaev')
    print(f'In the tank we have {tank.volume} litters')
    mersedes.start_car()
    print('Move to the Gas stantion')
    mersedes.move(0.055, 3)
    mersedes.stop_car()
    mersedes.refueling(20)
    mersedes.start_car()
    mersedes.move(0.055, 300)
    mersedes.stop_car()
    print(f'In the tank we have {tank.volume} litters')
    print('Meleage:', mersedes.mileage)
