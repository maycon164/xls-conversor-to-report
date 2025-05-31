
from core.config.config_loader import ConfigLoader
from core.report.report_enhancement import ReportEnhancement
from core.report.report_factory import ReportFactory
from core.report.report_pdf_processor import ReportPdfProcessor, ReportInformationDTO
from core.report.report_xlsx_reader import ReportXLSXReader
from core.report.row_report_enhancer import DescriptionHandler, CapitalizeDescription, RateOverEndTime


def init():
    file = "./resources/ml-report.xls"
    cols = ["Data", "Hora de Início", "Hora de Término", "Duração", "Salário", "Descrição"]
    config_file_path = "./resources/config.yml"

    report_reader = ReportXLSXReader()
    rows = report_reader.read_file(file, cols)

    config_loader = ConfigLoader()
    config = config_loader.load(config_file_path)

    report_factory = ReportFactory()
    report = report_factory.create_report(config, rows)

    report_enhancement = ReportEnhancement([DescriptionHandler(), RateOverEndTime(), CapitalizeDescription()])
    report_enhancement.enhance_data(report)

    report_pdf_processor = ReportPdfProcessor()
    report_dto = ReportInformationDTO(report, "./resources", "report-template.html", )

    report_pdf_processor.generate_report(report_dto)

init()