
class QuickSetAll:
    def __init__(self):
        self.epoch = 0
        self.lookup = {}

    def set_all(self, val):
        self.epoch += 1
        self.set_all_val = val

    def set(self, key, val):
        self.lookup[ key ] = ( val, self.epoch )

    def lookup(self, key):
        val = self.lookup.get( key, None)
        if val:
            if val[1] == self.epoch:
                return val[0]
            # no longer needed - epoch is too old.
            sef.lookup.delete( key )

        if self.epoch > 0:
            return self.set_all_val
        return None
