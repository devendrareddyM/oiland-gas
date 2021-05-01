from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors


def pdf_generator(data):
    fileName = 'test.pdf'
    rowNumb = len(data)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (8, 0), colors.lightgrey),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12)
    ])

    pdf = SimpleDocTemplate(filename=fileName,
                            pagesize=letter)

    final_array = []
    header = ['Employee', 'Entry Date', 'EMP ID', 'Temperature', 'Type', 'Gate No', 'Company', 'Status', 'Remark']
    final_array.append(header)
    for each in data:
        each.pop('mask_detection')
        each.pop('voilation')
        each.pop('temperature_flag')
        each.pop('temperature_voilation_flag')
        each.pop('mask_flag')
        each.pop('gate_id')
        each.pop('phone_number')
        if each['status'] == 1:
            each['status'] = 'Open'
        else:
            each['status'] = 'Closed'
        data = [x for x in each.values()]
        final_array.append(data)

    table = Table(data=final_array)
    table.setStyle(style)

    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige
        ts = TableStyle(
            [('BACKGROUND', (0, i), (-1, i), bc)]
        )
        table.setStyle(ts)

    pdf_data = [table]
    pdf.build(pdf_data)
