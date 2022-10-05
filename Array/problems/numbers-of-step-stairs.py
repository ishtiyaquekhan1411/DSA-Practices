# Need to understand solution of this one.
def possibilities(stair_steps):
  if stair_steps == 0:
    return 0
  elif stair_steps == 1:
    return 1
  elif stair_steps == 2:
    return 2
  else:
    return possibilities(stair_steps - 1) + possibilities(stair_steps - 2)

# Driver code
stair_steps = 7
result = possibilities(stair_steps)
print("Number of possibilities to walk upstairs is", result)