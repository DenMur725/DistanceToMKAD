# Finding the distance from the MKAD to the specified address

The distance finding module is implemented on **Flask Blueprint**. The address is transmitted to the application in an **HTTP request**, if
the specified address is located inside the **MKAD**, the distance is not calculated. The result is written to a **.log** file.

## Settings
1. In the `geo` directory, open the `settings` file and install your `yandex-geocoder-key`
2. You can change the name of the logs file

## Operating instructions
0. Start the server and go to the "/geo" page
1. Send a POST request with the address
2. If the address is not inside MKAD, it will be made into a .log file
3. If the request is incorrect or the address is inside the MKAD, a message will be displayed

Modules used in the project: `flask`, `yandex_geocoder`, `geopy`, `pytest`, `os`