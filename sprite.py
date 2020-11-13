
import pokepy
import json

for poke_id in range(3):
    poke_id += 1
    pokemon_form = client.get_pokemon_form(poke_id)

    tmp["front_default"] = pokemon_form.sprites.front_default
    tmp["front_shiny"] = pokemon_form.sprites.front_shiny
    #tmp["back_default"] = pokemon_form.sprites.back_default
    #tmp["back_shiny"] = pokemon_form.sprites.back_shiny