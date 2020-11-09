import pokepy
import json

def getEvolutionChainFromUrl(url):
    arr = url.split("evolution-chain/")
    chainId = arr[1].replace("/", "")
    return int(chainId)

poke_id = 1
client = pokepy.V2Client()
pokemon = client.get_pokemon(poke_id)
pokemon_species = client.get_pokemon_species(poke_id)
chain_id = getEvolutionChainFromUrl(pokemon_species.evolution_chain.url)
pokemon_evo = client.get_evolution_chain(chain_id)

# JSON - Pokemon Object Data
jsonFormat = {
    "id": pokemon.id,
    "evo_chain_id": chain_id,
    "name": pokemon.name,
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
    "text_entry": "dev_fill",
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
    tmp["name"] = e.stat.name
    tmp["base_stat"] = e.base_stat
    tmp["effort"] = e.effort
    jsonFormat["stats"].append(tmp)

# Pokemon Abilities
for e in pokemon.abilities:
    tmp = {}
    tmp["name"] = e.ability.name
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
    tmp["name"] = e.move.name
    tmp["level_learned_at"] = e.version_group_details[0].level_learned_at
    tmp["learn_method"] = e.version_group_details[0].move_learn_method.name
    jsonFormat["moves"].append(tmp)

print(json.dumps(jsonFormat))

'''
print(pokemon.id)
print(pokemon.name)
print(pokemon.base_experience)
print(pokemon.height / 10) # decimeters to meters
print(pokemon.weight / 10) # hectogram to kilogram
print(pokemon.species.name)

print("Pokemon Abilities:")
for a in pokemon.abilities:
    print("Is Hidden: {}".format(a.is_hidden))
    print(a.ability.name)

#print("Pokemon Moves:")
#Pokemon moves works but long as fuck
#for m in pokemon.moves:
#    print(m.move.name)
#    print(m.version_group_details[0].level_learned_at)
#    print(m.version_group_details[0].move_learn_method.name)

print("Pokemon Stats:")
for s in pokemon.stats:
    print(s.base_stat)
    print(s.effort) # one or two stats have this property
    print(s.stat.name)

print("Pokemon Types:")
for t in pokemon.types:
    print(t.type.name)

print("Pokemon Species:")
print(pokemon_species.base_happiness)
print(pokemon_species.capture_rate)
for e in pokemon_species.egg_groups:
    print(e.name)

prev_updated = "old"
updated = ""
for f in pokemon_species.flavor_text_entries:
    if f.language.name == "en":
        updated = f.flavor_text.replace("\n", " ")
        updated = updated.replace("\u000c", " ")
        if (not(updated == prev_updated)):
            prev_updated = updated
            print(updated)
        #if poke_id < 722:
        #    print("--> {}".format(f))
        #    if f.version.name == "omega-ruby" or f.version.name == "alpha-sapphire":
                # any pokemon that existed up to omega-ruby/alpha-sapphire appears here
        #        print(f.flavor_text)
        #elif poke_id >= 722 and poke_id < 810:
        #    if f.version.name == "sun" or f.version.name == "moon":
                # any pokemon that was created during sun and moon are here
        #        print(f.flavor_text)
        #elif poke_id >= 810:
        #    if f.version.name == "sword" or f.version.name == "shield":
                # any pokemon that was created during sword and shield are hre
        #       print(f.flavor_text)

print(pokemon_species.genera[7].genus)
print(pokemon_species.generation.name)
print(pokemon_species.growth_rate.name)
print(pokemon_species.hatch_counter)
'''

'''
# Still need to experiment with evolution since some pokemon have unique evolution properties
print("Evolution Chain:")
print(pokemon_evo.chain.species.name)
for evo_1 in pokemon_evo.chain.evolves_to:
    for detail in evo_1.evolution_details:
        print(detail.min_level)
    print(evo_1.species.name)

    for evo_2 in evo_1.evolves_to:
        for detail in evo_2.evolution_details:
            print(detail.min_level)
        print(evo_2.species.name)
    #print(evo.evolution_details)
'''