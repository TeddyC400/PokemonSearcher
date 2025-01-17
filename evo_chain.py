
import pokepy
import json
import time

client = pokepy.V2Client()

json_chunk = {"evolution_chains": []}

poke_id = 0
for i in range(78):
    poke_id += 1
    pokemon_evo = client.get_evolution_chain(poke_id)

    tmp_1 = {}
    tmp_2 = {"evos": []}
    tmp_3 = {"evos": []}

    tmp_1["name"] = pokemon_evo.chain.species.name
    # some evos need to append and not override one another like evo chain 144
    tmp_1["next_evo"] = tmp_2
    for evo_1 in pokemon_evo.chain.evolves_to:
        tmp = {}
        tmp["name"] = evo_1.species.name

        tmp["min_level"] = evo_1.evolution_details[0].min_level
        tmp["trade_species"] = evo_1.evolution_details[0].trade_species

        tmp_2["evos"].append(tmp)

        tmp_2["next_evo"] = tmp_3
        for evo_2 in evo_1.evolves_to:
            tmp = {}
            tmp["name"] = evo_2.species.name

            tmp["min_level"] = evo_2.evolution_details[0].min_level
            tmp["trade_species"] = evo_2.evolution_details[0].trade_species

            tmp_3["evos"].append(tmp)

    #print(tmp_1)
    #print(json.dumps(tmp_1))
    json_chunk["evolution_chains"].append(tmp_1)

    time.sleep(0.01)

#print (json.dumps(json_chunk, ensure_ascii=False))
with open("pokemon_data/evo_chain.json", "w", encoding="utf-8") as outfile:
    json.dump(json_chunk, outfile, ensure_ascii=False, indent=4)

print("End of evo chain data...")