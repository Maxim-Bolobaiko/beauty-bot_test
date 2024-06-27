import json


def compare_jsons(json_old, json_new, diff_list):
    result = {}

    def compare_nested(old, new, path):
        for key in old:
            if key in new:
                current_path = path + [key]
                if isinstance(old[key], dict) and isinstance(new[key], dict):
                    compare_nested(old[key], new[key], current_path)
                elif old[key] != new[key]:
                    full_path = ".".join(current_path)
                    if len(current_path) > 2:
                        if current_path[-2] in diff_list:
                            result[full_path] = new[key]
                    else:
                        if current_path[-1] in diff_list:
                            result[full_path] = new[key]

    compare_nested(json_old, json_new, [])
    return result
