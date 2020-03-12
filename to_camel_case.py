def to_camel_case(text):
    badlist = ['_','-']
    goodlist = [char for char in text]
    for i in range(0,len(goodlist)):
        if goodlist[i] in badlist:
            goodlist[i+1] = goodlist[i+1].upper()
    text = ''
    for i in goodlist:
        text += i
    text = text.replace('_','')
    text = text.replace('-','')
    return text


tc2 = ''
tc = 'the_stealth_warrior_or_The-Stealth-Warrior'
print(to_camel_case(tc))


