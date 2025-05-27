from abc import ABC, abstractmethod
from datetime import time

from core.model.index import ReportRow

class RowReportHandler(ABC):

    @abstractmethod
    def handle(self, row_report: ReportRow):
        pass

class DescriptionHandler(RowReportHandler):
    DEFAULT_DESCRIPTION_MESSAGE = "Trabalhando no projeto MoneyLaw"

    def handle(self, row_report: ReportRow):
        if row_report.description == "":
            row_report.set_description(self.DEFAULT_DESCRIPTION_MESSAGE)

class RateOverEndTime(RowReportHandler):

    RATE_APPLY_CUTOFF_TIME = time(6, 00, 00)
    RATE = 0.5

    def handle(self, row_report: ReportRow):
        if row_report.end_time < self.RATE_APPLY_CUTOFF_TIME :
            row_report.set_additional(row_report.salary * self.RATE)

class CapitalizeDescription(RowReportHandler):

    def handle(self, row_report: ReportRow):
        if row_report.description:
            row_report.set_description(row_report.description.capitalize())