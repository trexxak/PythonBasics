### Python Klassen ###
def diamond():

    class Human:
        year = 1990

    class Student(Human):
        year = 1996

    class Teacher(Human):
        year = 2018

    class Markus(Teacher, Student):
        pass
        # t_year = Teacher.year
        # s_year = Student.year
        # h_year = Human.year
    
    print(Markus.year)



## Aufbau ##
"""

Um eine Klasse zu erstellen, wird das "class"-keyword verwendet:
        
        class Test():
            pass

Instanziierung geschieht durch Zuweisung der jeweiligen Klasse.

        test = Test()

Konstruktoren (in Python: Initiatoren), werden durch die __init__()
Methode definiert. 

Erster Parameter ist hier immer "self", hierbei ist der Bezeichner
für den Parameter jedoch arbiträr. 

Dem self folgende Parameter, können dann an instanziierte Objekte übergeben werden:

        class Test():
            def __init__(self,param):
                self.eigenschaft = param

Um den Parameter auch der Eigenschaft des Objekts zu übergeben, 
muss diese noch dem Parameter zugewiesen werden (siehe oben).

"""
def classes():
    class Entity():
        def __init__(self, name="dummy", position=(-1000,-1000), is_player=False):
            self.name = name
            self.pos = position
            self.player = is_player
    def instancing_objects():
        enemy_1 = Entity("Ghost",(0,8))
        enemy_2 = Entity("Slime",(4,-4))
        p_name = input("What's your name?")
        player = Entity(p_name,(0,0),True)
        actors = [enemy_1, enemy_2, player]
        [print(f"{obj.name} stands on {obj.pos} and is " +("not ","")[obj.player]+"a player.") 
        for obj in actors]
    instancing_objects()
    


## Vererbung ##
"""

Klassen können voneinander erben:

        class ElternKlasse():
            def __init__(self, param):
                self.eigenschaft = param

        class KindKlasse(ElternKlasse):
            pass

        kind = KindKlasse(4)

Hier kann das Problem auftreten, dass der Initiator der Kindklasse 
den der Elternklasse überschreibt, und dies so dazu führen kann, 
dass Elterneigenschaften für das Objekt überschrieben werden.

Um dies zu verhindern, lässt sich der Elterninitator innerhalb des Kindinitiators 
aufrufen (entweder durch "super()" oder den Bezeichner der Elternklasse):

        class ElternKlasse():
            def __init__(self, param):
                self.eigenschaft = param

        class KindKlasse(ElternKlasse):
            def __init__(self, param, param_2):
                super().__init__(param)
                #ElternKlasse.__init__(self,param)
                self.eigenschaft_2 = param_2
        
        kind = KindKlasse(4,2)

"""
def inheritance():
    class Entity():
        def __init__(self,name,pos,target):
            self.name = name
            self.pos = pos
            self.target = target

    class NPC(Entity):
        def __init__(self,name,pos,target):
            super().__init__(name,pos,target)
            self.name = "[NPC] "+ name
            self.drop = "trash"
        
        def die(self):
            print(f"{self.name} dies and drops {self.drop}.")
            
    class Hostile(NPC):
        def __init__(self,name,pos,target,atck,deff):
            super().__init__(name,pos,target)
            self.atck = atck
            self.deff = deff

        def attack(self):
            print(f"{self.name} attacks {self.target.name} for {self.atck-(self.target.deff*.5)} damage.")
    
    class Friendly(NPC):
        def __init__(self,name,pos,target):
            super().__init__(name,pos,target)
            self.stock = ("expensive trash",.2)
        def trades(self):
            print(f"{self.name} offers you to trade {self.stock[0]} for {self.stock[1]} Gold!")

    class Other(NPC):
        def hopping(self):
            print(f"{self.name} hops around happily.")

    class Player(Entity):
        def __init__(self,name,pos,target,level,strength,durability):
            super().__init__(name,pos,target)
            self.atck = strength*level*0.1
            self.deff = durability*level*0.1
        def attack(self):
            print(f"{self.name} attacks {self.target} for {self.atk-self.target.deff}.")

    def miniworld():
        bunny = Other("Fips",1,"Kräuter")
        npc_0 = Friendly("Fantastico",2,bunny)
        player_0 = Player("Mochog",0,None,10,10,10)
        npc_1 = Hostile("Toaster",3,player_0,10,10)

        run = True
        while run:
            player_0.pos += 1
            if player_0.pos == npc_0.pos:
                npc_0.trades()
            if player_0.pos == npc_1.pos:
                npc_1.attack()
            if player_0.pos == bunny.pos:
                bunny.hopping()
            if player_0.pos > 10:
                run = False
    miniworld()
