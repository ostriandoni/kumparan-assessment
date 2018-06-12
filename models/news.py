from datetime import datetime

news = {
    'resource_methods': ['GET', 'POST', 'DELETE'],
    'item_methods':  ['GET', 'DELETE'],
    'schema': {
        'link': {
            'type': 'string',
            'unique': True,
            'required': True
        },
        'createdAt': {
            'type': 'datetime',
            'default': datetime.utcnow()
        },
        'title': {
            'type': 'string',
            'required': True
        },
        'content': {
            'type': 'string',
            'required': True
        },
        'attachments': {
            'type': 'list',
            'default': []
        },
        'writer': {
            'type': 'string',
            'required': True
        },
        'editor': {
            'type': 'string',
            'required': True
        },
        'reporter': {
            'type': 'string'
        },
        'like': {
            'type': 'integer',
            'default': 0
        },
        'topics': {
            'type': 'list',
            'required': True
        },
        'comments': {
            'type': 'list',
            'default': []
        },
        'status': {
            'type': 'string',
            'allowed': ['draft', 'deleted', 'publish']
        }
    }
}
