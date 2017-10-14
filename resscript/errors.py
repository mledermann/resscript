"""
Error classes.
"""


class ResumableScriptError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        return super().__str__()


class TaskDefinitionError(ResumableScriptError):
    pass
