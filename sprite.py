
import pokepy
import json
import urllib.request
import time

# How to download images off of website URLs
# https://stackoverflow.com/questions/8286352/how-to-save-an-image-locally-using-python-whose-url-address-i-already-know

# How to fix SSL certification and be able to download the images
# https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error

client = pokepy.V2Client()

gen = 1
poke_id = 720
for i in range(1):
    poke_id += 1
    pokemon_form = client.get_pokemon_form(poke_id)

    jsonFormat = {
        "front_default": pokemon_form.sprites.front_default,
        "front_shiny": pokemon_form.sprites.front_shiny
    }

    if poke_id <= 151:
        gen = 1
    elif poke_id >= 152 and poke_id <= 251:
        gen = 2
    elif poke_id >= 252 and poke_id <= 386:
        gen = 3
    elif poke_id >= 387 and poke_id <= 493:
        gen = 4
    elif poke_id >= 494 and poke_id <= 649:
        gen = 5
    elif poke_id >= 650 and poke_id <= 721:
        gen = 6

    urllib.request.urlretrieve(jsonFormat["front_default"], "pokemon_images/gen{}/default/{}.png".format(gen, poke_id))
    urllib.request.urlretrieve(jsonFormat["front_shiny"], "pokemon_images/gen{}/shiny/{}.png".format(gen, poke_id))

    print(poke_id)

    time.sleep(0.05)

    #front_default pokemon_form.sprites.front_default
    #front_shiny = pokemon_form.sprites.front_shiny
    #tmp["back_default"] = pokemon_form.sprites.back_default
    #tmp["back_shiny"] = pokemon_form.sprites.back_shiny
    #print(json.dumps(jsonFormat))

print("End of image downloading...")