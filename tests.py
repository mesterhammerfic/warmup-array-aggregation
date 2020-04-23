import numpy as np
from IPython.display import display, Markdown


class Test():

    def __init__(self):
        self.wrong_count = 0
        self.data = {'failed': {}}
        self.data['random'] = {'failed': {}}

    def assert_equals(self, answer, solution):
        if self.broadcast:
            answer = list(answer)

        if np.all(solution == answer):
            return 1
        else:
            return 0

    def update_data(self, test_number, result, random=False, prompt=[]):
        if result == 0:
            failed = True
        else:
            failed = False

        if random:
            self.data['random'][test_number] = result
            if failed:
                self.data['random']['failed'][test_number] = prompt

        else:
            self.data[test_number] = result
            if failed:
                self.data['failed'][test_number] = prompt

    def print_results(self):
        check = '✅'
        X = '❌'
        header_template = '''## {}\n\n--------------- \n \n <details><summary>Test Results</summary>'''
        test_template = '\n\n{} {}Test {} {}'
        describe = '\n >*{} tests {}*'
        wrong_count = 0
        for key in self.data.keys():
            if key in ['failed', 'random']:
                continue
            if self.data[key] == 0:
                wrong_count += 1
                header_template += test_template.format(X, '', key, 'failed.')
            else:
                header_template += test_template.format(
                    check, '', key, 'passed!')

        if wrong_count != 0:
            fail_describe = describe.format(wrong_count, 'failed')
            header = 'Failed' + fail_describe
        else:
            pass_describe = describe.format(len(self.data) - 2, 'passed')
            header = 'Passed!' + pass_describe

        if self.random:
            random_header = '</details>\n### Randomly Generated Tests –– {}\n\n--------------- \n\n<details><summary>Random Tests Results</summary>'
            random_wrong_count = 0

            for key in self.data['random'].keys():
                if key == 'failed':
                    continue
                if self.data['random'][key] == 0:
                    wrong_count += 1
                    random_header += test_template.format(
                        X, 'Random ', key, 'failed.')
                    random_wrong_count += 1
                else:
                    random_header += test_template.format(
                        check, 'Random ', key, 'passed!')

            if random_wrong_count != 0:
                random_header = random_header.format(
                    'Failed' + describe.format(random_wrong_count, 'failed.'))
            else:
                random_header = random_header.format(
                    'Passed' + describe.format(len(self.data['random'])-1, 'passed.'))

            header_template += random_header

        mark = Markdown(header_template.format(header))
        display(mark)


class ArrayTest(Test):

    def __init__(self):
        super().__init__()

    def solution_function(self, arr1, arr2):
        return np.sum(arr1) + np.sum(arr2)

    def test_1(self):
        answer = self.function([1, 2, 3], [4, 5, 6])
        solution = self.solution_function([1, 2, 3], [4, 5, 6])
        result = self.assert_equals(answer, solution)
        self.update_data(1, result, prompt=[[1, 2, 3], [4, 5, 6]])

    def test_2(self):
        answer = self.function([-1, -2, -3], [-4, -5, -6])
        solution = self.solution_function([-1, -2, -3], [-4, -5, -6])
        result = self.assert_equals(answer, solution)
        self.update_data(2, result, prompt=[[-1, -2, -3], [-4, -5, -6]])

    def test_3(self):
        answer = self.function([0, 0, 0], [4, 5, 6])
        solution = self.solution_function([0, 0, 0], [4, 5, 6])
        result = self.assert_equals(answer, solution)
        self.update_data(3, result, prompt=[[0, 0, 0], [4, 5, 6]])

    def test_4(self):
        answer = self.function([100, 200, 300], [400, 500, 600])
        solution = self.function([100, 200, 300], [400, 500, 600])
        result = self.assert_equals(answer, solution)
        self.update_data(4, result, prompt=[[100, 200, 300], [400, 500, 600]])

    def test_5(self):
        answer = self.function([9.299999999999933, 7.899999999999935, -5.500000000000016],
                               [-6.800000000000011, -6.400000000000013, -5.900000000000015])
        solution = self.solution_function([9.299999999999933, 7.899999999999935, -5.500000000000016],
                                          [-6.800000000000011, -6.400000000000013, -5.900000000000015])
        result = self.assert_equals(answer, solution)
        self.update_data(5, result, prompt=[[9.299999999999933, 7.899999999999935, -5.500000000000016],
                                            [-6.800000000000011, -6.400000000000013, -5.900000000000015]])

    def test_6(self):
        answer = self.function([-3, -8, -10], [-5, -9, -6])
        solution = self.solution_function([-3, -8, -10], [-5, -9, -6])
        result = self.assert_equals(answer, solution)
        self.update_data(6, result, prompt=[[-3, -8, -10], [-5, -9, -6]])

    def test_7(self):
        answer = self.function([1, 2, 3], [-1, -2, -3])
        solution = self.solution_function([1, 2, 3], [-1, -2, -3])
        result = self.assert_equals(answer, solution)
        self.update_data(7, result, prompt=[[1, 2, 3], [-1, -2, -3]])

    def random_tests(self):

        # Different range paramaters for testings
        ranges = [(1, 10000, 1), (-10, 10, 1), (-1, 1, .01), (-20, 20, .1)]
        # Index that will be used to iterate over paramaters
        range_index = 0
        # Initial arrays
        options = [list(np.random.choice(list(np.arange(1, 50)), size=3))
                   for x in range(200)]

        # 100 iterations that sum 100 different random pairs of arrays
        for i in range(100):
            data = [options[np.random.choice(
                list(range(len(options))))] for x in range(2)]
            solution = self.solution_function(data[0], data[1])
            answer = self.function(data[0], data[1])
            result = self.assert_equals(answer, solution)
            self.update_data(i+1, result, random=True,
                             prompt=[data[0], data[1]])

            # Every 20 iterations the options are updates using our range paramaters
            if (i+1) % 20 == 0:
                options = [list(np.random.choice(list(np.arange(ranges[range_index][0],
                                                                ranges[range_index][1],
                                                                ranges[range_index][2])),
                                                 size=3))
                           for x in range(200)]

    def run(self, function, random=False, broadcast=False):
        if broadcast:

            def broadcast_function(a, b):
                a = np.asarray(a)
                b = np.asarray(b)
                return list(a+b)

            self.solution_function = broadcast_function
        self.broadcast = broadcast
        self.function = function
        self.random = random
        self.test_1()
        self.test_2()
        self.test_3()
        self.test_4()
        self.test_5()
        self.test_6()
        self.test_7()

        if random:
            self.random_tests()

        self.print_results()


