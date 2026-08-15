import io
import base64
import xlsxwriter

from odoo import api,models,fields,_
from odoo.exceptions import ValidationError


class ShopAvailableReportWizard(models.TransientModel):
    _name = 'shop.available.report.wizard'
    _description = "Shop Available Report Wizard"

    start_date = fields.Date('Start Date',require=True)
    end_date = fields.Date('End Date',require=True)
    report_file = fields.Binary("Excel File",readonly=True,attachment=False)
    report_filename = fields.Char("Filename",readonly=True)

    def action_export_excel(self):
        self.ensure_one()
        if self.start_date > self.end_date:
            raise ValidationError(_("Start Date cannot be greater than End Date!"))

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output,
                                       {"in_memory":True,"stings_to_formulas":False,"string_to_url":False})
        worksheet = workbook.add_worksheet("Available Report")

        title_format = workbook.add_format({
            "bold":True,
            "font_size":16,
            "align":"center",
        })

        worksheet.merge_range("A1:F1","Available Report",title_format)

        workbook.close()
        filename = ("shop_report"+str(self.start_date)+"_to_"+str(self.end_date))
        #short_report_july5_to_july19

        excel_data = output.getvalue()
        encode_excel = base64.b64encode(excel_data)

        self.report_file = encode_excel
        self.report_filename = filename

        output.close()

        download_url = ("/web/content/"+self._name+"/"+str(self.id)+"/report_file/"+filename+"?download=true")

        return {
            "type":"ir.actions.act_url",
            "url":download_url,
            "target":"self",
        }


