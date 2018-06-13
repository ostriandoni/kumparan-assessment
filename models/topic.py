from datetime import datetime

topic = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods':  ['GET', 'DELETE'],
    'schema': {
        'createdAt': {
            'type': 'datetime',
            'default': datetime.utcnow()
        },
        'title': {
            'type': 'string',
            'required': True
        },
        'tag': {
            'type': 'string',
            'required': True,
            'unique': True
        },
        'categories': {
            'type': 'dict',
            'schema': {
                'latest': {
                    'type': 'list',
                    'default': []
                },
                'popular': {
                    'type': 'list',
                    'default': []
                }
            },
        }
    }
}
