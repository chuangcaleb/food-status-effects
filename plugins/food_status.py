"""Plugin to generate all food status effects"""

from beet import Context, Function, Advancement
import yaml

SCOREBOARD_FOODS = {
    "cake": "minecraft.custom:minecraft.eat_cake_slice",
    "milk_bucket": "minecraft.used:minecraft.milk_bucket"
}


def generate_function(food, effect_list):

    if food in SCOREBOARD_FOODS.keys():
        function_body = [f"scoreboard players set @s cc.fs.{food} 0"]
    else:
        function_body = [
            f"advancement revoke @s only food_status_effects:{food}"]

    for effect in effect_list:
        # for effect in effect_list:
        function_body.append(
            f"effect give @s minecraft:{effect[0]} {effect[1]} {int(effect[2])-1}"
            # f"effect give @s minecraft:{effect['id']} {effect['dur']} {effect['amp']-1}"
        )
    return function_body


def beet_default(ctx: Context):
    ctx.require(generate_files)


def generate_files(ctx: Context):

    ctx.generate(
        "init",
        Function(
            [f"scoreboard objectives add cc.fs.{food} {SCOREBOARD_FOODS[food]}"
             for food in SCOREBOARD_FOODS],
            prepend_tags=["minecraft:load"]
        )
    )
    ctx.generate(
        "uninstall",
        Function(
            [f"scoreboard objectives remove cc.fs.{food}"
             for food in SCOREBOARD_FOODS],
        )
    )

    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)

        tick_check = []

        for food, effect_list in data.items():

            ctx.generate(
                f"food_effect/{food}",
                Function(
                    generate_function(food, effect_list),
                )
            )

            if food in SCOREBOARD_FOODS:
                tick_check.append(
                    f"execute as @a if score @s cc.fs.{food} matches 1.. run function food_status_effects:food_effect/{food}")
            else:
                ctx.generate(
                    food,
                    Advancement(ctx.template.render(
                        "consume_food.json",
                        food=food
                    ))
                )

        if tick_check:
            ctx.generate(
                f"tick",
                Function(
                    tick_check,
                    prepend_tags=["minecraft:tick"]
                ),
            )
