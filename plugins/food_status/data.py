

class EffectList:

    SPEED = "speed"
    SLOWNESS = "slowness"
    HASTE = "haste"
    MINING_FATIGUE = "mining_fatigue"
    STRENGTH = "strength"
    INSTANT_HEALTH = "instant_health"
    INSTANT_DAMAGE = "instant_damage"
    JUMP_BOOST = "jump_boost"
    NAUSEA = "nausea"
    REGENERATION = "regeneration"
    RESISTANCE = "resistance"
    FIRE_RESISTANCE = "fire_resistance"
    WATER_BREATHING = "water_breathing"
    INVISIBILITY = "invisibility"
    BLINDNESS = "blindness"
    NIGHT_VISION = "night_vision"
    HUNGER = "hunger"
    WEAKNESS = "weakness"
    POISON = "poison"
    WITHER = "wither"
    HEALTH_BOOST = "health_boost"
    ABSORPTION = "absorption"
    SATURATION = "saturation"
    GLOWING = "glowing"
    LEVITATION = "levitation"
    LUCK = "luck"
    BAD_LUCK = "bad_luck"
    SLOW_FALLING = "slow_falling"
    CONDUIT_POWER = "conduit_power"
    DOLPHINS_GRACE = "dolphins_grace"
    BAD_OMEN = "bad_omen"
    HERO_OF_THE_VILLAGE = "hero_of_the_village"
    DARKNESS = "darkness"


FOOD_STATUS_CONFIG = {
    "apple": [(EffectList.SPEED, 10, 1), [EffectList.REGENERATION, 10, 1]]
}
