import time
import unittest


class MyTestCase(unittest.TestCase):
    def test1(self):
        a = [1, 2, 3]
        b = [3, 4, 5]
        start_time_a = time.time()
        a.remove(1)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(5)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b

    def test2(self):
        a = [1, 2, 3]
        b = [3, 4, 5, 10, 11, 1101010101, 12323123]
        start_time_a = time.time()
        a.remove(1)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(12323123)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b

    def test3(self):
        a = [1, 2, 3, 1031023, 1032103, 1023123, 123123, 123, 3213213, 1231231, 12313213, 3123123213]
        b = [3, 4, 5, 10, 11, 1101010101, 12323123]
        start_time_a = time.time()
        a.remove(12313213)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(12323123)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b

    def test4(self):
        a = [1, 2, 3, 1031023, 1032103, 1023123, 123123, 123, 3213213, 1231231, 12313213, 3123123213]
        b = [3]
        start_time_a = time.time()
        a.remove(12313213)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(3)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b


    def test5(self):
        a = [1, 2, 3, 1031023, 1032103, 1023123, 123123, 123, 3213213, 1231231, 12313213, 3123123213, 412412, 4214, 424124, 412412]
        b = [3, 13, 3213, 1241]
        start_time_a = time.time()
        a.remove(412412)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(1241)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b

    def test6(self):
        a = [1, 2, 3, 1031023, 1032103, 1023123, 123123, 123, 3213213, 1231231, 12313213, 3123123213, 412412, 4214, 424124, 412412, 4124124,421, 4214,1421, 412412, 4124214, 5215125, 414124124124, 4124124, 4124124124]
        b = [3, 13, 3213, 1241, 412414, 41241, 41241]
        start_time_a = time.time()
        a.remove(4124124124)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(1241)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b

    def test7(self):
        a = [1, 2, 3, 1031023, 1032103, 1023123, 123123, 123, 3213213, 1231231, 12313213, 3123123213, 412412, 4214, 424124, 412412, 4124124,421, 4214,1421, 412412, 4124214, 5215125, 414124124124, 4124124, 4124124124]
        b = [3]
        start_time_a = time.time()
        a.remove(4124124124)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(3)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b

    def test8(self):
        a = [1, 424124, 412412, 4124124,421, 4214,1421, 412412, 4124214, 5215125, 414124124124, 4124124, 4124124124]
        b = [3, 5]
        start_time_a = time.time()
        a.remove(4124124124)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(5)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b


    def test9(self):
        a = [1, 424124, 412412, 4124124,421, 4214,1421, 412412, 4124214, 5215125, 414124124124, 4124124, 4124124124]
        b = [3, 5, 412412, 412412]
        start_time_a = time.time()
        a.remove(4124124124)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(5)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b


    def test10(self):
        a = [1, 424124, 412412, 4124124,421, 4214,1421, 412412, 4124214, 5215125, 414124124124, 4124124, 4124124124]
        b = [3, 5, 4140, 41204, 412414]
        start_time_a = time.time()
        a.remove(4124124124)
        end_time_a = time.time()
        start_time_b = time.time()
        b.remove(412414)
        end_time_b = time.time()
        c = int((end_time_a - start_time_a) * 1000)
        b = int((end_time_b - start_time_b) * 1000)
        assert c == b
if __name__ == '__main__':
    unittest.main()
