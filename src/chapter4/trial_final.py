from typing import Final

VENDOR_NAME: Final = "Viafore's Auto-Dog"


def display_vendor_information():
    global VENDOR_NAME
    vendor_info = "Auto-Dog v1.0"
    # vendor_info += VENDOR_NAMEでなければならないのに、コピペミスをした
    VENDOR_NAME += VENDOR_NAME
    print(vendor_info)


display_vendor_information()
