hdict = libs.hdict.hdict

groups = {
    'all': {
        'member_patterns': (
            r".*",
        ),
        'metadata': {
            'set': {
                hdict({
                    'a': 10,
                    'b': {
                        'c': 11,
                    },
                }),
                hdict({
                    'a': 12,
                    'b': {
                        'c': 13,
                    },
                }),
            },
        },
    },
}
