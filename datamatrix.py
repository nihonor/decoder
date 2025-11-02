from pylibdmtx import pylibdmtx
from PIL import Image

# Load the image
image_path = "2531d174-90d6-485b-92ec-b607a4e084ae.png"
img = Image.open(image_path)

# Decode the Data Matrix code
decoded = pylibdmtx.decode(img)

# Print the result
if decoded:
    print("Decoded Data Matrix content:", decoded[0].data.decode('utf-8'))
else:
    print("No Data Matrix code detected.")
