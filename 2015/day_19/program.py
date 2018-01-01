from random import shuffle
import re

with open('input_file.txt') as inputfile:
    replacements = [line.strip().split(" => ") for line in inputfile]

medicine = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

unique = set()
for replacement in replacements:
    find, replace = replacement
    indexes = [m.start() for m in re.finditer(find, medicine)]

    for index in indexes:
        unique.add(medicine[:index] + replace + medicine[index + len(find):])

print len(unique)

count = 0
current_mol = medicine
while current_mol != 'e':
    temp_molecule = current_mol
    for value, key in replacements:
        if key in current_mol:
            count += current_mol.count(key)
            current_mol = current_mol.replace(key, value)

    if temp_molecule == current_mol:
        current_mol = medicine
        count = 0
        shuffle(replacements)

print count
