import json
import time
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
from barcode import EAN13 # type: ignore
from barcode.writer import ImageWriter # type: ignore
from reportlab.pdfgen import canvas # type: ignore
from reportlab.lib.pagesizes import A4 # type: ignore
import tkinter as tk
import os
import tkinter.scrolledtext as ScrolledText
from points_to_pixels import points_to_pixels
from typing import Tuple

def create_and_draw_labels(data: pd.DataFrame, text_widget: ScrolledText.ScrolledText, c: canvas.Canvas, supplier: str, current_width: int, current_height: int) -> Tuple[int, int, int, int]:

    try:
        with open("C:\\Users\\Digiox\\Documents\\code\\labeler\\src\\configs\\labels.json") as f:
            config = json.load(f)
        text_widget.insert(tk.END, f"Label configuration loaded from JSON file.: {config}\n")
        print_dpi = config['print_dpi']
        label_width_pt = config['label_width_pt']
        label_height_pt = config['label_height_pt']
        x_spacing = config['x_spacing']
        y_spacing = config['y_spacing']
    except Exception as e:
        text_widget.insert(tk.END, f"Error loading JSON file: {e}\n")
        return 0, 0, 0, 0

    # Cheking if the label dimensions are defined
    
    if not label_width_pt or not label_height_pt:
        text_widget.insert(tk.END, "Label dimensions are not defined.\n")
        return 0, 0, 0, 0
    else:
        text_widget.insert(tk.END, f"Label dimensions are {label_width_pt}x{label_height_pt} points.\n")

    # Cheking if the label spacing is defined
    if x_spacing is None or y_spacing is None:
        text_widget.insert(tk.END, "Label spacing is not defined.\n")
        return 0, 0, 0, 0
    else:
        text_widget.insert(tk.END, f"Label spacing is {x_spacing}x{y_spacing} points.\n")

    page_width, page_height = A4

    # Convert label dimensions to pixels
    label_width_px = points_to_pixels(label_width_pt)
    label_height_px = points_to_pixels(label_height_pt)

    # Starting position for the first label at the top of the page

    labels_generated = 0
    labels_failed = 0

    for index, row in data.iterrows():
            print(f"index: {index}")

            try:
                # Récupération des données nécessaires pour l'étiquette
                product_id = row['Produit ID']
                product_name = row['Produit']
                price = row['Prix de vente']
                barcode = str(row['Code-barres'])
                supplier_ref = row['Ref. fournisseur']
                variant = row['Déclinaison']

                # Create the label with a red border
                color = "white"
                img = Image.new('RGB', (label_width_px, label_height_px), color)
                draw = ImageDraw.Draw(img)
                draw.rectangle(((0, 0), (label_width_px-1, label_height_px-1)), outline='black', width=1)
                font = ImageFont.truetype('arial.ttf', 25)
                print(f"supplier: {supplier}")
                label_text = f"ID: {product_id}\n{product_name}\nRef: {supplier_ref}\n{supplier}"
                if pd.isna(variant):
                    price_text = f"{price} €"
                else:
                    price_text = f"{price} €\n{variant}"

                # Draw label text at the top-left corner
                draw.text((10, 10), label_text, fill='black', font=font)

                # Define a larger font
                large_font_size = 32
                # Créer un objet font pour le price_text
                # Créer un objet font pour le price_text
                large_font = ImageFont.truetype('arial.ttf', large_font_size)

                # Utiliser textbbox pour obtenir la boîte englobante du texte de price_text
                # Les coordonnées de départ (0, 0) sont utilisées pour mesurer la taille du texte
                bbox = draw.textbbox((0, 0), price_text, font=large_font)

                # bbox contient (x0, y0, x1, y1)
                # La largeur du texte est x1 - x0
                price_text_width = bbox[2] - bbox[0]

                # Calculer la position x pour price_text
                # On soustrait la largeur du texte price_text et on divise par 2 pour centrer, puis on ajoute la marge de gauche
                price_x_position = label_width_px - price_text_width - 10  # 10 est la marge de gauche pour label_text

                # Dessiner price_text avec la nouvelle position x
                draw.text((price_x_position, 10), price_text, fill='black', font=large_font)
                
                # Generate the barcode with options to improve quality
                ean = EAN13(barcode, writer=ImageWriter())
                barcode_img = ean.render(writer_options={
                    'module_width': 0.21,  # Adjust for thinner, less pixelated bars
                    'module_height': 4.0,  # Adjust for taller, less pixelated bars
                    'font_size': 3,  # Font size converted to pixels
                    'text_distance': 3,
                    'quiet_zone': 1,
                    'write_text': True,
                    'dpi': print_dpi
                })
                
                # Calculate the barcode scale based on the label dimensions and DPI
                barcode_scale = min(label_width_px / barcode_img.width, label_height_px / barcode_img.height / 2)
                barcode_img = barcode_img.resize((int(barcode_img.width * barcode_scale), int(barcode_img.height * barcode_scale)), resample=Image.LANCZOS)
                
                # Place the barcode on the label
                barcode_x_position = (label_width_px - barcode_img.width) // 2
                barcode_y_position = label_height_px - barcode_img.height - points_to_pixels(1)  # Convert 10 points offset to pixels
                img.paste(barcode_img, (barcode_x_position, barcode_y_position))
                
                try:
                    # Save the label to a temporary image file
                    temp_img_path = f'temp_img_{index}_{supplier}.png'
                    img.save(temp_img_path)
                except Exception as e:
                    text_widget.insert(tk.END, f"Error saving temporary image file: {e}\n")
                    labels_failed += 1
                    continue
                
                try:
                    # Draw the image onto the PDF
                    c.drawImage(temp_img_path, current_width, current_height - label_height_pt, label_width_pt, label_height_pt)
                    print(f"Label {product_name} drawn at {current_width}, {current_height - label_height_pt} with supplier {supplier}")
                except Exception as e:
                    text_widget.insert(tk.END, f"Error drawing image onto PDF: {e}\n")
                    labels_failed += 1
                    continue
                
                # Update positions for the next label
                current_width += label_width_pt + x_spacing
                if current_width + label_width_pt > page_width:
                    current_width = x_spacing
                    current_height -= label_height_pt + y_spacing
                    if current_height < label_height_pt:
                        c.showPage()  # Create a new page if there's no room for the next label
                        current_height = page_height
                # Juste avant de dessiner l'image sur le PDF :
                if current_height - label_height_pt < 0:
                    c.showPage()  # Créer une nouvelle page
                    current_height = page_height  # Réinitialiser la hauteur
                    current_width = 0  # Réinitialiser la largeur

                # Remove temporary image files
                os.remove(temp_img_path)
                
                # Increment the count of generated labels
                labels_generated += 1
                

            except Exception as e:
                text_widget.insert(tk.END, f"Error generating label for {product_name}: {e}\n")
                labels_failed += 1
    return labels_generated, labels_failed, current_height, current_width
