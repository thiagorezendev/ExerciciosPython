#palavras = ('neymar', 'ronaldinho', 'messi', 'zidade', 'cristiano',
            #'mbappe', 'romario', 'cruyff', 'zlatan', 'neuer')
#for i in palavras:
    #print(f'\nNo nome {i.upper()} temos as vogais: ', end='')
    #for letra in i:
        #if letra.upper() in 'AEIOU':
            #print(f'{letra}', end=' ')


palavras = ('neymar', 'ronaldinho', 'messi', 'zidade', 'cristiano',
            'mbappe', 'romario', 'cruyff', 'zlatan', 'neuer')
for p in palavras:
    print(f'\nNo nome {p.upper()} temos as vogais', end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end=' ')