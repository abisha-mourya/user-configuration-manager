test_settings=({"theme":"light","volume":"medium"})
def add_setting(settings,new_setting):
    key,value=new_setting
    key=key.lower()
    value=value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key]=value
    return f"Setting '{key}' added with value '{value}' successfully!"
print(add_setting({'theme':'light'},('THEME','dark')))
print(add_setting({'theme':'light'},('volume','high')))

def update_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"
print(update_setting({'theme': 'light'}, ('volume', 'high')))
print(update_setting({'theme': 'light'}, ('volume', 'high')))

def delete_setting(settings, key):
    key = key.lower()

    if key not in settings:
        return "Setting not found!"

    del settings[key]
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result