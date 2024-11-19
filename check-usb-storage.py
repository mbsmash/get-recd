import os

def check_usb_storage(mount_point="/media/usb"):
    if os.path.ismount(mount_point):
        print(f"USB storage found at {mount_point}")
        return True
    else:
        print("USB storage not found.")
        return False

if __name__ == "__main__":
    check_usb_storage()
