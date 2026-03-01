from PIL import Image
import os
def encrypt_decrypt_imapge(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b =pixels[x, y]
            r_new = r ^ key
            g_new = g ^ key
            b_new = b ^ key 
            pixels[x, y] = (r_new, g_new, b_new)

image.save(output_path)
print( f"Image saved to {output_path}")            
 key = 123 

encrypt_decrypt_imapge(
   input_path="Original.png",
   output_path="encrypted.png",
   key=key
)
encrypt_decrypt_imapge(
    input_path="encrypted.png",
    output_path="decrypted.png"
    key=key
)