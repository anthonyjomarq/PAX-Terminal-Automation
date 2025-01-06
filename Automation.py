import csv
from sikuli import *  #SikuliX is used for automation

# CSV file path
file_path = 'terminal_datacsv.csv'

# Read CSV file
with open(file_path, mode='r') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    
    if rows:
        # Extract second data row
        second_row = rows[0]
        MID = second_row.get('MID', '')
        merchant_name = second_row.get('Merchant Name', '')
        terminal_name = second_row.get('Terminal Name', '')
        serial_number = second_row.get('SN', '')
        TID = second_row.get('TID', '')
        model = second_row.get('Model', '')
        phonenumber = second_row.get('Phone number (NO -)', '')
        email = second_row.get('Email', '')
        city = second_row.get('City', '')
        customer_name = second_row.get('Customer Name', '')
        zipcode = second_row.get('Zip Code', '')
        street = second_row.get('Street', '')

        # Print data for debugging
        print(f"MID: {MID}, Merchant: {merchant_name}, Terminal: {terminal_name}")
    else:
        print("Error: No data rows found.")

# Handle email popup
def handle_email_popup():
    popup_image = "Closepopup.png"
    if exists(popup_image, 2):  # Wait 2 seconds
        print("Closing popup...")
        click(popup_image)
        wait(1)  # Allow time for closure
    else:
        print("No popup.")

# Open PAX portal and search merchant
click("terminal_management.png")
click("search_merchant_field.png")
type(merchant_name)
type(Key.ENTER)
wait(2)

# Add a terminal
click("addterminal.png")
click("terminalname.png")
type(terminal_name)
click("Immediately.png")  # Activate immediately
click("Manufacturer.png")
click("PAX.png")
click("model.png")
click("A920.png")
click("sn.png")
type(serial_number)
click("okpax.png")

# Push app to terminal
click("pushtask.png")
click("pushapp.png")
wait(3)
click("searchapp.png")
type("omaha")
click("searchomaha.png")
wait(3)

# Find and select Omaha app
if exists("Omaha.png"):
    target_logo = find("Omaha.png")
    box_x = target_logo.getX() - 25
    box_y = target_logo.getY() + target_logo.getH() // 2
    click(Location(box_x, box_y))
    print("Clicked target box.")
else:
    print("Error: Omaha logo not found.")
    exit()

click("Okapp.png")
wait(2)

# Configure OMAHA settings
click("edc.png")

# Configure refund settings
click("Refund.png")
click("enable.png")

# Configure void settings
click("Void.png")
click("enable.png")
click("voidcompletion.png")
click("enable.png")
click("voidforced.png")
click("enable.png")
click("voidrefund.png")
click("enable.png")
click("voidpre.png")
click("enable.png")

# Configure credit features
click("creditfeatures.png")
wait(0.5)

# Configure debit settings
click("debit.png")
click("Void.png")
click("disable.png")
click("debit.png")
wait(0.5)

# Configure EBT features
click("ebtfeatures.png")
click("ebtedc.png")
click("disable.png")
click("ebtfeatures.png")
wait(0.5)

# Configure cash features
click("cashfeatures.png")
click("cashedc.png")
click("enable.png")
click("Refund.png")
click("enable.png")
click("Void.png")
click("enable.png")
click("voidrefund.png")
click("enable.png")
click("cashfeatures.png")
wait(0.5)

# Configure receipt information
click("receipt.png")
click("h1.png")
type(merchant_name)
click("h2.png")
type(street)
click("h3.png")
type(city + ", Puerto Rico " + zipcode)

# Format and enter phone number
formatted_phonenumber = f"{phonenumber[:3]}-{phonenumber[3:6]}-{phonenumber[6:]}"
click("h4.png")
type(formatted_phonenumber)

# Configure First Data OMAHA settings
click("firstdata.png")
click("hostfeatures.png")
click("mid.png")
type(MID)
click("device.png")
type(TID)
wheel(WHEEL_DOWN, 6)
wait(1)

handle_email_popup()
click("saveomaha.png")
wait(3)
wheel(WHEEL_DOWN, 10)
wait(1)

handle_email_popup()
click("next.png")
wait(2)

click("1734557778784.png")
click("okpush.png")

# Set timezone
click("timezone.png")
click("puertorico.png")

handle_email_popup()
click("activate.png")
wait(1)
handle_email_popup()
click("ok.png")

# Install TERMLINK and DYNAPAY apps
wait(1)
click("back.png")

# Push TermLink app
wait(1)
click("pushapp.png")
wait(3)
click("searchapp.png")
type("termlink")
click("searchomaha.png")
wait(3)
click("termlink.png")
click("ok.png")

handle_email_popup()
click("next.png")
click("push.png")
click("okpush.png")

click("timezone.png")
click("puertorico.png")

handle_email_popup()
click("activate.png")
handle_email_popup()
click("ok.png")
wait(2.5)

# Configure DynaPay app
click("back.png")
wait(0.5)
click("pushapp.png")
wait(3)
click("searchapp.png")
type("dynapay")
click("searchomaha.png")
wait(3)
click("1734987588707.png")
click("ok.png")

# Configure DynaPay settings
wait(1)
click("1735046604808.png")
type(MID)
click("tid.png")
type(TID)

# Configure sale keys
click("salekey.png")
type("?")
click("ebtkey.png")
type("?")

# Disable various features
hover("1735064347255.png")
wheel(WHEEL_DOWN, 11)
wait(1)

click("autoexpreso.png")
click("disable.png")

