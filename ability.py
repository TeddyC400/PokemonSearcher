
import pokepy
import json

client = pokepy.V2Client()
json_chunk = {"abilities": []}

for poke_id in range(3):
    poke_id += 1
    ability = client.get_ability(poke_id)

    jsonFormat = {
        "name": ability.name,
        "effect_entry": ability.effect_entries[1].effect.replace("\n", " "),
        "text_entry": "devi_fill"
    }

    # Text Entry
    last_entry = ""
    for e in ability.flavor_text_entries:
        if e.language.name == "en":
            last_entry = e.flavor_text
    last_entry = last_entry.replace("\n", " ")
    last_entry = last_entry.replace("\u000c", " ")
    jsonFormat["text_entry"] = last_entry

    json_chunk["abilities"].append(jsonFormat)

print(json.dumps(json_chunk, ensure_ascii=False))