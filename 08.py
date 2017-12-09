import re

def variableExists(registryName):
    if registryName in globals():
        return True
    else:
        return False

def initializeRegistryIfEmpty(conditionRegistry):
    if (not variableExists(conditionRegistry)):
        registryInitialization = 'global ' + conditionRegistry + ';' \
                                 + conditionRegistry + ' = 0'
        exec registryInitialization


def printMax(registries):
    exec 'print ' + str(getMax(registries))


def getMax(registries):
    return eval('max(' + ', '.join(registries) + ')')


with open('inputs/08.txt') as f:
    operations = {'inc': '+=', 'dec': '-='}
    registries = set()
    maxValueHeld = 0
    for line in f:
        # parsing
        lineMatcher = re.match(r'(\w+) (\w+) ([-]?\d+) if (.*)', line)
        expressionRegistry = lineMatcher.group(1)
        registries.add(expressionRegistry)
        expressionOperation = lineMatcher.group(2)
        expressionOperand = lineMatcher.group(3)
        condition = lineMatcher.group(4)
        conditionMatcher = re.match(r'(\w+) ([<>=!]+ ([-]?\d+))', condition)
        conditionRegistry = conditionMatcher.group(1)
        registries.add(conditionRegistry)

        # evaluation
        initializeRegistryIfEmpty(conditionRegistry)
        evalResult = eval(condition)
        initializeRegistryIfEmpty(expressionRegistry)
        if evalResult:
            expression = expressionRegistry + operations[expressionOperation] + expressionOperand
            exec expression
        maxRegistry = getMax(registries)
        if maxRegistry > maxValueHeld:
            maxValueHeld = maxRegistry
            

printMax(registries)
print maxValueHeld
