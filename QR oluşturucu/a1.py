import sys
import qrcode

# ====== Edit this variable to change the QR content ======
qr_data = "https://www.google.com/search?sca_esv=753d27767aefc527&sxsrf=AE3TifOuceMLGKaQd7DdPPzLygiADdYhIw:1765781356919&udm=28&fbs=AIIjpHwSU0Xn4FRaYzhfgs1jmQvO1iHxYDkd3SsHZ_fasDskA_FnrRYXwaoTYk_bFZyqo4JprrH5re36zGue2VzwVym9_hzOQ1Lhxs2MV5CZJim81eQCO2JwD_3HO8ALtn-ORgXOKSN98SpE3kZL-cLzOZxa4vk0aOPcC_TGXZhKNKqhvmYLadyP7H6rhPXhHz4lB--PTMyF-a5CE2z5NtgegP8xGiN6d3zXeBl6ihtNqJOpmd6PuR9S_PDFPrHZA4X8JK6QTMSX&q=Bourns+3590S&ved=1t:220175&ictx=111&biw=1707&bih=772&dpr=1.13"  # <-- put the text/URL you want encoded here
# =======================================================


def generate_qr(data: str, filename: str = "qr.png", box_size: int = 10, border: int = 4,
				fill_color: str = "black", back_color: str = "white") -> str:
	"""Generate a QR image from `data` and save it to `filename`.

	Returns the filename where the image was saved.
	"""
	qr = qrcode.QRCode(
		version=None,
		error_correction=qrcode.constants.ERROR_CORRECT_M,
		box_size=box_size,
		border=border,
	)
	qr.add_data(data)
	qr.make(fit=True)
	img = qr.make_image(fill_color=fill_color, back_color=back_color)
	img.save(filename)
	return filename


if __name__ == "__main__":
	# Allow overriding the `qr_data` from the command line: ``python a1.py "my text"``
	data = qr_data
	if len(sys.argv) > 1:
		data = sys.argv[1]

	out = generate_qr(data)
	print(f"QR saved to: {out}")

