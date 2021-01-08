# Password leak finder - plf
PFL is a sample program implemented using Python 3 and PyQt5 GUI. It makes use of a **famous** website https://haveibeenpwned.com/ and its API.

# How it works....

This program uses an above site to check if your password ever leaked. However page doesnt know your password. How is that?Its because of K-Anonymity. Read this:

https://passwordbits.com/haveibeenpwned-checks-password/ (great explanation)

or just watch this:

https://www.youtube.com/watch?v=hhUb5iknVJs
(tip: this program works quite similar to what this guru made in the video.)

But if you are still afraid of typing your precious password on some strange web , you can just use this app.

## Requirements

For app to work you need python(>3.6) and and pyqt5. You do not have to use requirements.txt since it is really simple program. Of course you can use virtual environment to test it out. Go like this:

```console 
$ sudo pip install pyqt5
```
## How to

For program to work type:

```console
python3 plf.py
```
Then just follow the instruction

## About the Author

My name is Adrian Gąsior. I'm an aspiring ML eng who tries to master python. 

## License

PLF is released under the [MIT License](https://opensource.org/licenses/MIT).



