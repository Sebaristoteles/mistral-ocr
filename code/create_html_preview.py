import os
import subprocess
from glob import glob

# Get the absolute path to the data/output/examples folder relative to this script
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# adjust the path to the markdown folder
# -----------------------------------------------------------------------------

markdown_folder = os.path.join(base_dir, "data", "output", "examples")

# -----------------------------------------------------------------------------



# Find all markdown files in the folder
md_files = glob(os.path.join(markdown_folder, "*.md"))

for md_file in md_files:
    md_filename = os.path.basename(md_file)
    output_html = os.path.splitext(md_filename)[0] + ".html"
    subprocess.run([
        "quarto", "render", md_filename,
        "--to", "html",
        "--output", output_html
    ], cwd=markdown_folder, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"Created: {os.path.join(markdown_folder, output_html)}")