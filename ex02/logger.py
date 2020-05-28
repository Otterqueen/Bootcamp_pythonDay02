import time
from random import randint
import os


def log(fonction):
    def fonc_to_print_log(*arg, **kwarg):
        f = open("machine.log", "a")
        string_to_print = "({0})Running: {1: <20}\t\
".format(os.getenv("USER"), fonction.__name__.replace("_", " ").capitalize())

        start = time.time()
        val_to_ret = fonction(*arg, **kwarg)
        end = time.time()
        exec_time = end - start
        if exec_time < 1:
            string_to_print += (
                "[ exec-time = {0:.3f} ms ]\n".format(exec_time * 1000))
        else:
            string_to_print += (
                "[ exec-time = {0:.3f} s  ]\n".format(end - start))
        f.write(string_to_print)
        f.close()
        return val_to_ret

    return fonc_to_print_log


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
