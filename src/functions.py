from fuzzywuzzy import fuzz
import re
import random
import colorsys

def sample_distinct_colors(n):
    colors = []
    for i in range(n):
        hue = i / n
        rgb = colorsys.hsv_to_rgb(hue, 0.85, 0.85)  # reduce saturation and value by 20%
        rgb = (int(rgb[0] * 255), int(rgb[1] * 255), int(rgb[2] * 255))
        colors.append("#{:02x}{:02x}{:02x}".format(*rgb))
    return colors

def sample_colors(hex_palette, n):
    rgb_palette = [hex_to_rgb(hex_color) for hex_color in hex_palette]
    new_colors = set()
    while len(new_colors) < n:
        color1 = random.choice(rgb_palette)
        color2 = random.choice(rgb_palette)
        r = (color1[0] + color2[0]) / 2
        g = (color1[1] + color2[1]) / 2
        b = (color1[2] + color2[2]) / 2
        new_color = "#{:02x}{:02x}{:02x}".format(int(r), int(g), int(b))
        new_colors.add(new_color)
    return list(new_colors)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generateColorPalette(colors, n):
    # Calculate the average hue of the input colors
    avg_hue = sum(int(color[1:3], 16) for color in colors) / len(colors)

    # Generate a list of colors with the same hue and varying lightness
    palette = []
    for i in range(n):
        lightness = (i / (n - 1)) * 255
        color = f"#{int(avg_hue):02x}{int(lightness):02x}{int(lightness):02x}"
        palette.append(color)

    return palette

def getDaysToAdd(date):
    #Define a function to calculate the number of days to add for  determining possible matches
    weekday = date.weekday()
    if weekday == 6:  # Sunday
        return 2
    elif weekday == 5:  # Saturday
        return 3
    elif weekday == 4:  # Friday
        return 4
    else:
        return 1

def extractWords(string:str):
    # This function extracts all the words in a string which are separated by spaces or non-letters.
    # The reason I have it in a function like this is because I was having trouble putting the start/end of string (^$) in a positive lookahead/lookback with an OR clause   
    l1=re.findall(r'^[a-zA-Z]+(?=[^a-zA-Z])',string)
    l4=re.findall(r'^[a-zA-Z]+$',string)
    l2=re.findall(r'(?<=[^a-zA-Z])([a-zA-Z]+)(?=[^a-zA-Z])',string)
    l3=re.findall(r'(?<=[^a-zA-Z])[a-zA-Z]+$',string)
    l1.extend(l2)
    l1.extend(l3)
    l1.extend(l4)
    return [x.upper() for x in l1]

def extractNumbers(string: str):
    # This function extracts all the numbers in a string which are separated by spaces or non-digits.
    # The reason I have it in a function like this is because I was having trouble putting the start/end of string (^$) in a positive lookahead/lookback with an OR clause
    l1=re.findall(r'^[0-9]+(?=[^0-9])',string)
    l4=re.findall(r'^[0-9]+$',string)
    l2=re.findall(r'(?<=[^0-9])([0-9]+)(?=[^0-9])',string)
    l3=re.findall(r'(?<=[^0-9])[0-9]+$',string)
    l1.extend(l2)
    l1.extend(l3)
    l1.extend(l4)
    return l1

# Scoring functions
def narrativeSimilarityScore(t1, t2):
    if fuzz.ratio(t1, t2) >= fuzz.ratio(t2,t1):
        return fuzz.ratio(t1,t2)*0.01
    else:
        return fuzz.ratio(t2,t1)*0.01
    
def matchedWordsScore(n1, n2, weight):
    return weight*len(set(extractWords(n1)).intersection(set(extractWords(n2))))

def matchedNumbersScore(n1, n2, weight):
    return weight*len(set(extractNumbers(n1)).intersection(set(extractNumbers(n2))))

def accountNumberScore(n1, a1, n2, a2, w1, w2):
    if a1 in n2 or a2 in n1:
        return w1
    elif a1[-4:] in n2 or a2[-4:] in n1:
        return w2
    else:
        return 0
    
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
