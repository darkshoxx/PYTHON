from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configures")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud.... if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."

    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded ypour ship and
            destrpyed your entire crew. YOu are the alst durviving 
            menger and your last mission is to get the neutron desturcht
            bomb dfrom the Wwapeons Armorsy, put it in the bringe, and
            blow the sip upo after getting tnoto a n escape pod.
        
            YOuÄre running down the centroal corridor to the Wapons
            Armory when a Fothon jumps out, red scaöly skin, dark grimy
            teetha and evil clown costume flowing arount his hate
            filled body. He's blocking the door to the Armory and
            about to pull a wapopn to blast you..
            """))

        action = input("> ")

        if action == 'shoot!':
            print(dedent("""
            Quick on the deraw you yank oout your blaster and fire 
            it at the Gothon. His clown costume is flowing and 
            moving around hios boy, which thwos off your aim.
             Your laser hits his costume but isses him entirels.
            THis completely ruisn hisbrand ne wcostume his mother
            bought hium, which makes him fly into an insane rage
            and blast you repeatedly in the face until you are
            dead. THen he eats you.
            """))
            return 'death'

        elif action == 'dodge!':
            print(dedent("""
            Like a world class boxer you dodge wavve, slip and
            sligde right as the GortthonÄs blaster cranks a laser
            past your head. In the middle of your artful dodge
            your fot slips and you bang your head on the metal
            wall and pass out. You wake upo shortly after only to 
            die as the Gothon stomps on your head and east you.
            """))
            return 'death'
        elif action == 'tell a joke':
            print(dedent("""
            Lucky for you they made you lerarn Gothon insults in
            the academy, You tell the one Gothon joke you know:
            Lbhe zbgure vf fb snk, jura fur fvgf nebhaq gur bhhfr,
            fur fugf nebhaq gur uubhfr. The Gotrhon sips, tirs
            not to lkaught, then busts out laughng and canÄt move.
            WQHile heÄs alughing you run up and shoot in square in
            the head pitting him down, then jumpo through the
             Waepon Armorey door.
            """))
            return 'laser_weapon_armory'
        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You do a ffive roll into the Waapon Aemory, crouch and scan
        the room for more Gothons that might be hiding. ItÄs dead
        quiet, too quiet. YOu stand up and run to the far side of
        the room and fin the neutron boimb ion ts container.
        THereÄs a jeypad loick oin the npx and you need the ode to
        get the bomb ot. If you get hte code weong 1ß tiomes then 
        the lock closes forever and you canÄt ge the bomb. The
        code is 3 digits.
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks, letting
                gas out. You grab the neutron boimb and run as fast as
                you can to sthe bridsge where you must place it in the 
                right spot.
                """))
            return 'the_bridge'

        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a
                sickening melting sound as the mechanism is fuesd
                together. You decide to sit there and finally the
                Gothons blow up the ship from their shop and you die.
                """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridgfe with the neuton destruc bomb
            under your arm and surprise 5 Gotrzhons who are trying to
             take contorl of the ship. Each f them has an even uglier
             clown costuem than the last. They havenÄt piulled their 
             weapoins oput cet, as the ysee the active bomb under your
             arm and donÄt want to set it off. 
            """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
                In a panic you thrown the bomb at the group of Gothons
                and make a leap for the fdoor,
                Tirght as you drop it a
                Gothon shoots you right in the back killing you,. As
                you die you asee another GOthan frantically try to
                disarm the bomb. YOu die knowing they will oprobably
                blow up when t goes off.
                """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
                You piint your balster at the bombunder your arm and
                the Gothons oputtheir ahjad up and start to sweat.
                Yo inch backward top the door, open it and then
                carefully place the bomb on the foolr, ointing your
                blaster at it. Youtthen jm,p back throught the door,
                opunche the close btuton and blas the lock so the
                Gothans canÄt ge tiout. Noth athat the bomb is placed,
                ypu run to the escape poid to ge toff this tin can.
                """))
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You rush throgzhtb the ship desparately trying top make to to the
            the escape pd before the whole shoip explöodes. It seems
            like hardly any Gothons are on the shiop sou your rin is
            clear of interference. YOu get to the chamber with the
            escape pods and mot need to opick ope opt tale. Sopme of
            them coul be damambed boiut you donÄt have tiome to look.
            There' 5 pods, whic h ojne do yu take?
            """))

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")
        if int(guess) != good_pod:
            print(dedent(f"""
                YOujump into pod {guess} and hit the eject button.
                The pod escapes out iotp the void of space, then
                implodes as the jull ruputes, crishomg yopur bnody int
                jam jelly.
                """))
            return 'death'
        else:
            print(dedent(f"""
                you jump into pod {guess} adn hit the jeect button.
                The opiod easily slides out into sppace hedng to the
                plane  below. As it flies to the planet, you look
                back and see your shop implide then explode like a 
                bright star, takung out th Gorthoin shop at the same
                time. YOu won!
                """))

            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You win! GOod job.")
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)



a_Map = Map('central_corridor')
a_game = Engine(a_Map)
a_game.play()