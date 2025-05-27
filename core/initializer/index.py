from datetime import date
from typing import List

import yaml

from core.model.index import ReportRow, Report
from core.report.report_enhancement import ReportEnhancement
from core.report.report_pdf_processor import ReportPdfProcessor, ReportInformationDTO
from core.report.row_report_enhancer import DescriptionHandler, CapitalizeDescription, RateOverEndTime
from read_excel import read_file
import pandas as pd

with open("./resources/config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

def parser_to_report_row(row):
    return ReportRow(
        row["Data"],
        row["Hora de Início"],
        row["Hora de Término"],
        row["Duração"],
        row["Salário"],
        0,
        "" if pd.isna(row["Descrição"]) else row["Descrição"]
    )


def create_report(items: List[ReportRow]) -> Report:
    return Report(
        date.today(),
        "Invoice#1123C",
        config["developer"]["name"],
        config["developer"]["address"],
        config["developer"]["city"],
        config["costumer"]["company_name"],
        config["costumer"]["address"],
        config["costumer"]["city"],
        config["account"]["bank_name"],
        config["account"]["pixkey"],
        items,
        None,
        None,
        None
    )


def init():
    file = "./resources/ml-report.xls"
    cols = ["Data", "Hora de Início", "Hora de Término", "Duração", "Salário", "Descrição"]

    items = read_file(file, cols)
    items.pop()

    parsed_items = [(parser_to_report_row(item)) for item in items]

    report = create_report(parsed_items)

    report_rows_handlers = [DescriptionHandler(), RateOverEndTime(), CapitalizeDescription() ]
    report_enhancement = ReportEnhancement(report_rows_handlers)

    report_enhancement.enhance_data(report)

    report_pdf_processor = ReportPdfProcessor()

    report_dto = ReportInformationDTO(report, "./resources", "report-template.html", )

    report_pdf_processor.generate_report(report_dto)

init()