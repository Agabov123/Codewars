def cakes(recipe, available):
    check = all(item in recipe for item in available)
    if check is True:
        return 0
    else:
        cake = 100
        for i in recipe:
            cakes = int(available[i]/recipe[i])
            if cakes < cake:
                cake = cakes
        return cake
