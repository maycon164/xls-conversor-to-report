from datetime import time

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

    def handlers(item):
        for rule in rules:
            rule(item)
        return item

    return handlers

apply_rules = make_handler(check_description, apply_rate_over_end_time, capitalize_description)
