import os
from cssbeautifier import beautify

# Directory where your .min.css files are stored
input_dir = "./"
output_dir = "./styles_pretty_ko"
os.makedirs(output_dir, exist_ok=True)

# Loop through all .min.css files and create .css versions
for file_name in os.listdir(input_dir):
    if file_name.endswith(".css"):
        input_path = os.path.join(input_dir, file_name)
        output_file = file_name.replace(".css", ".css")
        output_path = os.path.join(output_dir, output_file)

        with open(input_path, 'r', encoding='utf-8') as f:
            minified_css = f.read()

        pretty_css = beautify(minified_css)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(pretty_css)

        print(f"Converted {file_name} → {output_file}")
