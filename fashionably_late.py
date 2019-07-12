# %%
party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

# %%
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    arrivedAt = arrivals.index(name) + 1
    length = len(arrivals)
    halfPosition = length//2 + (length % 2) 
    if arrivedAt > halfPosition and arrivedAt != length:
        return True
    else:
        return False


# %%
print(fashionably_late(party_attendees, 'Mona'))


#%%
planets = ['Mercury',
 'Venus',
 'Earth',
 'Malacandra',
 'Jupiter',
 'Saturn',
 'Uranus',
 'Neptune']


#%%
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

#%%
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]
print(planets)


#%%
print(planets)

#%%
t = (1, 2, 3)

#%%
print(type(t))

#%%
print(t[0])

#%%
a = 3
b = 5
a, b = b, a
print(a)
print(b)

#%%
datestr: str = '1956-01-31'
year = datestr.split('-')
print(year)
#%%
