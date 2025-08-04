import jinja2
import pdfkit

from core.model.index import ReportInformationDTO
from core.report.report_processor import ReportProcessor

wkhtmltopdf_path = "/usr/bin/wkhtmltopdf"

def format_currency(value):
    return f"R${value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def get_template(resources_path: str, template_name: str):
    loader = jinja2.FileSystemLoader(resources_path)
    env = jinja2.Environment(loader=loader)
    # TODO: add filters should be send with report_dto
    env.filters["format_currency"] = format_currency
    return env.get_template(template_name)


def get_config():
    return pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

def generate_pdf(resource_path: str, template_name: str):
    output_text = get_template(resource_path, template_name).render()
    config = get_config()
    pdfkit.from_string(output_text, "curriculo.pdf", configuration=config)

class ReportPdfProcessor(ReportProcessor):


    def generate_report(self, report_dto: ReportInformationDTO) -> None:

        output_text = get_template(report_dto.get_resources_path(), report_dto.get_template_name()).render(report_dto.get_report_context())
        config = get_config()
        pdfkit.from_string(output_text, "report.pdf", configuration=config)

