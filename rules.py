from datetime import time

from core.model.index import ReportRow

DEFAULT_DESCRIPTION_MESSAGE = "Trabalhando no projeto MoneyLaw"

def check_description(item):
    if item["description"] == "":
        item["description"] = DEFAULT_DESCRIPTION_MESSAGE

def apply_rate_over_end_time(item):

    if item["end_time"] < time(6, 00, 00):
        item["additional"] = item["salary"] * 0.5

def capitalize_description(item):
    if item["description"]:
        item["description"] = item["description"].capitalize()

## Chain of responsability
def make_handler(*rules):

    def handlers(report_row: ReportRow):
        for rule in rules:
            rule(report_row)
        return report_row

    return handlers

apply_rules = make_handler(check_description, apply_rate_over_end_time, capitalize_description)
