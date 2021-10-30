hashable = libs.hashable.hashable

groups = {
    'all': {
        'member_patterns': (
            r".*",
        ),
        'metadata': {
            'dicts': {
                hashable({
                    'a': 10,
                    'b': {
                        'c': 11,
                    },
                }),
                hashable({
                    'a': 12,
                    'b': {
                        'c': 13,
                    },
                }),
            },
            'sets': {
                hashable({5,6,7}),
            },
        },
    },
}
