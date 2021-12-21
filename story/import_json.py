import json


def import_json(dir: str, obj: str) -> list:
    # "story/scenes.json" 'scenes'
    with open(dir) as jsonScenesFile:
        file = json.load(jsonScenesFile)
        content = file[obj]
        jsonScenesFile.close()
    return content
