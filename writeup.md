# Walkthrough

Step 1. Navigate to the home page of the website at port 8000 on localhost.

Step 2. Click on the 'View an image' button.

Step 3. Download the .bmp file.

Step 4. In the directory where you have downloaded the image, run the following command to extract the flag embedded in the image (there's no passphrase):
steghide extract -sf stegog.bmp

Step 5. Display the contents of a.txt using the following command to get the first flag:
cat a.txt
Answer key: CTF_SDaT{Image_Stegonagraphy!}

Step 6. Navigate back to the home page, and click on the 'Hear music' button.

Step 7. Download the .wav file.

Step 8. In the directory where you have downloaded the music, run the following command to extract the flag embedded in the file (there's no passphrase):
steghide extract -sf stegog.wav

Step 9. Display the contents of b.txt using the following command to get the second flag:
cat b.txt
Answer key: CTF_SDaT{Audio_Stegonagraphy!}

Step 10. Navigate back to the home page, and click on the 'Decrypt a flag' button.

Step 11. Copy the encrypted flag from the webpage.

Step 12. Open an interactive python interpreter or an online C++ compiler.

Step 13. Run the following code to perform the first stage of decrypting the flag:

In a python interpreter run the following code:

>>> key = 'Z'
>>> encrypted = 'c9<co>;9>hhl>9<ni>;iml9>8l988;mjiohkbchk'
>>> decrypted = ''.join([chr(ord(x)^ord(key)) for x in encrypted])
>>> print(decrypted)

The following C++ program could also do the decryption:

#include <iostream>
using namespace std;

int main(int argc, char* argv[])
{
    char keyChar = 'Z';
    string encryptedStr = "c9<co>;9>hhl>9<ni>;iml9>8l988;mjiohkbchk";
    string decryptedStr;
    for(auto characterVal: encryptedStr)
    {
       decryptedStr.push_back(characterVal^keyChar);
    }
    cout << decryptedStr;

    return 0;
}

The decrypted string is 
9cf95dacd226dcf43da376cdb6cbba7035218921.

Step 14. Do a search on the web to find the string corresponding to the SHA1 hash 9cf95dacd226dcf43da376cdb6cbba7035218921.
Search "sha1 hash 9cf95dacd226dcf43da376cdb6cbba7035218921" on Google to find that the SHA1 hash of 'azerty' is 9cf95dacd226dcf43da376cdb6cbba7035218921.

Step 15. To decrypt the string 'azerty' shift all characters of the string to the right by 7 positions in the English alphabet. 
a --> h
z --> g
e --> l
r --> y
t --> a
y --> f
Answer Key:CTF_SDaT{hglyaf!}

Step 16. Navigate back to the home page, and click on the 'Get a stock price' button.

Step 17. Submit 'Amazon; pwd; find . -iname Flag;' to find that the last flag is in /app/stocks/Flag and that the current working directory is /app. 

Step 18. Navigate back to the home page and click on 'Get a stock price' again.

Step 19. Submit 'Google; cat stocks/Flag;' to see the flag.
Answer Key:CTF_SDaT{Command_Injection!}