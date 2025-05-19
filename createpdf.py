import jinja2
import pdfkit

base_html = "report-template.html"
wkhtmltopdf_path = "/usr/bin/wkhtmltopdf"
resources_path= "./resources/"

def format_currency(value):
    return f"R${value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def generate_report(context):
    loader = jinja2.FileSystemLoader(resources_path)

    env = jinja2.Environment(loader=loader)
    env.filters["format_currency"] = format_currency

    template = env.get_template(base_html)
    output_text = template.render(context)
    pdf_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)
    pdfkit.from_string(output_text, "report.pdf", configuration=pdf_config)


