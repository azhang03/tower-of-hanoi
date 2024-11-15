# Towers of Hanoi Game
import random
import time

# Class for the functionality of a peg
class Peg:
    def __init__(self, discnum, start = False):
        if start:
            self.discs = list(reversed(range(discnum)))
            self.size = discnum
        else:
            self.discs = [-1]*discnum
            self.size = 0

    def checkTop(self):
        if self.size <= 0:
            print("This peg is empty!")
            return -1
        return self.discs[self.size-1]

    def removeTop(self):
        if self.size <= 0:
            print("This peg is empty!")
            return False
        else:
            self.discs[self.size-1] = -1
            self.size -= 1
            return True

    def addToTop(self, d):
        # first one is to prevent it from not adding if its -1
        if self.size != 0 and (d > self.discs[self.size-1] or self.size == len(self.discs)):
            print("Invalid move!")
            return False
        else:
            self.discs[self.size] = d
            self.size += 1
            return True

# Class that holds the 3 pegs
class Towers:
    def __init__(self, discnum):
        self.pegs = [Peg(discnum, True), Peg(discnum), Peg(discnum)]

    def display_pegs(self):
        pegs = self.pegs
        for i in reversed(range(len(pegs[0].discs))):
            for peg in pegs:
                if peg.discs[i] != -1:
                    print(" ",peg.discs[i], end=" ")
                else:
                    print(" ","|", end=" ")
            print()
        print("--------------")

    def checkSolved(self):
        if (self.pegs[0].size == 0) and (self.pegs[1].size == 0):
            return True
        return False

    def move(self, take, add):
        if self.pegs[take].size > 0:
            holder = self.pegs[take].checkTop()
        if self.pegs[take].removeTop():
            # If we are able to remove, try adding
            if not self.pegs[add].addToTop(holder):
                # If we can't add, return the disc
                self.pegs[take].addToTop(holder)

# Fancy Completion Function
def scrambled_display():
    target = "YOU DID IT! CONGRATULATIONS!"
    display = [" "] * len(target)
    while ''.join(display) != target:
        for i in range(len(target)):
            if display[i] != target[i]:
                display[i] = chr(random.randint(32, 126))
        print(''.join(display), end='\r')   # Overwrite the line
        time.sleep(0.01)
    print("".join(display))


def main():
    discnum = input("How many discs would you like? ").strip()

    while not discnum.isdigit():
        discnum = input("Hmmm...that's not a number. Try again: ").strip()

    tower = Towers(int(discnum))

    print("WELCOME TO THE TOWERS OF HANOI!")
    tower.display_pegs()

    take = input("What peg are you taking from? (0,1,2)\n").strip()
    while (not take.isdigit()) or (int(take) < 0) or (int(take) > 2):
        take = input("Not a valid value! Try again! ")

    add = input("Where will you add this? (0,1,2)\n").strip()
    while (not add.isdigit()) or (int(add) < 0) or (int(add) > 2):
        add = input("Not a valid value! Try again! ")

    while (take != 'q'):
        tower.move(int(take), int(add))
        tower.display_pegs()
        if tower.checkSolved():
            take = 'q'
            print()
            scrambled_display()
        else:
            take = input("What peg are you taking from? (0,1,2)\n").strip()
            while (not take.isdigit()) or (int(take) < 0) or (int(take) > 2):
                take = input("Not a valid value! Try again! ")

            add = input("Where will you add this? (0,1,2)\n").strip()
            while (not add.isdigit()) or (int(add) < 0) or (int(add) > 2):
                add = input("Not a valid value! Try again! ")

    for i in range(10, 0, -1):
        print(f"Closing in {i} second(s)... ", end='\r', flush=True)
        time.sleep(1)
    print("Bye!")




if __name__ == "__main__":
    main()