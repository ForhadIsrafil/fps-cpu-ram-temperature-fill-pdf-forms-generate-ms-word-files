from docx.shared import Inches, Mm
from docxtpl import DocxTemplate, InlineImage
from faker import Faker
from faker.providers import internet
import glob
import time
import random
from rich.progress import track
from art import *

Art = text2art("DOCX  FILE")
print(Art)

tpl = DocxTemplate("cv_template.docx")

index = 1
for image in track(glob.glob("images/*.jpg"), description="[cyan]Generating..."):

    lang_list = ['it_IT', 'en_US', 'ja_JP', 'ru_RU']
    fake = Faker(locale=random.choice(lang_list))

    # print(fake.profile())
    # print(fake.first_name())
    # print(fake.last_name())
    # print(fake.paragraph())
    # print(fake.text())
    myimage = InlineImage(tpl, image_descriptor=image, width=Inches(3.19), height=Inches(2.15))

    tpl.render({'im': myimage, 'first_n': fake.first_name(), 'last_n': fake.last_name(), 'summery': fake.text()})
    tpl.save(f"docx_files/{index}_profile.docx")
    index += 1



















