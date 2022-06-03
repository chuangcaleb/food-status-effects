"""Plugin to generate all food status effects"""

from beet import Context, Function, Advancement
import yaml


def generate_function(food, effect_list):

    function_body = [f"advancement revoke @s only cchesed:foodstatus/{food}"]

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

    with open('data.yml', 'r') as file:
        data = yaml.safe_load(file)
        # print(data)

        for food, effect_list in data.items():
            # for food, effect_list in data.FOOD_STATUS_CONFIG.items():

            filename = f"{ctx.project_author}:foodstatus"

            ctx.data[f"{filename}/{food}"] = Function(
                generate_function(food, effect_list)
            )

            ctx.data[f"{filename}/{food}"] = Advancement(
                ctx.template.render(
                    "consume_food.json",
                    food=food
                )
            )
