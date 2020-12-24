import pokepy
import json
import time

# api link: https://pokeapi.github.io/pokepy/usage/

#def getEvolutionChainFromUrl(url):
#    arr = url.split("evolution-chain/")
#    id = arr[1].replace("/", "")
#    return int(id)

def getIdFromUrl(url, split_at):
    arr = url.split(split_at)
    id = arr[1].replace("/", "")
    return int(id)

client = pokepy.V2Client()
json_chunk = {"pokemon": []}

poke_id = 0
for i in range(151):
    poke_id += 1
    pokemon = client.get_pokemon(poke_id)
    pokemon_species = client.get_pokemon_species(poke_id)
    chain_id = getIdFromUrl(pokemon_species.evolution_chain.url, "evolution-chain/")

    # JSON - Pokemon Object Data
    jsonFormat = {
        "id": pokemon.id,
        "name": pokemon.name,
        "evo_chain_id": chain_id,
        "base_experience": pokemon.base_experience,
        "height": pokemon.height / 10, # decimeters to meters
        "weight": pokemon.weight / 10, #hectograms to kilograms
        "types": [],
        "stats": [],
        "abilities": [],
        "base_happiness": pokemon_species.base_happiness,
        "capture_rate": pokemon_species.capture_rate,
        "egg_groups": [],
        "genus": pokemon_species.genera[7].genus,
        "gen_origin": pokemon_species.generation.name,
        "growth_rate": pokemon_species.growth_rate.name,
        "hatch_counter": pokemon_species.hatch_counter,
        "text_entry": None,
        "moves": []
    }

    # Pokemon Types
    for e in pokemon.types:
        tmp = {}
        tmp["name"] = e.type.name
        jsonFormat["types"].append(tmp)

    # Pokemon Stats
    for e in pokemon.stats:
        tmp = {}
        tmp["base_stat"] = e.base_stat
        tmp["effort"] = e.effort
        jsonFormat["stats"].append(tmp)

    # Pokemon Abilities
    for e in pokemon.abilities:
        tmp = {}
        tmp["id"] = getIdFromUrl(e.ability.url, "ability/")
        #tmp["name"] = e.ability.name
        tmp["is_hidden"] = e.is_hidden
        jsonFormat["abilities"].append(tmp)

    # Pokemon Egg Groups
    for e in pokemon_species.egg_groups:
        tmp = {}
        tmp["name"] = e.name
        jsonFormat["egg_groups"].append(tmp)

    # Pokemon Text Entries
    last_entry = ""
    for e in pokemon_species.flavor_text_entries:
        if e.language.name == "en":
            last_entry = e.flavor_text
    last_entry = last_entry.replace("\n", " ")
    last_entry = last_entry.replace("\u000c", " ")
    jsonFormat["text_entry"] = last_entry

    for e in pokemon.moves:
        tmp = {}
        #tmp["name"] = e.move.name -- get from move.py
        tmp["id"] = getIdFromUrl(e.move.url, "move/")
        tmp["level_learned_at"] = e.version_group_details[0].level_learned_at
        tmp["learn_method"] = e.version_group_details[0].move_learn_method.name
        jsonFormat["moves"].append(tmp)

    #print(json.dumps(jsonFormat, ensure_ascii=False))
    json_chunk["pokemon"].append(jsonFormat)

    time.sleep(0.1)

#print(json.dumps(json_chunk, ensure_ascii=False))
with open("pokemon_data/gen1.json", "w", encoding="utf-8") as outfile:
    json.dump(json_chunk, outfile, ensure_ascii=False, indent=4)

print("End of pokemon data...")