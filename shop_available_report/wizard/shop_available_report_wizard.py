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
                                       {"in_memory":True,"strings_to_formulas":False,"string_to_urls":False})
        worksheet = workbook.add_worksheet("Available Report")

        title_format = workbook.add_format({
            "bold":True,
            "font_size":16,
            "align":"center",
        })
        header_format = workbook.add_format({
            "bold":True,
            "border":1,
            "align":"center",
        })
        text_format = workbook.add_format({
            "border": 1,
        })
        number_format = workbook.add_format({
            "border": 1,
            "num_format": "#,##0.00",
        })
        date_format = workbook.add_format({
            "border": 1,
            "num_format": "yyyy-mm-dd",
        })

        worksheet.merge_range("A1:F1","Available Report",title_format)

        items = self.env['shop.item'].search([("date",">=",self.start_date),("date","<=",self.end_date),("state","in",("draft","available"))])

        worksheet.write(2,0,"Item Reference",header_format)
        worksheet.write(2,1,"Item",header_format)
        worksheet.write(2,2,"Date",header_format)
        worksheet.write(2,3,"Product",header_format)
        worksheet.write(2,4,"QTY",header_format)
        worksheet.write(2,5,"Unit Cost",header_format)
        worksheet.write(2,6,"Total Amount",header_format)
        worksheet.write(2,7,"Status",header_format)

        worksheet.set_column("A:C",16)
        worksheet.set_column("D:D",25)
        worksheet.set_column("E:H",20)

        row = 3
        for item in items:
            for line in item.item_line_ids:
                if not line.product_id:
                    continue
                sequence = "-"
                if item.sequence:
                    sequence = item.sequence
                else:
                    sequence = "-"
                worksheet.write(row,0,sequence,text_format)
                worksheet.write(row,1,item.name or "-",text_format)
                worksheet.write(row,2,item.date or "",date_format)
                worksheet.write(row,3,line.product_id.name,text_format)
                worksheet.write(row,4,line.quantity,number_format)
                worksheet.write(row,5,line.unit_cost,number_format)
                worksheet.write(row,6,line.total_amount,number_format)
                worksheet.write(row,7,"Available" if item.state=='available' else "Draft",number_format)
                row+=1

        workbook.close()
        filename = ("shop_report"+str(self.start_date)+"_to_"+str(self.end_date)+".xlsx")
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


