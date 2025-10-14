# battle.py — инициализация и цикл боя
import random
from core import Character, Warrior, Mage, Healer, Rogue, Boss
import skills

def turn_order(actors):
    alive = [a for a in actors if a.is_alive]
    return sorted(alive, key=lambda x: x.agility, reverse=True)

def all_dead(group):
    return not any(x.is_alive for x in group)

def make_party_and_boss():
    warrior = Warrior("Axe (Воин)",  "Warrior", hp=110, mp=22, strength=16, agility=8,  intelligence=5)
    mage    = Mage   ("Skywrath Mage (Маг)", "Mage", hp=75,  mp=46, strength=5,  agility=12, intelligence=18)
    healer  = Healer ("IO (Хил)",    "Healer",  hp=80,  mp=48, strength=4,  agility=10, intelligence=16)
    rogue   = Rogue  ("Riki (Плут)", "Rogue",   hp=85,  mp=28, strength=10, agility=17, intelligence=7)
    party = [warrior, mage, healer, rogue]
    boss = Boss("Roshan (Босс)", "Boss", hp=420, mp=120, strength=18, agility=11, intelligence=15)
    return party, boss

def hero_turn(hero, boss, party):
    if not hero.is_alive:
        return
    # Хил лечит самого низкого по %HP, остальные — свою способность по боссу
    if isinstance(hero, Healer):
        low = [p for p in party if p.is_alive and p.hp / p.hp_max < 0.5]
        if low:
            for line in skills.healer_heal(hero, low[0], boss): print(line)
        else:
            print(hero.attack(boss))
    elif isinstance(hero, Warrior):
        for line in skills.warrior_power_strike(hero, boss): print(line)
    elif isinstance(hero, Mage):
        for line in skills.mage_fireball(hero, boss): print(line)
    elif isinstance(hero, Rogue):
        for line in skills.rogue_backstab(hero, boss): print(line)
    else:
        print(hero.attack(boss))

def battle(seed=42):
    random.seed(seed)  # глобальный сид для повторяемости критов/спецударов
    party, boss = make_party_and_boss()
    round_no = 1
    print("=== 4 против Босса — старт боя ===")

    while boss.is_alive and not all_dead(party):
        print("\n" + "="*60)
        print(f"Раунд {round_no}")
        for a in party + [boss]:
            print(f"  {a.name:22}  HP {a.hp:3}/{a.hp_max:3}  MP {a.mp:3}/{a.mp_max:3}")

        order = turn_order(party + [boss])
        for actor in order:
            if not actor.is_alive:
                continue
            if actor is boss:
                for line in boss.shockwave(party): print(line)
            else:
                hero_turn(actor, boss, party)
            if not boss.is_alive or all_dead(party):
                break
        round_no += 1

    print("\n" + "="*60)
    print("Победа пати!" if not boss.is_alive else "Победа босса...")

if __name__ == "__main__":
    battle()