wait(0.5)
click("1735226597109.png")
click("disable.png")

click("postautho.png")
click("disable.png")

hover("1735047257369.png")
wheel(WHEEL_DOWN, 40)

# Configure food and cash settings
wait(0.5)
click("foodpurchase.png")
click("disable.png")

click("cashpurchase.png")
click("disable.png")

click("foodreturn.png")
click("disable.png")

click("balanceinquiry.png")
click("disable.png")

click("cashpurchasewithcashback.png")
click("disable.png")

click("cashadvance.png")
click("disable.png")

click("foodvoucher.png")
click("disable.png")

click("cashvoucher.png")
click("disable.png")

wheel(WHEEL_DOWN, 6)
wait(0.5)

# Configure manual entry settings
click("manual.png")
click("enable.png")
click("manualcvv.png")
click("enable.png")
click("manualexpdate.png")
click("enable.png")
click("manualzipcode.png")
click("enable.png")
click("cash.png")
click("enable.png")

# Configure additional settings
click("viewmoredata.png")
wheel(WHEEL_DOWN, 12)

wait(1)
click("swipe.png")
click("disable.png")
wait(0.2)
click("1735065364717.png")
click("disable.png")

hover("1735226842568.png")
wheel(WHEEL_DOWN, 7)
wait(1)

# Clear custom fields
click("customfield.png")
type("a", KeyModifier.CTRL)
type(Key.DELETE)

click("ebtcustomfieldpara.png")
type("a", KeyModifier.CTRL)
type(Key.DELETE)

wheel(WHEEL_DOWN, 7)
wait(1)

# Configure tip and batch settings
click("enabletip.png")
click("disable.png")
wait(0.2)
click("1735226949163.png")
click("disable.png")

click("1735065166373.png")
wheel(WHEEL_DOWN, 20)
wait(1)

click("batchdetailprint.png")
click("enable.png")

# Configure shortcuts and auto-close
click("shortcutpayment.png")
click("enable.png")
click("shortcutbatchclose.png")
click("enable.png")
click("shortcutlasttransaction.png")
click("enable.png")
click("autoclose.png")
click("enable.png")
click("autoclosedyna.png")
type("a", KeyModifier.CTRL)
type(Key.DELETE)
type("2300")

# Final activation steps
handle_email_popup()
click("next.png")
click("push.png")
click("okpush.png")

click("timezone.png")
click("puertorico.png")

handle_email_popup()
click("activate.png")
handle_email_popup()
click("ok.png")

# DATAWIRE configuration
import random
from itertools import permutations

# Function to generate random TIDs
def generate_random_tids(base_tid, count=3):
    generated_tids = set()
    while len(generated_tids) < count:
        all_permutations = list(permutations(str(base_tid)))
        all_tids = [''.join(p) for p in all_permutations]
        
        if str(base_tid) in all_tids:
            all_tids.remove(str(base_tid))
        
        random.shuffle(all_tids)
        
        for tid in all_tids:
            if tid not in generated_tids:
                generated_tids.add(tid)
            
            if len(generated_tids) >= count:
                break
    
    return list(generated_tids)

# Open DataWire website
click("1735315456735.png")
wait(1)

# Fill merchant information
click("merchantbusinessname.png")
type(merchant_name)
type(Key.ENTER)
click("dba.png")
type(merchant_name)
type(Key.ENTER)
click("street.png")
type(street)
type(Key.ENTER)
click("1735315520330.png")
type(city)
type(Key.ENTER)
click("state.png")
type("Puerto Rico")
type(Key.ENTER)
click("1734708557556.png")
type(zipcode)
type(Key.ENTER)

# Fill contact information
click("merchantcontactname.png")
type(customer_name)
type(Key.ENTER)
click("merchantcontactnumber.png")
type(phonenumber)
type(Key.ENTER)
click("email.png")
type(email)
type(Key.ENTER)
click("emailconfirm.png")
type(email)
type(Key.ENTER)
click("ademail.png")
type(email)
type(Key.ENTER)

# Configure processing platform
click("platform.png")
click("omahadata.png")
click("software.png")
type("Pax")
type(Key.ENTER)

click("nextdata.png")

# Configure MID and TIDs
click("1734708954324.png")
type(MID)
type(Key.ENTER)

click("1734708981569.png")
type(TID)
click("addtid.png")
wait(0.5)

# Generate and add additional TIDs
generated_tids = generate_random_tids(TID)
for tid in generated_tids:
    click("1734708981569.png")
    type(tid)
    click("addtid.png")
    wait(0.5)

click("submit.png")

# DYNAPAY AGILPAY configuration
click("1735315977827.png")
wait(1)

click("onboarding.png")
click("existente.png")
wait(2)

click("seleccione.png")
wait(0.5)
type(merchant_name)
type(Key.ENTER)
wait(1)

click("1734709271391.png")
wait(1)

click("1734709327165.png")
wait(1)

# Configure terminal settings
click("snagilpay.png")
type(serial_number)

click("1735316186442.png")

click("moneda.png")
click("us.png")

# Configure card credentials
click("credit.png")
click("adquirente.png")
click("ws01.png")

click("midagil.png")
type(MID)
click("tidagil.png")
type(TID)

click("horacierre.png")
type("23")
type(Key.ENTER)

wheel(WHEEL_DOWN, 6)

# Complete configuration
click("nextagil.png")
wait(2)
wheel(WHEEL_DOWN, 10)
wait(0.2)
click("1734709436553.png")

print("Automation process complete!")
