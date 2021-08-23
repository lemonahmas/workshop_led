from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
import time

#Please fill the angle brackets part

serial = spi(port=0, device=0, gpio=noop(), block_orientation=90)
device = max7219(serial,width=<>,block_orientation=<>)

while(True):
    virtual = viewport(device, width=200, height=100)

    t = time.strftime(r"%Y%m%d",time.gmtime())

    with canvas(virtual) as draw:
        #draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text(<>, f"current time:{t}", fill="white")

    for offset in range(<>):
        virtual.set_position((offset, 4))
        time.sleep(0.1)