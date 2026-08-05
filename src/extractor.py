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

PROMPT = """You are a document analysis assistant. You are looking at a scanned business document. Extract the following fields:

Date
Vendor
Description of items purchased
Part number(if available)
Purchase Order number (if available)
Who ordered it (if available)
Document type (if available) For doc_type return exactly one of: packing_slip, purchase_order, receipt, invoice, other

Return only a JSON object with these exact keys:
date:
vendor:
description:
purchase_order_number:
part_number:
who_ordered_it:
doc_type:

If a field is not found return null for that field"""

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

  content = []

  for image in images:
    content.append({
      "type": "image",
      "source": {"type": "base64", "media_type": "image/jpeg", "data": image
      }
    })

  content.append({
    "type": "text",
    "text": PROMPT
  })

  response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": content}]
  )

  raw =  response.content[0].text
  cleaned = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()

  print("Cleaned response:")
  print(cleaned)
  return cleaned


