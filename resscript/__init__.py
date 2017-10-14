"""
A module for controlling the execution of Python CLI scripts by breaking the script into resumable list of tasks.
"""

import os
from errors import TaskDefinitionError

__version__ = "0.1"

task_list = {}


class ResumableTaskList(object):
    """
    Base object for a resumable set of Tasks to be executed in sequence.
    """

    def __init__(self, progress_dir=None):
        self.progress_dir = progress_dir or os.getcwd()


def task(order_number):
    def wrap_task(task_function):
        if order_number in task_list:
            raise TaskDefinitionError("Multiple tasks defined for the same ordinal.")

        task_list[order_number] = task_function

        def exec_task(*args, **kwargs):
            return task_function(*args, **kwargs)

        return exec_task
    return wrap_task


if __name__ == '__main__':
    print(__doc__)
