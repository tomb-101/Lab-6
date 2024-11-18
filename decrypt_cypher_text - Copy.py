def decrypt_cypher_text(encrypted_text, key):
    # function implementation here...
    decrypted_list=[]
    decrypted_text=""
    for item in encrypted_text:
        decrypted_list.append((ord(item)-key))
    for num in decrypted_list:
        decrypted_text+=chr(num)
    return decrypted_text

# print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$", 3))