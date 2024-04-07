import random
from pypdf.generic import Dict, NameObject, NumberObject
from pypdf import PdfReader, PdfWriter

reader = PdfReader("example_form.pdf")
writer = PdfWriter()

page = reader.pages[0]
fields = reader.get_fields()
Countryoptions = fields['Country Combo Box'].get('/Opt')

option_index = Countryoptions.index(NameObject("Romania"))

writer.append(reader)

writer.update_page_form_field_values(
    page=writer.pages[0], fields={
        'Given Name Text Box': "some filled in text",
        'Address 2 Text Box': "some filled in text",
        'City Text Box': "some filled in text",
        'Favourite Colour List Box': fields['Favourite Colour List Box']['/Opt'][-2],
        'Country Combo Box':{'/V':'Slovakia'}
    },
)

# write "output" to PyPDF2-output.pdf
with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)
