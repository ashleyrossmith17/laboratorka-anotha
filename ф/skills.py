# skills.py — простые способности (по одной на класс)
# Чтобы избежать циклических импортов, тут нет импортов из core;
# функции ожидают объекты с нужными полями/методами (duck typing).
def warrior_power_strike(user, target):
    cost = 6
    if user.mp < cost:
        return [user.attack(target)]
    user.mp -= cost
    dmg = int(user.strength * 1.8) + 4
    dealt = target.take_damage(dmg)
    return [f"{user.name} использует Мощный удар по {target.name}: -{dealt}."]

def mage_fireball(user, target):
    cost = 8
    if user.mp < cost:
        return [user.attack(target)]
    user.mp -= cost
    dmg = int(user.intelligence * 2.0) + 3
    dealt = target.take_damage(dmg)
    return [f"{user.name} кидает Огненный шар в {target.name}: -{dealt} маг. урона."]

def healer_heal(user, ally, fallback_target):
    cost = 7
    if user.mp < cost:
        return [f"{user.name} не хватает MP — атакует.", user.attack(fallback_target)]
    user.mp -= cost
    before = ally.hp
    amount = 22 + user.intelligence // 2
    ally.hp = min(ally.hp_max, ally.hp + amount)
    healed = ally.hp - before
    return [f"{user.name} лечит {ally.name} на {healed} HP."]

def rogue_backstab(user, target, rng_roll=None):
    cost = 5
    if user.mp < cost:
        return [user.attack(target)]
    user.mp -= cost
    dmg = int(user.agility * 1.7) + 2
    # небольшой шанс сверхкрита у плута — используем встроенный random
    import random as _rnd
    if _rnd.randrange(100) < 25:
        dmg = int(dmg * 1.5)
    dealt = target.take_damage(dmg)
    return [f"{user.name} наносит Удар в спину {target.name}: -{dealt}."]
