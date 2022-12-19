from PySide6.QtCore import QByteArray
from PySide6.QtGui import QImage, QPixmap


def base64_to_pixmap(blob_image):
    ba = QByteArray.fromBase64(blob_image)
    img = QImage.fromData(ba, 'PNG')
    pixmap = QPixmap.fromImage(img)
    return pixmap
