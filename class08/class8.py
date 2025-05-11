from collections.abc import Iterable
def my_function(start:int, end:int, step:int = 1)->Iterable[int]:
    for i in range(start,end+1,step):
        yield i

a: Iterable[int] = my_function(1,10)
print(next(iter(a)))
print(next(iter(a)))
print(next(iter(a)))
print(list(a))

def make_car(manufacturer:str,model:str,**car_infos:str):
    car: dict[str,str] = {
        "manufacturer": manufacturer,
        "model" : model
        }
    for key , value in car_infos.items():
        car[key] = value
    return car

car = make_car("Hyndayi Civic","Altas", Color="Black", Year="2021")
print(car)