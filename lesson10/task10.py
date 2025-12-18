from __future__ import annotations
from typing import Any

class PowerSet:

    def __init__(self) -> None:
        self._set = {}

    def size(self) -> int:
        return len(self._set)

    def put(self, value: Any) -> None:
        self._set[value] = True

    def get(self, value: Any) -> bool:
        return self._set.get(value, False)

    def remove(self, value: Any) -> bool:
        return self._set.pop(value, False)

    def intersection(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for key in self._set:
            if set2.get(key):
                result.put(key)
        return result

    def union(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for key in self._set:
            result.put(key)
        for key in set2._set:
            result.put(key)
        return result

    def difference(self, set2: PowerSet) -> PowerSet:
        result = PowerSet()
        for key in self._set:
            if not set2.get(key):
                result.put(key)
        return result

    def issubset(self, set2: PowerSet) -> bool:
        diff = set2.difference(self)
        return diff.size() == 0

    def equals(self, set2: PowerSet) -> bool:
        if set2.size() != self.size():
            return False
        difference = set2.difference(self)
        return difference.size() == 0


