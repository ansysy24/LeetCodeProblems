def validStartingCity(distances, fuel, mpg):
    distances2 = distances + distances
    fuel = [num*mpg for num in fuel]
    fuel = fuel + fuel
    for i, dist in enumerate(distances):
        current = 0
        answer = True
        for j in range(i, i+len(distances)):
            current = current - distances2[j] + fuel[j]
            if current < 0:
                answer = False
                break
        if answer:
            return i

def validStartingCity(distances, fuel, mpg):
    fuel = [f*mpg for f in fuel]
    current_gas = 0
    min_gas = 0
    min_i = 0
    for i, dist in enumerate(distances):
        if current_gas < min_gas:
            min_gas = current_gas
            min_i = i
        current_gas = current_gas - dist + fuel[i]
    return min_i
