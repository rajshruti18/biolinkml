import unittest

from biolinkml.generators.jsonschemagen import JsonSchemaGenerator
from biolinkml.generators.pythongen import PythonGenerator
from tests.utils.python_comparator import compare_python
from tests.utils.test_environment import TestEnvironmentTestCase
from tests.test_issues.environment import env


class Issue120TestCase(TestEnvironmentTestCase):
    env = env

    def test_issue_120(self):
        """ Courses not inlining """
        env.generate_single_file('issue_120.py',
                                 lambda: PythonGenerator(env.input_path('issue_120.yaml')).serialize(),
                                 value_is_returned=True, comparator=compare_python)

        env.generate_single_file('issue_120.json',
                                 lambda: JsonSchemaGenerator(env.input_path('issue_120.yaml')).serialize(),
                                 value_is_returned=True)


if __name__ == '__main__':
    unittest.main()
