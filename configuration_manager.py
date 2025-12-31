def add_setting(settings, item):
    key, value = item
    key = key.lower()
    value = value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists!"
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, item):
    key, value = item
    key = key.lower()
    value = value.lower()
    
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update."
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings, key):
    key = key.lower()
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    return f"Setting '{key}' does not exist!"


def view_setting(settings):
    if not settings:
        return "No setting is available"
    output = "Current user settings:"
    for key, value in settings.items():
        output += f"\n{key.capitalize()}: {value}"
    return output


test_settings = {}

print(add_setting(test_settings, ("Theme", "Dark")))
print(add_setting(test_settings, ("Notification", "Enabled")))
print(update_setting(test_settings, ("Theme", "Light")))
print(view_setting(test_settings))
print(delete_setting(test_settings, "Theme"))
print(view_setting(test_settings))
  
    
    
    
    
    
    
    