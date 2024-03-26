# Keylogger

Keylogger made in python that works on Linux and Windows

# Usage for Linux

You probably don't have certain libraries for this script, so install with:

```
pip3 install email-to pynput smtplib
```

We run the keylogger

```
python3 Keylogger.py
```

![image](https://github.com/MT-256/Keylogger/assets/127991386/f711633b-3a56-489b-9085-8e206be72dbc)


We receive the response by email

![image](https://github.com/MT-256/Keylogger/assets/127991386/a6d1b3f8-c583-4f72-8fe6-23bd35738be4)

# Usage for Windows

Now if we want to do it with Windows, preferably we should do it in a virtualized Windows 10 service to do it as quickly as possible

Once we have windows, we must install python in windows, when we have everything ready, we open a cmd with administrator permissions and we install pyinstaller and other necessary libraries

```
pip3 install pyinstaller
```

```
pip3 install email-to pynput smtplib
```

Now if we want to make it an executable we will use the following command:

```
pyinstaller --onefile --noconsole key.py
```

![image](https://github.com/MT-256/Keylogger/assets/127991386/8e8db458-c6c0-473f-accd-51d20745ff1d)

If you want to play around with obfuscation, we should remove keywords from the script and remove the 'noconsole'

```
pyinstaller --onefile key.py 
```

# Setting for gmail

In order for the information to reach us by email, we must make several configurations in our Gmail, first we go to settings

![image](https://github.com/MT-256/Keylogger/assets/127991386/753b1145-174d-49a9-b25c-95a54a6a6068)

We must activate two-step verification of the account to be able to use the passwords app

![image](https://github.com/MT-256/Keylogger/assets/127991386/2939a8f4-76ca-42b5-a56a-4e6facdeacf8)

Once verified, we go to the end of the page, we will find the Apps passwords option


![image](https://github.com/MT-256/Keylogger/assets/127991386/8c372a69-ec6f-478e-9780-413dbcc637d7)

We give it the name we want

![image](https://github.com/MT-256/Keylogger/assets/127991386/ef0aead0-3e27-4060-ab16-1b2a5ba9f297)

It will give us a code that we must replace in the part of the script that says "EMAIL_PASSWORD"

![image](https://github.com/MT-256/Keylogger/assets/127991386/bbdcd0c8-dea2-4b0f-a2fc-4bee278bb86b)
