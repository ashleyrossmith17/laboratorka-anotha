# core.py — базовые сущности: Character, классы героев и Boss
import random

class Character:
    def __init__(self, name, cls, hp, mp, strength, agility, intelligence):
        self.name = name
        self.cls = cls
        self.hp_max = hp
        self.hp = hp
        self.mp_max = mp
        self.mp = mp
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence


    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        amount = max(0, int(amount))
        before = self.hp
        self.hp = max(0, self.hp - amount)
        return before - self.hp

    def attack(self, target):
        # базовая атака для всех классов
        base = self.strength + self.agility // 3
        crit_chance = min(40, 10 + self.agility * 2 // 3)  # %
        if random.randrange(100) < crit_chance:
            base = int(base * 1.6)
            dealt = target.take_damage(base)
            return f"{self.name} Критует {target.name}: -{dealt}."
        dealt = target.take_damage(base)
        return f"{self.name} атакует {target.name}: -{dealt}."

class Warrior(Character):
    pass

class Mage(Character):
    pass

class Healer(Character):
    pass

class Rogue(Character):
    pass

class Boss(Character):
    # Способность босса: удар волной (урон по всем) или одиночная атака
    def shockwave(self, party):
        cost = 12
        logs = []
        if self.mp >= cost:
            self.mp -= cost
            logs.append(f"{self.name} выпускает ударную волну!")
            for p in party:
                if p.is_alive:
                    dealt = p.take_damage(10 + self.intelligence // 2)
                    logs.append(f" ➤ {p.name} получает -{dealt}.")
            return logs
        # иначе одиночная атака по самому слабому по HP
        living = [p for p in party if p.is_alive]
        if not living:
            return ["Босс никого не видит."]
        target = min(living, key=lambda x: x.hp)
        logs.append(self.attack(target))
        return logs
