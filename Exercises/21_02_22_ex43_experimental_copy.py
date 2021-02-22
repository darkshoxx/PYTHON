WIN_STATE = "You Failed!"

class Scene(object):

    def enter(self):
        pass


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

    def enter(self):
        print("lol, you died. Try again? 1:Yes")
        restart_request = input("> ")
        if restart_request == '1':
            return 'central_corridor'
        else:
            return 'finished'


class CentralCorridor(Scene):

    def enter(self):
        print("THis is CR! THere is Alien. YOu have Gun WHat do?")
        print("0:Talk, 1:Shoot")
        decision = input("> ")
        if decision == '0':
            print("He no talk, he kill")
            return 'death'
        else:
            print("He Die")
        return 'escape_pod'


class LaserWeaponArmory(Scene):

    def enter(self):
        pass


class TheBridge(Scene):

    def enter(self):
        pass


class EscapePod(Scene):

    def enter(self):
        print("Here is pod. Time is running out. Use Pod? 0:No 1:Yes")
        pod_usage = input("> ")
        if pod_usage == '0':
            print("run out of O2.")
            return 'death'
        else:
            print("Good Job")
            global WIN_STATE
            WIN_STATE = "You YOu WIN"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print(f"Game over. You {WIN_STATE}")

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_brigde': TheBridge(),
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
