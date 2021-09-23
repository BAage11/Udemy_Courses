guestList = {'John': 'A011', 'Kyle': 'A009', 'Jake': 'BQ02', 'Tamra': 'A015', 'Josh': 'BQ13'}

def get_key(guestName):
    capName = guestName.capitalize()
    found = False
    for k,v in guestList.items():
        if k == capName:
            print("Key : " + v)
            found = True
    if found != True:
        print("Not Registered")
            

get_key('jake')
get_key('tamra')
get_key('Ted')