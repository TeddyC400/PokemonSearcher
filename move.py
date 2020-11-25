
import pokepy
import json

client = pokepy.V2Client()
json_chunk = {"moves": []}

poke_id = 0
for poke_id in range(3):
    poke_id += 1
    move = client.get_move(poke_id)

    jsonFormat = {
        "name": move.name,
        "type": move.type.name,
        "accuracy": move.accuracy,
        "power": move.power,
        "pp": move.pp,
        "priority": move.priority,
        "target": move.target.name,
        "damage_class": move.damage_class.name,
        "effect_entry": move.effect_entries[0].effect.replace("\n", " "),
        "text_entry": "dev_fill",
        "stat_changes": [],
        "gen_origin": move.generation.name

    }

    # Text Entry
    last_entry = ""
    for e in move.flavor_text_entries:
        if e.language.name == "en":
            last_entry = e.flavor_text
    last_entry = last_entry.replace("\n", " ")
    last_entry = last_entry.replace("\u000c", " ")
    jsonFormat["text_entry"] = last_entry

    # Stat Changes
    for e in move.stat_changes:
        tmp = {}
        tmp["stat"] = e.stat.name
        tmp["change"] = e.change
        jsonFormat["stat_changes"].append(tmp)

    json_chunk["moves"].append(jsonFormat)

#print (json.dumps(json_chunk, ensure_ascii=False))
with open("move.json", "w", encoding="utf-8") as outfile:
    json.dump(json_chunk, outfile, ensure_ascii=False, indent=4)