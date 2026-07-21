# Takes a PDF file and sends it to Claude Vision API
# Returns structured data: date, vendor, description, part number, PO, document type
import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

