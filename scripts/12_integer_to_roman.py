from collections import OrderedDict


def inttoroman(num):
    map = OrderedDict({'1000': 'M','900': 'CM','500':'D','400': 'CD','100': 'C','90': 'XC', '50': 'L', '40': 'XL','10': 'X','9': 'D','5': 'V','4': 'IV','1': 'I'})
    roman = ''
    while num > 0:
        for i in map.keys():
            if num / int(i) >= 1:
                num = num - int(i)
                roman = roman + map[i]
                break
    return roman