"""
Bridge pattern example.
"""
from abc import ABCMeta, abstractmethod


class Reporter(metaclass=ABCMeta):

    @abstractmethod
    def report_good_news(self):
        raise NotImplementedError()

    @abstractmethod
    def report_bad_news(self):
        raise NotImplementedError()


class FairReporter(Reporter):
    def report_good_news(self, news):
        print(news)

    def report_bad_news(self, news):
        print(news)


class PositiveBiasReporter(Reporter):
    def report_good_news(self, news):
        print(news)

    def report_bad_news(self, news):
        print("Nothing to report.")


class News(metaclass=ABCMeta):

    def __init__(self, reporter, news):
        self._reporter = reporter
        self.news = news

    @abstractmethod
    def report(self):
        raise NotImplementedError()

class BadNews(News):

    def report(self):
        return self._reporter.report_bad_news(self.news)


reporter1 = FairReporter()
reporter2 = PositiveBiasReporter()
BadNews(reporter1, "Out of money").report()
BadNews(reporter2, "Out of money").report()
