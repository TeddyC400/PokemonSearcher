
import pokepy
import json

client = pokepy.V2Client()
ability = client.get_ability(1)

jsonFormat = {
    "name": ability.name,
    "effect_change": ability.effect_changes[0][1].effect,
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

print (json.dumps(jsonFormat, ensure_ascii=False))