hdict = repo.libs.hdict.hdict


defaults = {
    'set': {
        hdict({'foo': 'bar'}),
    }
}


@metadata_reactor.provides(
    'set',
)
def test(metadata):
    return {
        'set': {
            hdict({'alice': 'bob', '1': {'2': '3'}}),
            hdict({'fix': 'foxi'}),
        }
    }
