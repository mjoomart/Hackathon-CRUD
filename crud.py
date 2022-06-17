from settings import settings
import requests
import json


body_type = ('sedan', 'coupe', 'CUV', 'wagon', 'pickup', 'minvan', 'hatchback')

class Car:

    def list_records(self):

        print('Listing records\n')

        URL = '?maxRecords=3&view=Grid%20view'
        req = requests.get(url=settings.get_url()+ URL, headers=settings.HEADERS)
        return req.json()

    def retrieve_a_record(self, id_):
        req = requests.get(settings.get_url()+ f'/{id_}', headers=settings.HEADERS)
        return req.json()

    def create_records(self):
        
        print('Create record:\n')

        obj = {'fields': {'brand': input('Car brand: '),
         'model': input('brand model: '),
          'year': input('Year: '),
           'volume': input('volume: '),
            'color': input('Color: '),
            'type': input(f'Select body Type {body_type}: '),
            'mileage': input('mileage: '),
            'price': input('price: ')}, 'typecast': True}
        obj = json.dumps(obj)
        req = requests.post(settings.get_url(), headers=settings.HEADERS, data=obj)
        return req.json()

    def update_records(self, id_):
        
        print('Update record:\n')

        data = {'records': [{'id': id_, 'fields': {'brand': input('Car brand: '),
         'model': input('brand model: '),
          'year': int(input('Year: ')),
           'volume': float(input('volume: ')),
            'color': input('Color: '),
            'type': input(f'Select body Type {body_type}: '),
            'mileage': int(input('mileage: ')),
            'price': float(input('price: '))}}]}
        
        data = json.dumps(data)
        req = requests.patch(settings.get_url(), headers=settings.HEADERS, data=data)
        return req.json()
    
    def delete_records(self, id_):
        
        print('Delete record:\n')
        req = requests.delete(settings.get_url() + f'/{id_}', headers={'Authorization': settings.TOKEN}, data=f'records[]={id_}')
        return req.json()
    

car = Car()

# print(car.list_records())
# print(car.retrieve_a_record('recFdMhxQYCGHCbQG'))
# print(car.create_records())
# print(car.update_records('rec5QG43LaFAp7Uhm'))
print(car.delete_records('rec5QG43LaFAp7Uhm'))
