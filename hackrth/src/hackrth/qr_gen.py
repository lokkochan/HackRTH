import qrcode


def qr_gen(redeem_code):
    qr = qrcode.QRCode(
        version=1,
        box_size=16,
        border=4,
    )
    qr.add_data(redeem_code)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    return img
