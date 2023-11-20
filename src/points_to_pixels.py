import json

# Load the JSON file
with open("C:\\Users\\Digiox\\Documents\\code\\labeler\\src\\configs\\labels.json") as f:
    data = json.load(f)

# Extract the print_dpi value
print_dpi = data['print_dpi']

def points_to_pixels(points, dpi=print_dpi):
    inches = points / 72  # Convert points to inches
    return int(inches * dpi)  # Convert inches to pixels