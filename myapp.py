
from flask import Flask

myapp=Flask(__name__)

@myapp.route("/")
def home():
    # Use a breakpoint in the code line below to debug your script.
    return "hi ! my Flask only"  # Press Ctrl+F8 to toggle the breakpoint.

@myapp.route("/tst")
def tst():
    return "hi ! my Flask tst"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myapp.run()
    # print_hi('PyCharm')