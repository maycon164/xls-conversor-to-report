from dataclasses import dataclass, asdict
from datetime import date, datetime
from typing import List
from datetime import time


@dataclass
class BankInformation:
    invoice_code: str
    name: str
    pix_key: str

@dataclass
class Developer:
    name: str
    address: str
    city: str
    bank_info: BankInformation

@dataclass
class Costumer:
    company_name: str
    address: str
    city: str

@dataclass
class ReportRow:
    date: str
    init_time: time
    end_time: time
    duration: datetime
    salary: float
    additional: float
    description: str
    additional: float

    def set_description(self, description: str):
        self.description = description

    def set_additional(self, additional: float):
        self.additional = additional

@dataclass
class Report:
    generated_date: date
    rows: List[ReportRow]
    developer: Developer
    costumer: Costumer
    total_hours: str
    total_value: str
    additional: str

    def get_total_hours(self):
        return self.total_hours

    def set_total_hours(self, total_hours):
        self.total_hours = total_hours

    def set_additional(self, additional):
        self.additional = additional

    def get_additional(self):
        return self.additional

    def set_total_value(self, total_value):
        self.total_value = total_value

    def get_total_value(self):
        return self.total_value

    def to_dict(self) -> dict:
        return asdict(self)


class ReportInformationDTO:
    report: Report
    resources_path: str
    template_name: str

    def __init__(self, report: Report, resources_path: str, template_name: str):
        self.report = report
        self.resources_path = resources_path
        self.template_name = template_name

    def get_report_context(self):
        return self.report.to_dict()

    def get_resources_path(self):
        return self.resources_path

    def get_template_name(self):
        return self.template_name
