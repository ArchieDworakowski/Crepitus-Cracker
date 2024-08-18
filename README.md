Place any image that have suspicion of steganography in the same directory as the program, and when it is run, it will detect, and attempt to extract any data hidden in the image

This prototype runs on debian linux systems only


Example output, where stegImage is steganography hiding an image, and stegText is steganography hiding text:

Scan Time:     2024-08-18 12:11:43
Target File:   /home/archd13/Downloads/stegFinal/final.py
MD5 Checksum:  f4cc040062f81cf0682d6fd77ff46af4
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------


Scan Time:     2024-08-18 12:11:43
Target File:   /home/archd13/Downloads/stegFinal/original.jpg
MD5 Checksum:  f86b8d07751d0300a30a1af2096c11dc
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01


Scan Time:     2024-08-18 12:11:43
Target File:   /home/archd13/Downloads/stegFinal/stegImage.png
MD5 Checksum:  772dba6f1587d54a7fbc2b36f6bc481f
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 800 x 1000, 8-bit/color RGBA, non-interlaced
54            0x36            Zlib compressed data, compressed


Scan Time:     2024-08-18 12:11:43
Target File:   /home/archd13/Downloads/stegFinal/stegText.png
MD5 Checksum:  d727d60f2c681eac9e3f0a5e36224f96
Signatures:    411

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 800 x 1000, 8-bit/color RGB, non-interlaced
62            0x3E            Zlib compressed data, default compression

possible steganography in _stegImage.png.extracted
possible steganography in _stegText.png.extracted
