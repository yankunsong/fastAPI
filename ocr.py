import pytesseract
import asyncio

async def read_image(image_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(image_path, lang=lang)
        await asyncio.sleep(2)
        return text
    except:
        return "[Error] Unable to process file: {0}".format(image_path)
