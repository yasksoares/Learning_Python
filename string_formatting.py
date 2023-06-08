"""
 Basic string formatting
 s - string
 d - int
 f - float
 x ou X - Hexadecimal
 > - Left 
 < - Right
 ^ - Center
 Signal - + or -
 = - forces aa number to appear before the sign
 Ex: 0 >-100, .1f
 Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')

print(f'{variavel: >10}')

print(f'{variavel: >20}')

print(f'{variavel: ^10}')

print(f'{variavel:$^10}')

print(f'{variavel:0^10}')

print(f'{1000.654151648487985:,.1f}')

print(f'{-1000.654151648487985:-,.1f}')

print(f'{1000.654151648487985:+,.1f}')

print(f'{1000.654151648487985:0=+10,.1f}')

print(f'The hexadecimal of 1500 is {1500: 08X}')





