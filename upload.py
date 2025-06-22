import os
import zipfile
import subprocess

def install_megacmd():
    """Installs megacmd package."""
    try:
        # Install wget
        subprocess.run(['apt', 'install', '-y', 'wget'], check=True, capture_output=True, text=True)
        
        # Download megacmd package
        subprocess.run([
            'wget', 
            'https://mega.nz/linux/repo/xUbuntu_20.04/amd64/megacmd-xUbuntu_20.04_amd64.deb'
        ], check=True, capture_output=True, text=True)
        
        # Install megacmd
        subprocess.run(['apt', 'install', '-y', './megacmd-xUbuntu_20.04_amd64.deb'], check=True, capture_output=True, text=True)
        
        # Remove the deb file
        subprocess.run(['rm', 'megacmd-xUbuntu_20.04_amd64.deb'], check=True, capture_output=True, text=True)
        print("megacmd installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing megacmd: {e.stderr}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error during megacmd installation: {e}")
        exit(1)

def get_profile_path(profile_name):
    """Finds the profile folder using the profile name."""
    profiles_dir = os.path.expanduser('~/.mozilla/firefox')
    profile_folders = [f for f in os.listdir(profiles_dir) if f.endswith(profile_name)]
    if profile_folders:
        return os.path.join(profiles_dir, profile_folders[0])
    return None

def zip_folder(folder_path, zip_name):
    """Zips the folder, skipping symbolic links."""
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Skip symbolic links
                if not os.path.islink(file_path):
                    try:
                        zipf.write(file_path, os.path.relpath(file_path, folder_path))
                    except FileNotFoundError:
                        print(f"File not found and skipped: {file_path}")
                else:
                    print(f"Symbolic link skipped: {file_path}")
    print(f'Folder zipped successfully as {zip_name}')

def upload_to_mega(zip_name):
    """Uploads the zip file to MEGA's /part2 folder."""
    try:
        # Log out if already logged in
        subprocess.run(['mega-logout'], capture_output=True, text=True)
        
        # Log in to MEGA account
        subprocess.run(['mega-login', 'volcnao62@gmail.com', '21504174lL@'], check=True, capture_output=True, text=True)
        
        # Create /part2 folder if it doesn't exist
        subprocess.run(['mega-mkdir', '/github-firefox'], capture_output=True, text=True)
        
        # Upload the zip file to /part2
        result = subprocess.run(['mega-put', zip_name, '/github-firefox'], check=True, capture_output=True, text=True)
        print(f'File {zip_name} uploaded successfully to MEGA /github-firefox')
    except subprocess.CalledProcessError as e:
        print(f'Error during MEGA operation: {e.stderr}')
        exit(1)
    except Exception as e:
        print(f'Unexpected error during upload: {e}')
        exit(1)

def delete_file(file_path):
    """Deletes the specified file."""
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting file '{file_path}': {e}")
    else:
        print(f"File '{file_path}' does not exist.")

if __name__ == '__main__':
    # Install megacmd
    install_megacmd()
    
    # Read the latest profile name created by the bash script
    try:
        with open('current_profile.txt', 'r') as f:
            profile_name = f.read().strip()
    except FileNotFoundError:
        print("Error: 'current_profile.txt' not found.")
        exit(1)

    # Find the profile folder
    profile_path = get_profile_path(profile_name)

    if profile_path:
        zip_name = profile_name + '.zip'

        # Zip the profile folder
        zip_folder(profile_path, zip_name)

        # Upload the zip file to MEGA's /part2 folder
        upload_to_mega(zip_name)

        # Remove the zip file after uploading
        delete_file(zip_name)
    else:
        print(f"Profile folder for '{profile_name}' not found.")
