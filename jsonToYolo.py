import json
import os

def convert_to_yolo_format(json_file, output_dir):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for item in data:
       
        x_min = item['rectMask']['xMin']
        y_min = item['rectMask']['yMin']
        width = item['rectMask']['width']
        height = item['rectMask']['height']
        
        x_center = (x_min + width / 2) / 640  # Remplacez 640 par la largeur de votre image
        y_center = (y_min + height / 2) / 480  # Remplacez 480 par la hauteur de votre image
        width = width / 640  # Remplacez 640 par la largeur de votre image
        height = height / 480  # Remplacez 480 par la hauteur de votre image

        class_id = 0

        # Créer le contenu du fichier .txt
        txt_content = f"{class_id} {x_center} {y_center} {width} {height}\n"
        
        # Nom du fichier de sortie
        base_name = os.path.basename(json_file).replace('.json', '.txt')
        output_file = os.path.join(output_dir, base_name)
        
        # Écrire le fichier .txt
        with open(output_file, 'w') as out_f:
            out_f.write(txt_content)

# Exemple d'utilisation
convert_to_yolo_format('/path/to/your/labels.json', '/path/to/your/output_dir')
