# encryption

Pretty bad attempt at making an encryption algorithm. This is by no means finished, it works horribly right now

## how it works
This algorithm uses ord() and chr() to get ASCII (or Unicode idk) values for each character you give. It alters the values and turns them back into ASCII (or Unicode, i have no idea)

## examples

### encrypt.py
```
What's the key? 2
What's the message? encrypted
encrypted text: 𐱭𐳐𐱗𐳼𐵉𐳦𐴒𐱭𐱢
```
### decrypt.py
```
What's the key? 2
What's the encrypted message? ������������������
decrypted text: encrypted
```

## how to use it

Let me start off with this: Don't actually use this. This is the worst thing you could use to protect yourself.

That being said, if you want to see how bad it is:
- Fill in the key field as a very small integer (no more than 5, it'll completely break)
- Fill in some text
- It will now give you ~garbled~ encrypted text

The same goes for the decryption algorithm:
- Fill in the key field with the same key you used on encrypt.py
- Copy-paste the encrypted text from encrypt.py's output
- It will give you back your original output

