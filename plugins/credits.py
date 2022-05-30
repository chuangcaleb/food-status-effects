"""Plugin that generates a function to print credits"""


__all__ = [
    "CreditsOptions",
    "credits",
]


from beet import Context, Function, configurable
from pydantic import BaseModel


class CreditsOptions(BaseModel):
    link: str = ""


def beet_default(ctx: Context):
    # print(ctx)
    ctx.require(credits)


@configurable(validator=CreditsOptions)
def credits(ctx: Context, opts: CreditsOptions):
    # ctx.generate("credits", create_credits_function(opts.link))
    credits_func_name = ctx.project_author + ":credits"
    ctx.data[credits_func_name] = create_credits_function(opts.link)


def create_credits_function(link: str):
    return Function(
        ('tellraw @s ["","Credits: ",{"text":"[click me]","clickEvent":{"action":"open_url","value":"%s"}}]' % link)
    )
