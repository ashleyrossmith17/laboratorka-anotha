# items.py — (опционально) простые предметы — не используются в бою по умолчанию
class HealthPotion:
    def __init__(self, power=25):
        self.name = f"Зелье лечения (+{power})"
        self.power = power
    def use(self, user, target):
        before = target.hp
        target.hp = min(target.hp_max, target.hp + self.power)
        healed = target.hp - before
        return [f"{user.name} лечит {target.name}: +{healed} HP."]

class ManaPotion:
    def __init__(self, power=15):
        self.name = f"Зелье маны (+{power})"
        self.power = power
    def use(self, user, target):
        before = target.mp
        target.mp = min(target.mp_max, target.mp + self.power)
        gained = target.mp - before
        return [f"{user.name} восполняет ману {target.name}: +{gained} MP."]
