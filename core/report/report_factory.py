from datetime import date

import pandas as pd

from core.model.index import Report, ReportRow, Developer, BankInformation, Costumer


class ReportFactory:

    def create_report(self, config: dict, items: list ) -> Report:
        report = Report(
            date.today(),
            list(map(lambda item: self.create_report_row(item), items)),
            self.create_developer(config),
            self.create_costumer(config),
            None,
            None,
            None)

        return report

    def create_report_row(self, row: dict) -> ReportRow:
        report_row = ReportRow(
            row["Data"],
            row["Hora de Início"],
            row["Hora de Término"],
            row["Duração"],
            row["Salário"],
            0,
            "" if pd.isna(row["Descrição"]) else row["Descrição"])

        return report_row

    def create_developer(self, config: dict):
        developer = Developer(
            config["developer"]["name"],
            config["developer"]["address"],
            config["developer"]["city"],
            self.create_bank_info(config)
        )
        return developer

    def create_bank_info(self, config: dict):
        bank_info = BankInformation(
            "TODO_GENERATE_CODE_INVOICE",
            config["account"]["bank_name"],
            config["account"]["pixkey"],
        )
        return bank_info

    def create_costumer(self, config: dict):
        costumer = Costumer(
            config["costumer"]["company_name"],
            config["costumer"]["address"],
            config["costumer"]["city"]
        )
        return costumer
