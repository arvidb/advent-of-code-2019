'''input
171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX
'''
reactions = {}
try:
    while True:
        requirements, output = input().split('=>')
        output = tuple(output.strip().split(' '))
        reactions[output[1]] = (output[0], [tuple(x.strip().split(' ')) for x in requirements.split(',')])
except:
    pass


def required_ore(amount, chemical, owned):
    global reactions

    if chemical == 'ORE':
        return amount

    if chemical in owned:
        saved = owned[chemical]
        if amount >= saved:
            amount -= saved
            owned[chemical] = 0
        elif amount < saved:
            owned[chemical] -= amount
            amount = 0

    increment, input_chems = reactions[chemical]
    needed = (1 + ((amount-1) // int(increment)))
    ore = 0

    for input_chem in input_chems:
        i, c = input_chem
        ore += required_ore(needed*int(i), c, owned)

    if needed*int(increment) > amount:
        if chemical not in owned:
            owned[chemical] = 0
        owned[chemical] += (needed*int(increment)) - amount

    return ore

print("Part 1", required_ore(1, 'FUEL', {}))

def binary_search(low, high, target):
    while low <= high:
        mid = low + (high - low)//2
        ore = required_ore(mid, 'FUEL', {})
        if ore == target:
            return mid
        elif ore > target:
            high = mid - 1
        else:
            low = mid + 1

    return mid

def find_required_ors(target):
    global reactions
    high = 1
    while True:
        if required_ore(high, 'FUEL', {}) > target:
            break
        else:
            high *= 2

    return binary_search(high//2, high, target)

print("Part 2", find_required_ors(1000000000000))