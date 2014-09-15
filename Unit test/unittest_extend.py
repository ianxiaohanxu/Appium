# -*- coding: utf-8 -*-

import unittest, time


def get_testcase_list(testsuite = None):
	caselist = []
	if isinstance(testsuite, unittest.TestCase):
		caselist.append(testsuite._testMethodName)
		return caselist
	else:
		for item in testsuite._tests:
			caselist.extend(get_testcase_list(item))
		return caselist
		
class TestReport(object):
	def __init__(self, testsuite):
		self._all = get_testcase_list(testsuite)
		self.count_of_all = len(self._all)
		self.passed = []
		self.failure = []
		self.error = []
		self.skip = []
		self.Efailure = []
		self.UEpass = []
		self.allRun = []
		self.noRun = []
		
	def get_pass(self, testresult):
		for item in testresult.passed:
			name = item[0]._testMethodName
			status = 'Pass'
			output = item[1]
			errormessage = ''
			duration = item[0].duration
			start = item[0].start_time
			end = item[0].end_time
			fstart = item[0].fstart_time
			self.passed.append([name, status, output, errormessage, duration, start, end, fstart])
			
	def get_failure(self, testresult):
		for item in testresult.failures:
			name = item[0]._testMethodName
			status = 'Fail'
			output = item[1]
			errormessage = item[2]
			duration = item[0].duration
			start = item[0].start_time
			end = item[0].end_time
			fstart = item[0].fstart_time
			self.failure.append([name, status, output, errormessage, duration, start, end, fstart])
		
	def get_error(self, testresult):
		for item in testresult.errors:
			name = item[0]._testMethodName
			status = 'Error'
			output = item[1]
			errormessage = item[2]
			duration = item[0].duration
			start = item[0].start_time
			end = item[0].end_time
			fstart = item[0].fstart_time
			self.error.append([name, status, output, errormessage, duration, start, end, fstart])
		
	def get_skip(self, testresult):
		for item in testresult.skipped:
			name = item[0]._testMethodName
			status = 'Skip'
			output = item[1]
			errormessage = ''
			duration = 0
			start = ''
			end = ''
			fstart = 0
			self.skip.append([name, status, output, errormessage, duration, start, end, fstart])
		
	def get_Efailure(self, testresult):
		for item in testresult.expectedFailures:
			name = item[0]._testMethodName
			status = 'Efail'
			output = item[1]
			errormessage = item[2]
			duration = item[0].duration
			start = item[0].start_time
			end = item[0].end_time
			fstart = item[0].fstart_time
			self.Efailure.append([name, status, output, errormessage, duration, start, end, fstart])
			
	def get_UEpass(self, testresult):
		for item in testresult.unexpectedSuccesses:
			name = item[0]._testMethodName
			status = 'UEpass'
			output = item[1]
			errormessage = ''
			duration = item[0].duration
			start = item[0].start_time
			end = item[0].end_time
			fstart = item[0].fstart_time
			self.UEpass.append([name, status, output, errormessage, duration, start, end, fstart])
		
	def statistic(self):
		self.allRun = self.passed + self.failure + self.error + self.skip + self.Efailure + self.UEpass
		self.allRun.sort(key = lambda case: case[7])
		self.count_pass = len(self.passed)
		self.count_failure = len(self.failure)
		self.count_error = len(self.error)
		self.count_skip = len(self.skip)
		self.count_Efailure = len(self.Efailure)
		self.count_UEpass = len(self.UEpass)
		self.count_allRun = len(self.allRun)
		self.count_noRun = self.count_of_all - self.count_allRun
		if self.count_noRun > 0:
			allRun = set(item[0] for item in self.allRun)
			self.noRun = set(self._all) - allRun
		
	def get_time(self, testresult):
		self.start_time = testresult.start_time
		self.end_time = testresult.end_time
		self.duration = testresult.duration
		self.name = self.start_time.replace(' ', '_')
		
	def generate_report(self):
		return
		
		
class extend_test_result(unittest.TestResult):
	def __init__(self, stream=None, descriptions=None, verbosity=None):
		super(extend_test_result, self).__init__(stream, descriptions, verbosity)
		self.passed = []
		
		
	def stop(self, test_report):
		self.end_time = time.ctime()
		self.fend_time = time.time()
		self.duration = round(self.fend_time - self.fstart_time, 1)
		test_report.get_time(self)
		test_report.get_pass(self)
		test_report.get_failure(self)
		test_report.get_error(self)
		test_report.get_skip(self)
		test_report.get_Efailure(self)
		test_report.get_UEpass(self)
		test_report.statistic()
		test_report.generate_report()
		
	def addSuccess(self, test):
		self.passed.append((test, '\n'.join(test.output)))
		
	@failfast
	def addError(self, test, err):
		"""Called when an error has occurred. 'err' is a tuple of values as
		returned by sys.exc_info().
		"""
		self.errors.append((test, '\n'.join(test.output), self._exc_info_to_string(err, test)))
		self._mirrorOutput = True

	@failfast
	def addFailure(self, test, err):
		"""Called when an error has occurred. 'err' is a tuple of values as
		returned by sys.exc_info()."""
		self.failures.append((test, '\n'.join(test.output), self._exc_info_to_string(err, test)))
		self._mirrorOutput = True



	def addSkip(self, test, reason):
		"""Called when a test is skipped."""
		self.skipped.append((test, reason))

	def addExpectedFailure(self, test, err):
		"""Called when an expected failure/error occured."""
		self.expectedFailures.append(
			(test, '\n'.join(test.output), self._exc_info_to_string(err, test)))

	@failfast
	def addUnexpectedSuccess(self, test):
		"""Called when a test was expected to fail, but succeed."""
		self.unexpectedSuccesses.append((test, '\n'.join(test.output)))
		
		
		
class extend_test_case(unittest.TestCase):
	def setUp(self):
		self.start_time = time.ctime()
		self.fstart_time = time.time()
		
	def myPrint(self, text = None):
		self.output.append(text)
		print text
		
	def tearDown(self):
		self.end_time = time.ctime()
		self.fend_time = time.time()
		self.duration = round(self.fend_time - self.fstart_time, 1)
		
		
		
