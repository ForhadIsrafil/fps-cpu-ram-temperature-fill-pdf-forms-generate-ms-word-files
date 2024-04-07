import time
import fillpdf
from fillpdf import fillpdfs
import faker
import random

fake = faker.Faker(locale='en_US')

input_pdf_path = 'example_form.pdf'
fillpdfs.print_form_fields(input_pdf_path=input_pdf_path,page_number=1)
fields = fillpdfs.get_form_fields(input_pdf_path)

while True:
    data = {'Given Name Text Box': fake.first_name(),
            'Family Name Text Box': fake.last_name(),
            'Address 1 Text Box': fake.address(),
            'House nr Text Box': fake.phone_number(),
            'Address 2 Text Box': fake.address(),
            'Postcode Text Box': fake.postcode(),
            'City Text Box': fake.city(),
            'Gender List Box': random.choice(['Man', 'Woman']),
            'Height Formatted Field': random.randint(1, 500),
            'Driving License Check Box': random.choice(['Yes', 'No']),
            'Language 1 Check Box': random.choice(['On', 'Off']),
            'Language 2 Check Box': random.choice(['Yes', 'No']),
            'Language 3 Check Box': random.choice(['On', 'Off']),
            'Language 4 Check Box': random.choice(['Yes', 'No']),
            'Language 5 Check Box': random.choice(['On', 'Off']),
            'Favourite Colour List Box': random.choice(
                ['Black', 'Brown', 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Violet', 'Grey', 'White'])}

    #
    output_path = f"output.pdf"
    fillpdfs.write_fillable_pdf(input_pdf_path, output_path, data)

    time.sleep(2)
