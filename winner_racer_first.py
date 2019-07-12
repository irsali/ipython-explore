# %%
r = ["Mario", "Bowser", "Luigi"]

# %%
def purple_shell(racers: list):
    first = 'Luigi'
    racers.remove(first)
    racers.insert(0, first)
    return racers

# %%
print(purple_shell(r))
