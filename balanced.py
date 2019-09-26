"""
Reginald Braithwaite's "Pattern Matching and Recursion" in Python
See http://raganwald.com/2018/10/17/recursive-pattern-matching.html
"""


def simple_balanced(s):
    """
    A string is balanced iff:
     - there are an equal number of opening and closing parens
     - For all prefixes there are at least as many opening as closing parens
    """
    open_count = 0
    close_count = 0
    for c in s:
        if c == "(":
            open_count += 1
        elif c == ")":
            close_count += 1
        else:
            return False

        if close_count > open_count:
            return False

    return open_count == close_count


"""
A "pattern" is a function that takes a single string as input. If the pattern
matches, the function returns the substring that matches. If it does not match
the pattern returns False.
"""


def startswith(target):
    """
    Returns a pattern that matches if input starts with target.
    """
    return lambda s: s.startswith(target) and target


def follows(*patterns):
    """
    Returns a pattern that matches if all patterns occur in succession and
    returns the concatenated match.
    """

    def f(s):
        match_length = 0
        remaining = s

        for pattern in patterns:
            matched = pattern(remaining)
            if not matched:
                return False
            match_length += len(matched)
            remaining = s[match_length:]

        return s[:match_length]

    return f


def cases(*patterns):
    """
    Returns a pattern that matches the longest match in a list of patterns.
    """

    def f(s):
        matches = [p(s) for p in patterns if p(s)]
        if not matches:
            return False
        else:
            return sorted(matches, key=len)[-1]

    return f


def balancedprefix(s):
    """
    A pattern that matches if a prefix of s is a balanced set of parentheses.
    """
    return cases(
        startswith("()"),     # 1. trivial case
        follows(              # 2. () followed by balanced string
            startswith("()"),
            balancedprefix
        ),
        follows(              # 3. balanced string enclosed by ()
            startswith("("),
            balancedprefix,
            startswith(")")
        ),
        follows(              # 4. balanced string enclosed by ()
            startswith("("),  # followed by a balanced string
            balancedprefix,
            startswith(")"),
            balancedprefix,
        ),
    )(s)


def entirely(pattern):
    """
    Returns a pattern that matches if the entire string matches the pattern.
    """

    def f(s):
        matched = pattern(s)
        return (matched == s) and matched

    return f


balanced = entirely(balancedprefix)
