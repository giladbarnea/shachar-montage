def outside(a):
    def _inside(_a):
        return _a + 1
    return inside(a) * 2