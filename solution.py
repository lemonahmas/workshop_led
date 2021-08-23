from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
import time

serial = spi(port=0, device=0, gpio=noop(), block_orientation=90)
device = max7219(serial,width=32,block_orientation=-90)

while(True):
    virtual = viewport(device, width=300, height=100)

    t = time.strftime(r"%Y-%m-%d %H:%M:%S",time.gmtime())

    with canvas(virtual) as draw:
        #print(type(draw))
        #draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((3, 3), f"current time:{t}", fill="white", stroke_width=2)

    for offset in range(180):
        virtual.set_position((offset, 4))
        time.sleep(0.05)
