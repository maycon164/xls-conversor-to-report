from datetime import timedelta, date
import yaml

from createpdf import generate_report
from read_excel import read_file
import pandas as pd
import rules

file = "./resources/ml-report.xls"
cols = ["Data", "Hora de Início", "Hora de Término", "Duração", "Salário", "Descrição"]

with open("./resources/config.yml", "r") as config_file:
    config = yaml.safe_load(config_file)

def parser(row):
    return {
        "date": row["Data"],
        "init_time": row["Hora de Início"],
        "end_time": row["Hora de Término"],
        "duration": row["Duração"],
        "salary": row["Salário"],
        "additional": 0,
        "description":"" if pd.isna(row["Descrição"]) else row["Descrição"]
    }

def create_base_context(items, total_value, total_hours):
    ctx = {
        "generated_date": date.today(),
        "invoice_code": "Invoice#1123C",
        "dev_name": config["developer"]["name"],
        "dev_address": config["developer"]["address"],
        "dev_city": config["developer"]["city"],
        "costumer_company_name": config["costumer"]["company_name"],
        "costumer_address": config["costumer"]["address"],
        "costumer_city": config["costumer"]["city"],
        "bank_name": config["account"]["bank_name"],
        "bank_pix_key": config["account"]["pixkey"],
        "items": items,
        "total_value": total_value,
        "total_hours": total_hours
    }

    return ctx

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


def init():
    items = read_file(file, cols)
    items.pop()

    parsed_items = ([rules.apply_rules(parser(item)) for item in items])

    total_hours = sum_times([item["duration"].strftime("%H:%M:%S") for item in parsed_items])
    additional = sum([item["additional"] for item in parsed_items])
    total_value = sum([item["salary"] for item in parsed_items])

    context = create_base_context(parsed_items, total_value + additional, total_hours)

    generate_report(context)


init()