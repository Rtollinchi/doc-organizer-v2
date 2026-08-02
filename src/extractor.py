# Takes a PDF file and sends it to Claude Vision API
# Returns structured data: date, vendor, description, part number, PO, document type
import os
import base64
from anthropic import Anthropic
from dotenv import load_dotenv
from pdf2image import convert_from_path
from io import BytesIO

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_data(file_path):
  """
  Extract structured data from a PDF file and send it to the Claude Vision API.
  Returns an object with keys: date, vendor, description, part number, PO, document type.
  """
  images = []

  documents = convert_from_path(file_path)
  for doc in documents:
    buffer = BytesIO()
    doc.save(buffer, format="JPEG")
    img_bytes = buffer.getvalue()
    img_base64_bytes = base64.b64encode(img_bytes)
    images.append(img_base64_bytes.decode("utf-8"))
  return images


