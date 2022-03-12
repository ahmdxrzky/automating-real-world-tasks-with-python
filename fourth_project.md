Scenario
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. <br>
The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). <br>
The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. <br>
The contents of the HTML file need to be uploaded to a web service that is already running using Django. <br>
You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server. <br>

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products. <br>
Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. <br>
The email should have a PDF attached with the name of the fruit and its total weight (in lbs). <br>
Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. <br>

What I've done? <br>
1. Create a script to change format to .jpeg and resize all .tiff pictures [changeImage.py]() <br>
2. Create a script to upload all of manipulated pictures [supplier_image_upload.py]() <br>
3. Create a script to upload all descriptions provided by supplier [run.py]() <br>
4. Create a script to generate a PDF file as an attached file for email [reports.py]() <br>
5. Create a script to generate an email message with or without attachment and send it [emails.py]() <br>
6. Create a script to generate a customized PDF file [report_email.py]() <br>
7. Create a script to routinely check CPU, disk, memory usage and hostname resolved [health_check.py]()
