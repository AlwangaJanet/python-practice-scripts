import jsonFileHandler

# Read the JSON data
data = jsonFileHandler.readJsonFile('files/insulin.json')

if data != "":
    # Extract insulin molecule data
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
    
    # Calculate the molecular weight of insulin
    aaWeights = data['weights']
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']}
    
    molecularWeightInsulin = sum({x: (aaCountInsulin[x] * aaWeights[x]) for x in aaCountInsulin}.values())
    
    print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
    print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
else:
    print("Error. Exiting program")
