
import pokepy
import json

client = pokepy.V2Client()
move = client.get_move(13)

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

print (json.dumps(jsonFormat, ensure_ascii=False))