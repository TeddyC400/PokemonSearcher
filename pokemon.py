import pokepy
import json

client = pokepy.V2Client()
pokemon = client.get_pokemon(14)
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
print()
print()
print()
print()
#print(test[0].stat.name)