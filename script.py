layerOne = [
    ["w", "r", "g"],
    ["w","r"],
    ["w", "b", "r"],
    ["w","g"],
    ["w","b"], 
    ["w", "g", "o"], 
    ["w","o"], 
    ["w", "o", "b"]]
layerTwo = [
    ["r","g"], 
    ["r","b"], 
    ["o","g"], 
    ["o","b"]]
layerThree = [
    ["y", "r", "b"],
    ["y","r"],
    ["y", "g", "r"],
    ["y","b"],
    ["y","g"], 
    ["y", "b", "o"], 
    ["y","o"], 
    ["y", "o", "g"]]
cube = [layerOne, layerTwo, layerThree]

def listShiftLeft(list):
    list.append(list[0])
    list.remove(list[0])
    return list
def listShiftRight(list):
    originalList = tuple(list)
    list.remove(list[2])
    list.insert(0, originalList[2])
    return list
def edgeFlip(inpEdge):
    newEdge = [inpEdge[1], inpEdge[0]]
    return newEdge

def moveF(originalCube):
    virtualCube = [originalCube[2][2]]
    return(virtualCube)

print(cube)


