# Dependencies
import os
import time
import platform
import http
from bottle import Bottle, static_file

# Functions
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def host():
    filename = "My-identity.html"
    if not os.path.exists(filename):
        print(f"Error: '{filename}' does not exist!")
        return

    app = Bottle()

    @app.route('/')
    def serve_identity():
        return static_file(filename, root='.')

    print(f"Starting local server at http://localhost:8080 ...")
    app.run(host='localhost', port=8080)

# Main logo
clear() # clean looks matter
print("""
██╗    ██╗███████╗██████╗       ██╗██████╗  ██████╗ █████╗ ██████╗ ██████╗ 
██║    ██║██╔════╝██╔══██╗      ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝█████╗██║██║  ██║██║     ███████║██████╔╝██║  ██║
██║███╗██║██╔══╝  ██╔══██╗╚════╝██║██║  ██║██║     ██╔══██║██╔══██╗██║  ██║
╚███╔███╔╝███████╗██████╔╝      ██║██████╔╝╚██████╗██║  ██║██║  ██║██████╔╝
 ╚══╝╚══╝ ╚══════╝╚═════╝       ╚═╝╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
                                                                           
""")
print("Generate identity cards in HTML, with relevant information")
time.sleep(2)
clear()

# Program
print("""
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗███████╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   █████╗  
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██╔══╝  
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ███████╗
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                                                               
""")
print("Fill in the fields, properly.")
time.sleep(1)

# Fields
name1 = input("Your first name: ")
name2 = input("Your middle + last name: ")
email = input("Your email: ")
phone = input("Your telephone/mobile number: ")
country = input("Your country: ")
dob = input("Your date of birth (Any format): ")
zipc = input("Your zip code: ")
time.sleep(2)

# Main
pfp = name1[0] + name2[0]
html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Identity Card</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body style="background-color: #f4f4f5; font-family: system-ui, -apple-system, sans-serif;" class="min-vh-100 d-flex align-items-center justify-content-center p-3">

    <div class="card border-0 shadow-lg" style="width: 100%; max-width: 420px; border-radius: 24px; overflow: hidden;">
        <!-- Header -->
        <div style="height: 110px; background-color: #111827; position: relative;">
            <div class="bg-white rounded-circle d-flex align-items-center justify-content-center fw-bold fs-4" 
                 style="width: 72px; height: 72px; position: absolute; bottom: -36px; left: 28px; border: 4px solid white;">
                {pfp}
            </div>
        </div>

        <!-- Content -->
        <div class="card-body p-4" style="padding-top: 52px !important;">
            <h5 class="card-title fw-bold mb-1" style="font-size: 22px;">{name1} {name2}</h5>
            <p class="text-uppercase mb-4" style="font-size: 11px; letter-spacing: 0.1em; color: #9ca3af;">GENERATED</p>

            <div class="d-flex flex-column gap-3">
                <div>
                    <div class="text-uppercase fw-bold" style="font-size: 10px; letter-spacing: 0.14em; color: #9ca3af;">Full Name</div>
                    <div class="fw-medium mt-1" style="font-size: 15px;">{name1} {name2}</div>
                </div>

                <hr class="my-1" style="color: #f3f4f6; opacity: 1;">

                <div>
                    <div class="text-uppercase fw-bold" style="font-size: 10px; letter-spacing: 0.14em; color: #9ca3af;">Email Address</div>
                    <div class="fw-medium mt-1" style="font-size: 15px;">{email}</div>
                </div>

                <div>
                    <div class="text-uppercase fw-bold" style="font-size: 10px; letter-spacing: 0.14em; color: #9ca3af;">Phone Number</div>
                    <div class="fw-medium mt-1" style="font-size: 15px;">{phone}</div>
                </div>

                <div>
                    <div class="text-uppercase fw-bold" style="font-size: 10px; letter-spacing: 0.14em; color: #9ca3af;">Date of Birth</div>
                    <div class="fw-medium mt-1" style="font-size: 15px;">{dob}</div>
                </div>

                <div class="row">
                    <div class="col-6">
                        <div class="text-uppercase fw-bold" style="font-size: 10px; letter-spacing: 0.14em; color: #9ca3af;">Country</div>
                        <div class="fw-medium mt-1" style="font-size: 15px;">{country}</div>
                    </div>
                    <div class="col-6">
                        <div class="text-uppercase fw-bold" style="font-size: 10px; letter-spacing: 0.14em; color: #9ca3af;">Zip Code</div>
                        <div class="fw-medium mt-1" style="font-size: 15px;">{zipc}</div>
                    </div>
                </div>
            </div>

            <div class="d-flex align-items-center justify-content-between mt-4 p-3 rounded-3" style="background-color: #f9fafb;">
                <small class="text-muted" style="font-size: 11px;">Generated by Identity Generator</small>
                <span class="rounded-circle bg-success" style="width: 8px; height: 8px; display: inline-block;"></span>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
with open(f"My-identity.html", "w") as f:
    f.write(html)

print("Sucessfully Generated!")
time.sleep(2)
clear()

# HTTP
usrin = input("Do you wish to preview this file in a server [Y/N]: ")
if (usrin == "Y"):
    print("Starting...")
    time.sleep(1)
    host()
elif (usrin == "N"):
    print("Exiting...")
    time.sleep(1)
    exit()
else:
    exit()

# By Vyom
# 2026
