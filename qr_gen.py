import qrcode


def qr_gen():
    qr = qrcode.QRCode(
        version = 1
        box_size = 16
        border = 4
        )
    qr.add_data()
    qr.make(fit = True)

    img = qr.make_image(fill_color = 'black', back_color = 'white')