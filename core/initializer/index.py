import yaml
import json

from core.report.report_enhancement import ReportEnhancement
from core.report.report_factory import ReportFactory
from core.report.report_pdf_processor import ReportPdfProcessor, ReportInformationDTO
from core.report.row_report_enhancer import DescriptionHandler, CapitalizeDescription, RateOverEndTime
from read_excel import read_file

with open("./resources/config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

def init():
    file = "./resources/ml-report.xls"
    cols = ["Data", "Hora de Início", "Hora de Término", "Duração", "Salário", "Descrição"]

    items = read_file(file, cols)
    items.pop()

    report_factory = ReportFactory()
    report = report_factory.create_report(config, items)

    report_enhancement = ReportEnhancement([DescriptionHandler(), RateOverEndTime(), CapitalizeDescription()])
    report_enhancement.enhance_data(report)

    print(json.dumps(report.to_dict(), default=str, indent=2))

    report_pdf_processor = ReportPdfProcessor()
    report_dto = ReportInformationDTO(report, "./resources", "report-template.html", )

    report_pdf_processor.generate_report(report_dto)

init()