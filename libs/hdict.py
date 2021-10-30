import json
from functools import total_ordering


@total_ordering
class hdict(dict):
    def _json(self):
        return json.dumps(self, sort_keys=True)

    def __lt__(self, other):
        return self._json() < other._json()

    def __eq__(self, other):
        return self._json() == other._json()

    def __hash__(self):
        return hash(self._json())
