def format(item)-> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }

def formatter(item)->list:
    return [format(item) for itm in item]