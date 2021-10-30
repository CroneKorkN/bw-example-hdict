hdict = libs.hdict.hdict

nodes = {
    'node-1': {
        'hostname': "localhost",
        'bundles': {
            'test',
        },
        'metadata': {
            'set': {
                hdict({
                    'a': 1,
                    'b': {
                        'c': 3,
                    },
                }),
                hdict({
                    'a': 2,
                    'b': {
                        'c': 4,
                    },
                }),
            },
        },
    },
}
