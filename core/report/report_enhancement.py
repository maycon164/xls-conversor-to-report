from datetime import timedelta

from core.model.index import Report, ReportRow
from core.report.row_report_enhancer import RowReportHandler


class ReportEnhancement:
    row_handlers: list[RowReportHandler]

    def __init__(self, handlers: list[RowReportHandler]):
        self.row_handlers = handlers

    def process_handlers(self, row_report: ReportRow):
        for handler in self.row_handlers:
            handler.handle(row_report)

    def enhance_data(self, report: Report):

        for row_report in report.rows:
            self.process_handlers(row_report)

        additional = sum([row.additional for row in report.rows])
        total_value = sum([row.salary for row in report.rows])
        total_hours = sum_times([row.duration.strftime("%H:%M:%S") for row in report.rows])

        report.set_total_hours(total_hours)
        report.set_additional(additional)
        report.set_total_value(total_value)

        return report


def sum_times(times):
    mysum = timedelta()
    for i in times:
        (h, m, s) = i.split(':')
        d = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d

    # Get total hours, minutes, and seconds
    total_seconds = int(mysum.total_seconds())
    hours = total_seconds // 3600  # Number of full hours
    minutes = (total_seconds % 3600) // 60  # Remaining minutes
    seconds = total_seconds % 60  # Remaining seconds

    # Return the formatted result
    return f"{hours:02}:{minutes:02}:{seconds:02}"
