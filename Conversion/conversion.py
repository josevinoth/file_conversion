import os
from PIL import Image
import subprocess
def convert_cgm_to_svg(cgm_file, output_svg):
    # Check if pycgm2svg is installed
    try:
        import pycgm2svg
    except ImportError:
        raise ImportError("pycgm2svg library not installed. You can install it with 'pip install pycgm2svg'")

    # Convert CGM to SVG using pycgm2svg
    cgm2svg_command = f"pycgm2svg -i {cgm_file} -o {output_svg}"
    subprocess.run(cgm2svg_command, shell=True)


def convert_tif_to_svg(tif_file, output_svg):
    # Check if Pillow is installed
    try:
        from PIL import Image
    except ImportError:
        raise ImportError("Pillow library not installed. You can install it with 'pip install Pillow'")

    # Convert TIF to SVG using Pillow
    img = Image.open(tif_file)
    img.save(output_svg, "SVG")


if __name__ == "__main__":
    # Input file paths
    cgm_file_path = "../Conversion/allprims.cgm"
    tif_file_path = "../Conversion/file_example_TIFF_1MB.tiff"

    # Output file paths
    svg_output_cgm = "output_cgm.svg"
    svg_output_tif = "output_tif.svg"

    # Convert CGM to SVG
    convert_cgm_to_svg(cgm_file_path, svg_output_cgm)

    # Convert TIF to SVG
    convert_tif_to_svg(tif_file_path, svg_output_tif)

    print("Conversion complete.")