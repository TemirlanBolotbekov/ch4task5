class Soldier():
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun


class Guns():
    def shoots(self):
        print(f'{self.name} shoots from: {self.gun}')
        self.ammunition = 30
        while self.ammunition > 0:
            self.ammunition -= 1
            print('shot')

        if self.ammunition == 0:
            self.reloads()
        else:
            pass


    def reloads(self):
        self.reload = input('reload weapson? y/n: ')
        if self.reload == 'y':
            self.shoots()
        else:
            pass


class Act_of_Shooting(Soldier, Guns):
    def __init__(self, name, gun):
        Soldier.__init__(self, name, gun)


soldier1 = Act_of_Shooting('Ryan', 'AK47')
soldier1.shoots()