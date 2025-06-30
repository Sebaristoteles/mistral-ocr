import os
import json
import pandas as pd
from dotenv import load_dotenv
from ocr_api import MistralOCR
import base64

DEBUGGING = False

load_dotenv()
API_KEY = os.getenv("API_KEY")



# change this to your input CSV file path
# -----------------------------------------------------------------------------

input_csv = "data/input_examples.csv"

# -----------------------------------------------------------------------------



df = pd.read_csv(input_csv)

if DEBUGGING:
    #df = df.iloc[[10]]  # Selects the 11th row (Python uses zero-based indexing)
    df = df.head(1)

ocr = MistralOCR(API_KEY)

def decode_and_save_image(image_base64, img_path):
    # Remove data URL prefix if present
    if image_base64.startswith("data:image"):
        image_base64 = image_base64.split(",", 1)[1]
    with open(img_path, "wb") as img_file:
        img_file.write(base64.b64decode(image_base64))

for _, row in df.iterrows():
    input_folder = row["input_folder"]
    document_name = row["document_name"]

    input_path = os.path.join("data", "input", input_folder, document_name)
    output_folder = os.path.join("data", "output", input_folder)
    os.makedirs(output_folder, exist_ok=True)
    output_base = os.path.splitext(document_name)[0]
    output_md_path = os.path.join(output_folder, output_base + ".md")
    output_json_path = os.path.join(output_folder, output_base + ".json")

    try:
        result = ocr.process_document(input_path)

        # Prepare to update markdown and image references
        for page in result.pages:
            for img in getattr(page, "images", []):
                if img.image_base64:
                    new_img_name = f"{output_base}_{img.id}"
                    img_path = os.path.join(output_folder, new_img_name)
                    # Decode and save the image
                    decode_and_save_image(img.image_base64, img_path)
                    # Update image reference in markdown
                    page.markdown = page.markdown.replace(f"![]({img.id})", f"![]({new_img_name})")
                    page.markdown = page.markdown.replace(f"![{img.id}]({img.id})", f"![{new_img_name}]({new_img_name})")
                    img.id = new_img_name

        # Save updated JSON
        result_dict = result.model_dump() if hasattr(result, "model_dump") else result.__dict__
        with open(output_json_path, "w", encoding="utf-8") as f_json:
            json.dump(result_dict, f_json, ensure_ascii=False, indent=2)

        # Save updated markdown
        content = "\n\n".join([page.markdown for page in result.pages])
        with open(output_md_path, "w", encoding="utf-8") as f_md:
            f_md.write(content)
        print(f"Processed {document_name} -> {output_md_path} and {output_json_path}")
    except Exception as e:
        print(f"Failed to process {document_name}: {e}")