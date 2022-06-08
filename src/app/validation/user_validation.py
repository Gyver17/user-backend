registerSchema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'lastName': {'type': 'string'},
        'email': {
            "type": "object",
             "properties": {
                "body": {
                    "type": "string"
                },
                "domain": {
                    "type": "string"
                }
            },
            "required": [ "body", "domain"]
        },
        },
        'phone': {'type': 'string'},
        'password': {'type': 'string'},
    'required': ['name', 'lastName', 'email', 'phone', 'password']
}

updateSchema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'lastName': {'type': 'string'},
        'email': {
            "type": "object",
             "properties": {
                "body": {
                    "type": "string"
                },
                "domain": {
                    "type": "string"
                }
            },
            "required": [ "body", "domain"]
        },
        },
        'phone': {'type': 'string'},
    'required': ['name', 'lastName', 'email', 'phone']
}

loginSchema = {
    'type': 'object',
    'properties': {
        'email': {
            "type": "object",
             "properties": {
                "body": {
                    "type": "string"
                },
                "domain": {
                    "type": "string"
                }
            },
            "required": [ "body", "domain"]
        },
        },
        'password': {'type': 'string'},
    'required': ['email', 'password']
}