class MultiplyTest(Test):
    def __init__(self):
        super().__init__()

    def solution_function(self, a, b):
        return a * b

    def test_1(self):
        if self.broadcast:
            answer = self.function([4, 7, 10], [90, 3, 2])
            solution = self.solution_function([4, 7, 10], [90, 3, 2])
            prompt = [[4, 7, 10], [90, 3, 2]]
        else:
            answer = self.function(6, 4)
            solution = self.solution_function(6, 4)
            prompt = [6, 4]
        result = self.assert_equals(answer, solution)
        self.update_data(1, result, prompt=prompt)

    def test_2(self):
        if self.broadcast:
            answer = self.function([30, 13, 70], [1, 1, 1])
            solution = self.solution_function([30, 13, 70], [1, 1, 1])
            prompt = [[30, 13, 70], [1, 1, 1]]
        else:
            answer = self.function(1000, .5)
            solution = self.solution_function(1000, .5)
            prompt = [1000, .5]

        result = self.assert_equals(answer, solution)
        self.update_data(2, result, prompt=prompt)

    def test_3(self):
        if self.broadcast:
            answer = self.function([0, 0, 0], [0, 0, 0])
            solution = self.solution_function([0, 0, 0], [0, 0, 0])
            prompt = [[0, 0, 0], [0, 0, 0]]
        else:
            answer = self.function(-1, 0)
            solution = self.solution_function(-1, 0)
            prompt = [-1, 0]
        result = self.assert_equals(answer, solution)
        self.update_data(3, result, prompt=prompt)

    def random_tests(self):
        if not self.broadcast:

            options = np.arange(-5000, 5000)
            for i in range(100):
                data = np.random.choice(options, size=2)
                answer = self.function(data[0], data[1])
                solution = self.solution_function(data[0], data[1])
                result = self.assert_equals(answer, solution)
                self.update_data(i, result, random=True,
                                 prompt=[data[0], data[1]])
                if i % 50 == 0:
                    options = np.arange(-1000, 1000, .1)
        else:
            options = [list(np.random.choice(list(np.arange(-5000, 5000)), size=3))
                       for x in range(200)]
            for i in range(100):
                data = [options[np.random.choice(
                    list(range(len(options))))] for x in range(2)]
                answer = self.function(data[0], data[1])
                solution = self.solution_function(data[0], data[1])
                result = self.assert_equals(answer, solution)
                self.update_data(i, result, random=True,
                                 prompt=[data[0], data[1]])
                if i % 50 == 0:
                    options = [list(np.random.choice(list(np.arange(-1000, 1000, .1)), size=3))
                               for x in range(200)]

    def run(self, function, random=False, broadcast=False):
        self.broadcast = broadcast
        if broadcast:
            def broadcast_function(a, b):
                a = np.asarray(a)
                b = np.asarray(b)
                return list(a * b)
            self.solution_function = broadcast_function

        self.random = random
        self.function = function
        self.test_1()
        self.test_2()
        self.test_3()
        if random:
            self.random_tests()

        self.print_results()
