from datetime import datetime

topic = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
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
            'required': True
        },
        'categories': {
            'type': 'dict',
            'schema': {
                'latest': {
                    'type': 'list'
                },
                'popular': {
                    'type': 'list'
                }
            },
        }
    }
}
