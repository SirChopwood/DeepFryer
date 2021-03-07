    import names
    import random


    class CombatClass:
        Name = "Combat Class"
        Damage = 10
        Health = 10
        Saves = 10  # Chance to dodge incoming damage (e.g. 1 in 10)


    class WarriorClass(CombatClass):
        Name = "Warrior"
        Damage = 5
        Health = 20
        Saves = 5


    class ArcherClass(CombatClass):
        Name = "Archer"
        Damage = 15
        Health = 10
        Saves = 3


    class RogueClass(CombatClass):
        Name = "Rogue"
        Damage = 20
        Health = 5
        Saves = 2


    class FryClass:
        Name = "Tsuki's Fry"
        Class = WarriorClass
        Health = 0
        Level = 1
        Damage = 0

        def __init__(self, newname, newclass, newlevel):
            self.Name = newname
            self.Class = newclass
            self.Level = newlevel
            self.Damage = self.Class.Damage * self.Level
            self.Health = self.Class.Health * (self.Level*0.15)


    class BossClass:
        Name = "ModCorp Employee"
        Health = 400
        Level = 5
        Damage = 100

        def __init__(self, Name, Fries):
            self.Name = Name
            avg_dmg = []
            avg_hp = []
            for fry in Fries:
                avg_dmg.append(fry.Damage)
                avg_hp.append(fry.Health)
            roll_dmg = random.randint(1, 20)
            if roll_dmg == 1:
                self.Damage = (sum(avg_dmg) / len(avg_dmg)) * 1.5
            elif 1 < roll_dmg < 20:
                self.Damage = (sum(avg_dmg) / len(avg_dmg)) * 3
            elif roll_dmg == 20:
                self.Damage = (sum(avg_dmg) / len(avg_dmg)) * 5

            roll_hp = random.randint(1, 20)
            if roll_hp == 1:
                self.Health = (sum(avg_hp) / len(avg_hp)) * 1000
            elif 1 < roll_hp < 6:
                self.Health = (sum(avg_hp) / len(avg_hp)) * 1250
            elif 6 < roll_hp < 11:
                self.Health = (sum(avg_hp) / len(avg_hp)) * 1500
            elif 11 < roll_hp < 20:
                self.Health = (sum(avg_hp) / len(avg_hp)) * 1750
            elif roll_hp == 20:
                self.Health = (sum(avg_hp) / len(avg_hp)) * 2000

            print("A wild " + self.Name + " has appeared! " + str(self.Health) + "HP  " + str(self.Damage) + "ATK")


    def GenerateFries(count):
        Fries = []
        Classes = [ArcherClass(), WarriorClass(), RogueClass()]

        for i in range(count):
            FrenchFry = FryClass(names.get_full_name(), random.choice(Classes), random.randint(1, 50))
            Fries.append(FrenchFry)

        return Fries


    def AttackLoop(Fries, Boss):
        Round = 0
        while len(Fries)>0 and Boss.Health>0:
            BossTurn = True
            DamageRemaining = Boss.Damage
            Losses = []
            while BossTurn:
                if len(Fries) > 0:
                    Target = random.choice(Fries)
                    d20 = random.randint(0,Target.Saves)
                    if d20 == 1:
                        #print(Target.Name + " dodged an attack")
                        continue
                    else:
                        if Target.Health <= DamageRemaining:
                            Losses.append(Target.Name)
                            Fries.remove(Target)
                            DamageRemaining -= Target.Health
                        else:
                            Target.Health -= DamageRemaining
                            #print(Boss.Name + " Struck down with their BanHammer!\nLosses:")
                            #for Name in Losses:
                            #    print(Name)
                            BossTurn = False
                else:
                    break

            for Fry in Fries:
                Boss.Health -= Fry.Damage

                if Boss.Health <= 0:
                    if isinstance(Fry.Class, WarriorClass):
                        print(Boss.Name + " was defeated in an honourable duel with " + Fry.Name + " and their allies in battle!")
                    if isinstance(Fry.Class, ArcherClass):
                        print(Boss.Name + " was clipped by a storm of arrows from " + Fry.Name + " and their allies at the backlines!")
                    if isinstance(Fry.Class, RogueClass):
                        print(Boss.Name + " was assassinated swiftly by " + Fry.Name + " and their allies in the shadows!")
                    #for fry in Fries:
                    #   print(fry.Name + " the " + fry.Class.Name)
                    FryTurn = False
                    break

            Round += 1

        if len(Fries) <= 0:
            print("The Fries were defeated by " + Boss.Name + "... how unfortunate")
        elif Boss.Health <= 0:
            print(str(len(Fries)) + " were victorious after " + str(Round) + " Round(s)!")



    Fries = GenerateFries(100)
    Boss = BossClass("Daddy Tomb", Fries)
    AttackLoop(Fries, Boss)
    Fries = GenerateFries(100)
    Boss = BossClass("Daddy CALii", Fries)
    AttackLoop(Fries, Boss)
    Fries = GenerateFries(100)
    Boss = BossClass("Daddy Roggy", Fries)
    AttackLoop(Fries, Boss)
    Fries = GenerateFries(100)
    Boss = BossClass("Mummy Tori", Fries)
    AttackLoop(Fries, Boss)
    Fries = GenerateFries(100)
    Boss = BossClass("No1", Fries)
    AttackLoop(Fries, Boss)
    Fries = GenerateFries(100)
    Boss = BossClass("Queen Tsuki", Fries)
    AttackLoop(Fries, Boss)
