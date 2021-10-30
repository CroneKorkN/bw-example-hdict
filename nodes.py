hashable = libs.hashable.hashable

nodes = {
    'node-1': {
        'hostname': "localhost",
        'bundles': {
            'test',
        },
        'metadata': {
            'dicts': {
                hashable({
                    'a': 1,
                    'b': {
                        'c': 3,
                    },
                }),
                hashable({
                    'a': 2,
                    'b': {
                        'c': 4,
                    },
                }),
            },
            'sets': {
                hashable({3,4,5}),
            },
        },
    },
}
