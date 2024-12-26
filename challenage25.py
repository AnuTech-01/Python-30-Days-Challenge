#CHALLENAGE 25

#Python PIP

import subprocess
import sys

def install_package(package):
    try:
        # Run pip install command
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"'{package}' has been installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Error occurred while installing '{package}'.")

if __name__ == "__main__":
    package_name = input("Enter the package name to install: ")
    install_package(package_name)
