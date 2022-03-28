<h3> Scenario </h3>
You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers.
The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).
The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description.
The contents of the HTML file need to be uploaded to a web service that is already running using Django.
You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.
<br><br>

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.
Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded.
The email should have a PDF attached with the name of the fruit and its total weight (in lbs).
Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong.
<br><br>

What I've done? <br>
1. Create a script to change format of pictures from .tiff to .jpeg and resize it --> [changeImage.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/changeImage.py) <br>
2. Create a script to upload all of manipulated pictures in .jpeg format --> [supplier_image_upload.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/supplier_image_upload.py) <br>
3. Create a script to upload all descriptions provided by supplier --> [run_fruit.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/run_fruit.py) <br>
4. Create a script to generate a PDF file as an attached file for email --> [reports.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/reports.py) <br>
5. Create a script to generate an email message with or without attachment and send it --> [emails.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/emails.py) <br>
6. Create a script to generate a customized PDF file --> [report_email.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/report_email.py) <br>
7. Create a script to routinely check CPU, disk, memory usage and hostname resolved --> [health_check.py](https://github.com/ahmdxrzky/google-it-automation-with-python/blob/main/automating_real_world_tasks_with_python/health_check.py)
