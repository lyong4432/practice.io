import sys 
input = sys.stdin.readline  

n = input().strip()
if n == 'M':print('MatKor')
elif n == 'W': print('WiCys')
elif n == 'C': print('CyKor')
elif n == 'A': print('AlKor')
elif n == '$': print('$clear')
