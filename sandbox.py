from EasyMCP2221 import MCP2221

if __name__ == '__main__':
    usb_serials = ['0004688946',
                   '0006179578',
                   '0006178676',
                   '0006176088',
                   '0004694576',
                   '0004699196']
    for usb_serial in usb_serials:
        try:
            mcp = MCP2221.Device(usbserial=usb_serial)
            print(f"Connected to MCP2221 with USB serial: {usb_serial}")
            mcp.set_flash_protection(MCP2221.WriteProtection.PROTECTED, b'\x00\x00\x00\x00\x00\x00\x00\x00')
            print(mcp.get_all_gp_settings())

            print(mcp.get_all_chip_settings())
        except Exception as e:
            print(f"Failed to connect to MCP2221 with USB serial {usb_serial}: {e}")
