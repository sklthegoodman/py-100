import pygal.maps.world as world

def get_country_code(name):
    for key in world.COUNTRIES:
        if(world.COUNTRIES[key] == name):
            return key
    return None

