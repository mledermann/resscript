import unittest
import resscript


class TestTaskDef(unittest.TestCase):
    def test_one_task(self):

        @resscript.task("1")
        def run_me(x):
            print(x)

        self.assertEqual(resscript.task_list["1"].__name__, 'run_me')

