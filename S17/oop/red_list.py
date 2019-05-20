class RedList(list):
    def __repr__(self):
        mx_val = str(max(self))
        repr_default = super().__repr__()

        repr_new = repr_default.replace(mx_val, "\033[31;2m" + mx_val + "\033[0m")

        return repr_new


lst = RedList([1, 2, 3, 4, 5, 6])
