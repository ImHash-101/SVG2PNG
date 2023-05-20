import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Create the output directory if it does not exist
if not os.path.exists('output'):
    os.makedirs('output')

# Loop through all SVG files in the input directory
for filename in os.listdir('input'):
    if filename.endswith('.svg'):
        # Load the SVG file and render it as a bitmap
        drawing = svg2rlg(os.path.join('input', filename))
        bitmap = renderPM.drawToPIL(drawing)

        # Save the bitmap as a PNG file in the output directory
        output_filename = os.path.splitext(filename)[0] + '.png'
        bitmap.save(os.path.join('output', output_filename))
