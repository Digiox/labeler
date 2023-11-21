
Vous cherhez la documentation en français ?
Cliquez ici !

[FRENCH_README.md](FRENCH_README.md)


# LabelCraft

## Introduction

LabelCraft is a software that allows the user to generate labels from a CSV file (semicolon separator).

You can choose as many CSV files as you want, and the labels will be generated one after the other on a PDF (You will have a field to specify or save this PDF and a field to define its name).

For each file, you have a field that allows you to specify (mandatory) a supplier.

So each CSV file must have items from a single supplier.

## Mandatory Fields

Your CSV must have at least 6 columns (These will be the columns displayed on the label):

- Product ID
- Product
- Sale Price
- Barcode
- Supplier Reference
- Variation

Make sure the field names are written exactly as above.

## Interface Preview

<img src="assets\image.png" alt="Alt text" width="50%">

In this image, you can see the composition of the software interface:

1. The first field is for entering the name of the PDF file to be saved.
2. The second field is designed to specify a location on your computer where the file will be downloaded.
3. The third field is for the source CSV file (Browse button to open the file explorer).
4. The fourth field, which is just to the right of the third field, is used to specify the Supplier.
5. The Remove button is used to delete the current line.
6. The "Add CSV and Supplier" button adds two additional fields for a CSV source file and a supplier.
7. These are the software logs, where you can see if everything went well. If some labels could not be generated, you will be able to see it here.
8. If you want to clear the contents of the logs, the Clean/Erase button is present.
9. The button to start the generation once all fields are filled.

> **Note:** The more lines you have in your CSV, the longer the generation time will be. Don't worry, it's normal!

## Specific Requirements?

This version of the software is completely free and not customizable (It may become customizable in the future).

If you need a version of the software specific to your use, please send a message to **bourlon.lyann84@gmail.com** and request a quote.
