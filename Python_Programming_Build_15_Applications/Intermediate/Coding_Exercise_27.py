# Attempt this with paitience and remeber that you'll only succed when you fail
# Start off by creating the Guest class and it's methods

registrations = {'John': 'A011', 'Kyle': 'A009', 'Jake': 'BQ02', 'Tamra': 'A015', 'Josh': 'BQ03'}
keys = ['A010', 'A012', 'A014', 'BQ01']

class Guest():
    def __init__(self, name):
        self.name = name
        self.next_booking = ''

    def is_regd(self):
        if self.name in registrations:
            print('Registered')
        else:
            print('Not Registered')
    
    def get_key(self):
        if self.name in registrations:
            for k,v in registrations.items():
                if k == self.name:
                    print('Key : ' + str(v))
        else:
            self.reg()        
            
    def reg(self):
        if keys != []:
            self.next_booking = keys[0]
            keys.pop(0)
            print('Key : ' + str(self.next_booking))
            registrations[self.name] = self.next_booking
        else:
            self.fullyBooked()

    def fullyBooked(self):
        print('Sorry, no vacant rooms available')
    
    
guest1 = Guest('Josh')
print(guest1.name)
guest1.is_regd()
guest1.get_key()

guest2 = Guest('Hans')
print(guest2.name)
guest2.is_regd()
guest2.get_key()

guest3 = Guest('Evan')
print(guest3.name)
guest3.is_regd()
guest3.get_key()

guest4 = Guest('Kyle')
print(guest4.name)
guest4.is_regd()
guest4.get_key()

guest5 = Guest('Ted')
print(guest5.name)
guest5.is_regd()
guest5.get_key()

guest6 = Guest('Karl')
print(guest6.name)
guest6.is_regd()
guest6.get_key()

guest7 = Guest('Sam')
print(guest7.name)
guest7.is_regd()
guest7.get_key()
