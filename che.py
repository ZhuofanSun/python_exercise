name = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
        'Sc', 'Ti', 'V', 'Cr', 'Mg', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
        'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Hf',
        'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt']
mass = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 36, 40, 39, 40, 45, 47, 50, 52, 55, 56, 59, 59, 64,
        65, 70, 73, 75, 79, 80, 84, 86, 88, 89, 91, 93, 96, 98, 101, 102, 106, 108, 112, 115, 119, 122, 128, 127, 131,
        133, 137, 139, 179, 181, 184, 186, 190, 192, 195]
D = {}
for e in range(len(name)):
    D[name[e]] = mass[e]
formula = input('Please enter a chemical formula: ')
formula_lst = []
for e in range(65, 91):
    e = chr(e)
    formula = formula.replace(e, '+' + e)
for e in range(10):
    formula = formula.replace(str(e), '*' + str(e))
for e in range(10):
    formula = formula.replace('*' + str(e) + '*', '*' + str(e))
formula = formula.replace('(+', '+(')
for e in D:
    if len(e) == 2:
        formula = formula.replace(e, str(D[e]))
for e in D:
    if len(e) == 1:
        formula = formula.replace(e, str(D[e]))
print(eval(formula))
