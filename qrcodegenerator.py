import qrcode

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

# Add data to the QR code
data = "https://www.instagram.com/p/C9Fr97syNFGKuGNpFyNpsN8buUv9kxGQZLZ2Vo0/?img_index=3"
qr.add_data(data)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save('test.png')

# Display the image in the notebook
from IPython.display import Image
Image('test.png')
