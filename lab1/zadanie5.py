
def groupByFileType(filesNames):
    if not isinstance(filesNames, list):
        raise Exception("Should be given an list")
    if not all(isinstance(item, str) for item in filesNames):
        raise Exception("Array should only contain strings")
    if not all(len(item.split(".", 1)) > 1 and len(item.split(".", 1)[1]) > 0 for item in filesNames):
        raise Exception("Every filename should contain type after dot")

    fileTypes = set()

    for fileName in filesNames:
        fileType = fileName.split(".", 1)[1].strip()
        fileTypes.add(fileType)
    
    result = []
    for fileType in fileTypes:
        fileTypeArray = []
        for fileName in filesNames:
            if fileType == fileName.split(".", 1)[1].strip():
                fileTypeArray.append(fileName)
        result.append(fileTypeArray)
    return result