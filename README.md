# Food Status Effects Data Pack

> Adds relevancy and status buffs to obscure foods

## Introduction

There are 40-or-so items that you can consume for food in Minecraft. Yet, after Day 5, we only consume Cooked Beef exclusively.

There is such a variety of food, so many different things to explore the world and build farms for. Yet, 35-or-so of these foods would be considered junk, and would probably either be stashed in a chest, never to see the light of day, or perhaps would be thrown on the ground, waiting to despawn forever. I've NEVER seen or crafted a Rabbit Stew... ever. Have you?

There are also so many thematic and interesting status effects that foods can give, that opens so many avenues for gameplay!

## Design Principles

Foods can be an early-game option for utility and convenience, but must not be a late-game substitute for potions.

Common consumables (only Cooked Beef, really) are left untouched. Since everyone only eats Cooked Beef, sometimes Golden Apples, this pack would not be an interference for like, 90% of players' playstyles. Then, if people don't like this tweak, they can just ignore it!

See [data.yml](data.yml) for each tweak and the reasoning in the comments.

## Customization and Contribution

 This pack uses [beet](https://github.com/mcbeet/beet) as a development kit. You could edit [data.yml](data.yml) and recompile to get a pack with your own customized food status effects!

 ```sh
beet -p beet-custom.yml build
 ```

 It will create a .zip file in the releases directory named "food_status_effects_(custom)_data_pack.zip". Use this as your custom data pack.

## Examples

Here are some interesting status effects that foods can give with this data pack:

```yaml
# Players never visit the ocean floor because of the hassle of swimming up when they lose their air bubbles, or they just bring a bunch of doors for air pockets.
# Dried Kelp are quick snacks that grant one hunger point.
# What if they grant a small duration of water breathing??
# Players can just munch on Dried Kelp to keep their air replenished, keeping track of a second timer.
# Players wouldn't need to wait for late-game brewing just to get water breathing potions; yet Dried Kelp doesn't replace it, because a passive 8:00 minutes is way better than having to eat every 10 seconds.
# I've also added a bit of hunger as I've found that if players get fully fed when they're deep underwater, they can't eat more seaweed to replenish their water breathing, and then get stuck and drown.
# Anyways, seaweed would be more of a utility item.
dried_kelp:
  - [water_breathing, 10, 1]
  - [hunger, 2, 1]

# No one ever eats spider eyes. They only give one hunger point and even give you poison.
# Since they are eyes, what if they gave you temporary night vision?
# In 10 seconds, the night vision would be flashing and disorientating, but it would be a good early-game option when players are stuck in the dark.
spider_eye:
  - [night_vision, 10, 1]

# WHAT A MISSED OPPORTUNITY
# Simple, glow berries give you the glowing effect. Ugh. Literally the first reason why I made this pack.
# Duration is 10 seconds, matches up with the duration of glowing from spectral arrows
# They can also give some regeneration, to match up with sweet berries.
glow_berries:
  - [glowing, 10, 1]
  - [regeneration, 5, 1]

# Chorus Fruit teleport you, thematically alike to Endermen
# It's hard to know where Endermen are after they teleport around
# What if players get quick invisibility after they teleport. Players get a head start in escaping or manoeuvring to a better position.
# Right now, nobody really uses them anyways, because the few seconds of chomping time is more trouble than an uncertain 3 block's teleportation is worth.
# Besides, there are some particle effects where they land after teleporting, so it's not overpowered.
# And. Chorus fruit are an end-game item, so something powerful like invisibility is apt.
chorus_fruit:
  - [invisibility, 3, 1]
```
