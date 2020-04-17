from lexer import Token
from rules import Rule
import string


class CheckFunctionsCount(Rule):
    def __init__(self):
        super().__init__()
        self.depends_on = ["IsFuncDeclaration"]

    def run(self, context):
        if context.scope != None and context.scope.name == "GlobalScope":
            if context.scope.functions > 5:
                context.new_error("TOO_MANY_FUNCS", context.peek_token(0))
        return False, 0