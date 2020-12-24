
import pokepy
import json
import time

client = pokepy.V2Client()
json_chunk = {"abilities": []}

poke_id = 0
for i in range(233):
    poke_id += 1
    ability = client.get_ability(poke_id)

    jsonFormat = {
        "name": ability.name,
        "text_entry": "dev_fill"
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

    print(poke_id, end=" ")

    time.sleep(0.01)

#print(json.dumps(json_chunk, ensure_ascii=False))
with open("pokemon_data/ability.json", "w", encoding="utf-8") as outfile:
    json.dump(json_chunk, outfile, ensure_ascii=False, indent=4)

print("End of ability data...")