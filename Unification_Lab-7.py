def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = substitute(x, subst)
    y = substitute(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        if occurs(x, y, subst):
            return None
        subst[x] = y
        return subst

    if is_variable(y):
        if occurs(y, x, subst):
            return None
        subst[y] = x
        return subst

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0]:
            return None

        if len(x[1]) != len(y[1]):
            return None

        
        for a, b in zip(x[1], y[1]):
            result = unify(a, b, subst)

            if result is None:
                return None

            subst = result

        return subst

    return None


def is_variable(x):
    return isinstance(x, str) and x.islower() and x not in ["apple"]


def substitute(x, subst):
    while isinstance(x, str) and x in subst:
        x = subst[x]

    if isinstance(x, tuple):
        return (x[0], [substitute(a, subst) for a in x[1]])

    return x


def occurs(var, term, subst):
    term = substitute(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(var, a, subst) for a in term[1])

    return False


print("UNIFICATION ALGORITHM")



expr1 = ("Eats", ["x", "Apple"])
expr2 = ("Eats", ["Rambo", "y"])

result = unify(expr1, expr2)

if result is None:
    print("Unification Failed!")
else:
    print("Unification Successful!")
    print("Substitution Set:", result)
    print("Unified Expression:", substitute(expr1, result))