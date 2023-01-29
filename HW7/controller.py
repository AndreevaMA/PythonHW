import manual_input as mi
import data_input as di
import csv_export as expit
import csv_read as read
import csv2html as c2h


def button_click(choice):
    
    if choice == 1:
        result = mi.user_input()
        expit.catalog_update(result)

    if choice == 2:
        result = di.bulk_read()
        expit.catalog_update(result)

    if choice == 3:
        read.find_contact()

    if choice == 4:
        c2h.html_create()

