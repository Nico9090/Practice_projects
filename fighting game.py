class SwordFight:
        def __init__(self,type,size, horse):
                self.type=type
                self.size=size
                self.horse=horse
        def pick_up_sword(self):
                return 'Picking up %s' %(self.type)

if __name__ == "__main__":
        point=SwordFight('point sword','2 lbs','brown horse')
        print(point.pick_up_sword())
print(dir(point))

