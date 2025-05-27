from abc import ABC, abstractmethod

from core.report.report_pdf_processor import ReportInformationDTO


class ReportProcessor(ABC):

    @abstractmethod
    def generate_report(self, report_dto: ReportInformationDTO) -> None:
        pass