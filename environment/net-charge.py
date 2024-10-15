# Python3.7  
# Coding: utf-8  

# Store the human preproinsulin sequence in a variable
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Concatenate the bInsulin and aInsulin sequences
insulin = bInsulin + aInsulin

# pKa values of amino acids that contribute to the net charge of insulin
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Count the occurrence of relevant amino acids in insulin sequence
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}

# Initialize pH variable
pH = 0

# Loop through pH values from 0 to 14 and calculate net charge
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x]))) \
        for x in ['k', 'h', 'r']}.values()))
        -(sum({x: ((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x]))) \
        for x in ['y', 'c', 'd', 'e']}.values())))
    
    # Print the pH value and corresponding net charge
    print('{0:.2f}'.format(pH), netCharge)
    
    # Increment pH
    pH += 1
