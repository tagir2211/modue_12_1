import unittest

import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        '''
        Test class Runner, functoin walk
        :return:
        '''
        t_walk = runner.Runner('Test')
        for _ in range(1, 11):
            t_walk.walk()
        self.assertEqual(t_walk.distance, 50)

    def test_run(self):
        '''
        Test class Runner, functoin run
        :return:
        '''
        t_run = runner.Runner('Test')
        for _ in range(1, 11):
            t_run.run()
        self.assertEqual(t_run.distance, 100)

    def test_challenge(self):
        t_walk = runner.Runner('Wallker')
        t_run = runner.Runner('Runner')
        for _ in range(1, 11):
            t_walk.walk()
            t_run.run()
        self.assertNotEqual(t_run.distance, t_walk.distance)


if __name__ == '__main__':
    unittest.main()
