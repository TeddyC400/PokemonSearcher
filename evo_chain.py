
import pokepy
import json

client = pokepy.V2Client()
pokemon_evo = client.get_evolution_chain(144)

jsonFormat = {
    "chain": [
        {
            "name": None,
            "min_level": None,
            "held_item": None,
            "item": None,
            "known_move": None,
            "known_move_type": None,
            "location": None,
            "min_affection": None,
            "min_beauty": None,
            "min_happiness": None,
            "needs_overworld_rain": False,
            "party_species": None,
            "party_type": None,
            "relative_physical_stats": None,
            "time_of_day": "",
            "trade_species": None,
            "next_evo": []
        }
    ]
}

tmp = {}
tmp["name"] = pokemon_evo.chain.species.name

tmp_2 = {}
tmp["next_evo"] = tmp_2
# some evos need to append and not override one another like evo chain 144
for evo_1 in pokemon_evo.chain.evolves_to:
    tmp_2["name"] = evo_1.species.name
    for detail in evo_1.evolution_details:
        tmp_2["min_level"] = detail.min_level
        tmp_2["gender"] = detail.gender
        tmp_2["held_item"] = detail.held_item
        tmp_2["item"] = detail.item
        tmp_2["known_move"] = detail.known_move
        tmp_2["known_move_type"] = detail.known_move_type
        tmp_2["location"] = detail.location
        tmp_2["min_affection"] = detail.min_affection
        tmp_2["min_beauty"] = detail.min_beauty
        tmp_2["min_happiness"] = detail.min_happiness
        tmp_2["needs_overworld_rain"] = detail.needs_overworld_rain
        tmp_2["party_species"] = detail.party_species
        tmp_2["party_type"] = detail.party_type
        tmp_2["relative_physical_stats"] = detail.relative_physical_stats
        tmp_2["time_of_day"] = detail.time_of_day
        tmp_2["trade_species"] = detail.trade_species
    
    tmp_3 = {}
    tmp_2["next_evo"] = tmp_3
    for evo_2 in evo_1.evolves_to:
        tmp_3["name"] = evo_2.species.name
        for detail in evo_2.evolution_details:
            tmp_3["min_level"] = detail.min_level
            tmp_3["gender"] = detail.gender
            tmp_3["held_item"] = detail.held_item
            tmp_3["item"] = detail.item
            tmp_3["known_move"] = detail.known_move
            tmp_3["known_move_type"] = detail.known_move_type
            tmp_3["location"] = detail.location
            tmp_3["min_affection"] = detail.min_affection
            tmp_3["min_beauty"] = detail.min_beauty
            tmp_3["min_happiness"] = detail.min_happiness
            tmp_3["needs_overworld_rain"] = detail.needs_overworld_rain
            tmp_3["party_species"] = detail.party_species
            tmp_3["party_type"] = detail.party_type
            tmp_3["relative_physical_stats"] = detail.relative_physical_stats
            tmp_3["time_of_day"] = detail.time_of_day
            tmp_3["trade_species"] = detail.trade_species

print(json.dumps(tmp))

'''
# Still need to experiment with evolution since some pokemon have unique evolution properties
print("Evolution Chain:")
print(pokemon_evo.chain.species.name)
for evo_1 in pokemon_evo.chain.evolves_to:
    for detail in evo_1.evolution_details:
        print(detail.min_level)
        print(detail.gender)
        print(detail.held_item)
    print(evo_1.species.name)

    for evo_2 in evo_1.evolves_to:
        for detail in evo_2.evolution_details:
            print(detail.min_level)
        print(evo_2.species.name)
    #print(evo.evolution_details)
'''