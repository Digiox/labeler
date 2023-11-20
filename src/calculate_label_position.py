from typing import Tuple
from reportlab.pdfgen import canvas

def calculate_label_position(label_width_pt: int, label_height_pt: int, x_spacing: int, y_spacing: int, page_width: int, page_height: int, current_width: int, current_height: int, c: canvas.Canvas) -> Tuple[int, int]:
     # Update positions for the next label
    current_width += label_width_pt + x_spacing
    if current_width + label_width_pt > page_width:
        current_width = x_spacing
        current_height -= label_height_pt + y_spacing
        if current_height < label_height_pt:
            c.showPage()  # Create a new page if there's no room for the next label
            current_height = page_height

    return current_width, current_height