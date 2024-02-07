# my_func.py
def trip_price(dist_miles, mpg, price, loc_from, loc_to):
    total_price = dist_miles * price / mpg
    print(f'Un viaje de {loc_from} a {loc_to} costará ${total_price}')

trip_price(dist_miles=409, loc_from='A', loc_to='B', mpg=35, price=5.1)