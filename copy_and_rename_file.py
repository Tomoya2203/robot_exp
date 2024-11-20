import os
import shutil
import json

# aのフォルダだけ形式違うのでそれ以外をコピーした
def copy_and_rename_files(source_dir, dest_dir):
    """
    Recursively search for files containing 'image' in their name,
    copy them to the destination directory with modified filenames.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(source_dir):
        for file in files:
            if 'image' in file:  # Check if 'image' is in the filename
                # Construct the full source path
                source_path = os.path.join(root, file)

                # Create the new filename by replacing '/' with '_'
                relative_path = os.path.relpath(source_path, source_dir)
                new_filename = relative_path.replace(os.sep, "_")

                # Construct the destination path
                dest_path = os.path.join(dest_dir, new_filename)

                # Copy the file to the destination directory
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {source_path} -> {dest_path}")


def update_image_path_in_json(directory):
    """
    Update the `imagePath` field in all JSON files in the specified directory
    to match the JSON filename with `.png` as the extension.
    """
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    # Get the list of JSON files in the specified directory
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    for json_file in json_files:
        # Construct the new imagePath
        image_path = os.path.splitext(json_file)[0] + ".png"

        # Construct the full path to the JSON file
        json_path = os.path.join(directory, json_file)

        # Open and load the JSON file
        with open(json_path, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                print(f"Skipping {json_file}: Invalid JSON format.")
                continue

        # Update the imagePath field
        data['imagePath'] = image_path

        # Save the updated JSON file
        with open(json_path, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"Updated {json_file}: imagePath set to {image_path}")


# Example usage
source_directory = "./hsr_sim_obj_1000"  # Replace with your source directory
destination_directory = "./all_file"  # Replace with your destination directory

copy_and_rename_files(source_directory, destination_directory)
update_image_path_in_json(destination_directory)

