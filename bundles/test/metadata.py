hashable = repo.libs.hashable.hashable


defaults = {
    'dicts': {
        hashable({'foo': 'bar'}),
    },
    'sets': {
        hashable({1,2,3}),
    },
}


@metadata_reactor
def test(metadata):
    return {
        'dicts': {
            hashable({'alice': 'bob', '1': {'2': '3'}}),
            hashable({'fix': 'foxi'}),
        },
        'sets': {
            hashable({2,3,4}),
        },
    }
