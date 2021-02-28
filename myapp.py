
from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    # Use a breakpoint in the code line below to debug your script.
    return "hi ! my Flask only"  # Press Ctrl+F8 to toggle the breakpoint.

@app.route("/tst")
def tst():
    return "hi ! my Flask tst"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
    # print_hi('PyCharm')