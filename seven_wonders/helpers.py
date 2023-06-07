from seven_wonders.Resources import ResourceOptions, ResourceOption
from seven_wonders.Science import Science

def parse_string_to_resource(string):
    """Parse a string into a ResourceOptions object.

    Args:
        string (str): The string to parse.

    Returns:
        ResourceOptions: The parsed ResourceOptions object.
    """
    if string == '' or string == 0:
        return ResourceOptions(ResourceOption())
    elif '/' in string:
        options = []
        for option in string.split('/'):
            new_options = parse_string_to_resource(option)
            options.append(*new_options.options)
        return ResourceOptions(*options)
    else:
        resources = ResourceOption()
        for resource in string.split(','):
            resource = resource.strip()
            if resource[0].isdigit():
                count = int(resource[0])
                resource = resource[2:]
            else:
                count = 1
            resources += ResourceOption(**{resource: count})
        return ResourceOptions(resources)
    
def parse_string_to_science(string):
    """Parse a string into a Science object.

    Args:
        string (str): The string to parse.

    Returns:
        Science: The parsed Science object.
    """
    if string == '' or string == 0:
        return Science()
    else:
        string = string.strip()
        if string[0].isdigit():
            count = int(string[0])
            discovery = string[2:]
        else:
            count = 1
            discovery = string
        return Science(**{discovery: count})
    
def parse_card_type(string):
    """Parse a string into a card type.

    Args:
        string (str): The string to parse.

    Returns:
        str: The parsed card type.
    """
    if string == 'Raw Material' or string == 'raw_material':
        return 'raw_material'
    elif string == 'Manufactured Good' or string == 'manufactured_good':
        return 'manufactured_good'
    elif string == 'Civilian Structure' or string == 'civilian_structure':
        return 'civilian_structure'
    elif string == 'Scientific Structure' or string == 'scientific_structure':
        return 'scientific_structure'
    elif string == 'Commercial Structure' or string == 'commercial_structure':
        return 'commercial_structure'
    elif string == 'Military Structure' or string == 'military_structure':
        return 'military_structure'
    elif string == 'Guild' or string == 'guild':
        return 'guild'
    else:
        raise ValueError(f'Invalid card type: {string}.')