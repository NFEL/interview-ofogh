import json

from django.contrib.auth import get_user_model
from cars.models import Car
from road.models import Road, TollStation

User = get_user_model()


def populate(given_args: dict):
    verbose = given_args.get('verbose') or False

    print('Working on Roads data')
    with open(given_args.get('roads')) as f:
        roads_data = json.load(f)
        print(f'Found {len(roads_data)} Records ...')
        inserted_record = 0
        for road_data in roads_data:
            try:
                if verbose:
                    print(road_data)
                road_obj = Road.objects.update_or_create(**road_data)
                if verbose:
                    print(f'Created {road_obj}')
                inserted_record += 1
            except Exception as e:
                print(f'Following Error {e} at data{road_data}')
        print(f'Inserted records {inserted_record} to DB')

    print('Working on tollStations data')
    with open(given_args.get("tollStations")) as f:
        toll_stations_data = json.load(f)
        print(f'Found {len(toll_stations_data)} Records ...')
        inserted_record = 0

        for toll_station_data in toll_stations_data:
            try:
                if verbose:
                    print(toll_station_data)
                toll_station_obj = TollStation.objects.update_or_create(
                    **toll_station_data)
                if verbose:
                    print(f'Created {toll_station_obj}')
                inserted_record += 1
            except Exception as e:
                print(f'Following Error {e} at data{toll_station_data}')
        print(f'Inserted records {inserted_record} to DB')

    print('Working on owners data')
    with open(given_args.get('owners')) as f:
        owners_data = json.load(f)
        print(f'Found {len(owners_data)} Records ...')
        inserted_record = 0
        for owner_data in owners_data:
            try:
                cars=[]
                for car_data in owner_data.get('ownerCar'):
                    _car_obj, _=Car.objects.get_or_create(**car_data)
                    _car_obj.save()
                    cars.append(_car_obj.id)
                try:
                    user: User=User.objects.get(
                        national_code = owner_data.get('national_code'))
                except User.DoesNotExist:
                    user=User.objects.create_user(
                        username = owner_data.get('name'),
                        national_code = owner_data.get('national_code'),
                        age = owner_data.get('age'),
                        total_toll_paid = owner_data.get('total_toll_paid'),
                        password = str(owner_data.get('national_code'))
                        )


                user.cars.set(cars)
                user.save()
                if verbose:
                    print(f'Created {owner_data}')

                inserted_record += 1
            except Exception as e:
                print(f'Following Error {e} at data{owner_data}')
        print(f'Inserted records {inserted_record} to DB')
