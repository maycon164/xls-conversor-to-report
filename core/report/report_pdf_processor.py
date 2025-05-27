import jinja2
import pdfkit

from core.model.index import ReportInformationDTO
from core.report.report_processor import ReportProcessor


def format_currency(value):
    return f"R${value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class ReportPdfProcessor(ReportProcessor):

    wkhtmltopdf_path: str

    def __init__(self):
        self.wkhtmltopdf_path = "/usr/bin/wkhtmltopdf"

    def generate_report(self, report_dto: ReportInformationDTO) -> None:

        output_text = self.get_template(report_dto.get_resources_path(), report_dto.get_template_name()).render(report_dto.get_report_context())
        config = self.get_config()
        pdfkit.from_string(output_text, "report.pdf", configuration=config)


    def get_template(self, resources_path: str, template_name: str):
        loader = jinja2.FileSystemLoader(resources_path)
        env = jinja2.Environment(loader=loader)
        # TODO: add filters should be send with report_dto
        env.filters["format_currency"] = format_currency
        return env.get_template(template_name)

    def get_config(self):
        return pdfkit.configuration(wkhtmltopdf=self.wkhtmltopdf_path)

