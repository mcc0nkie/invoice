import os
from odf.document import load
from odf import text, teletype

class CreateInvoice:
    def __init__(self, output_name, template_location='./template/template.odt', **kwargs):
        odt_document = load(template_location)

        for key, value in kwargs.items():
            self.template_variables["{" + key + "}"] = value

        for paragraph in odt_document.getElementsByType(text.P):
            for key, value in self.template_variables.items():
                if key in paragraph:
                    teletype.extractText(paragraph).replace(key, value)

        odt_document.save(output_name)

