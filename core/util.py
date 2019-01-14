def log(jsonData):
    print(jsonData)


def collectionToDict(collectionData):
    if collectionData:
        if collectionData.data:
            return dict(collectionData.data)
        else:
            return dict(collectionData)
    else:
        return {}