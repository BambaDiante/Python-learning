def add_setting(dictionnary, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in dictionnary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    dictionnary[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(dictionnary, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key not in dictionnary:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    dictionnary[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(dictionnary, key):
    key = key.lower()

    if key not in dictionnary:
        return "Setting not found!"

    del dictionnary[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(dictionnary):
    if not dictionnary:
        return "No settings available."

    result = "Current User Settings:\n"
    for key, value in dictionnary.items():
        result += f"{key.capitalize()}: {value}\n"

    return result


test_settings = {
    'theme': 'light',
    'volume': 'high'
}

print(add_setting(test_settings, ('notifications', 'enabled')))
print(update_setting(test_settings, ('theme', 'dark')))
print(delete_setting(test_settings, 'volume'))
print(view_settings(test_settings))

