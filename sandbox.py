from EasyMCP2221 import MCP2221

if __name__ == '__main__':
    # NOTE: quick and dirty script to set the write protection on the MCP2221 devices (intended for ICT use). Make sure that you first set GPIO settings before applying
    # the write-protection.
    usb_serials = [
                "0006180251",
                "0006178898",
                "0006176117",
                "0006177280",
                "0006179096",
                "0006177783",
                   ]
    for usb_serial in usb_serials:
        try:
            mcp = MCP2221.Device(usbserial=usb_serial)
            print(f"Connected to MCP2221 with USB serial: {usb_serial}")
            print(mcp.get_all_gp_settings())
            print(mcp.get_all_chip_settings())
            usr = input('Apply write protection? (y/n): ')
            if usr.lower() == 'y':
                mcp.set_flash_protection(MCP2221.WriteProtection.PROTECTED, b'\x00\x00\x00\x00\x00\x00\x00\x00')

        except Exception as e:
            print(f"Failed to connect to MCP2221 with USB serial {usb_serial}: {e}")