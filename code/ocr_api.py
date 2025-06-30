# from official documentation of Mistral OCR API
# https://docs.mistral.ai/capabilities/OCR/basic_ocr/
# version that uses local files instead of URLs as input
class MistralOCR:
    def __init__(self, api_key):
        from mistralai import Mistral
        self.client = Mistral(api_key=api_key)

    def encode_image(self, image_path):
        import base64
        try:
            with open(image_path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        except Exception as e:
            print(f"Error encoding {image_path}: {e}")
            return None

    def process_document(self, image_path):
        base64_image = self.encode_image(image_path)
        if not base64_image:
            return None
        ocr_response = self.client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "image_url",
                "image_url": f"data:image/jpeg;base64,{base64_image}"
            },
            include_image_base64=True  # receive images back in case some part is not OCRed
        )
        return ocr_response