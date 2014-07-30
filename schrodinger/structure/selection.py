from schrodinger.structutils.analyze import evaluate_smarts
from ...structure.selection import Selection


class SelfSelection(Selection):
    def _execute(self, st):
        return [atom.index for atom in st.atom]


class SmartsSelection(Selection):
    def __init__(self, expression):
        self.expression = expression

    def _execute(self, st):
        matches = evaluate_smarts(st, self.expression, first_match_only=True,
                                  unique_sets=True)
        if len(matches) != 1:
            template = 'SMARTS expression "{}" '
            template += ('did produce more than one match'
                         if len(matches) > 1
                         else 'did not produce a match')
            raise ValueError(template.format(self.expression))
        return matches[0]