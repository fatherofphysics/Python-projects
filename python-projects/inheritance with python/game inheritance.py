# game in python using inheritance

class User():	#Main class
	def sign_in(self):
		print('logged in')

class Wizard(User): # sub class
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self): # method
		print(f'attacking with power of {self.power}')

class Archer(User): # sub class
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows

	def attack(self): # method
		print(f'attacking with arrows : arrows left - {self.num_arrows}')

class Hybrid(Wizard, Archer): # a hybrid player who have both powers
	def __init__(self, name, power, num_arrows):
		Archer.__init__(self, name, num_arrows)
		Wizard.__init__(self, name, power)


# give name, power

wizard1 = Wizard('Vedant',50)
archer1 = Archer('Nitin', 100)

# calling player power

wizard1.attack()
archer1.attack()