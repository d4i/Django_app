# Django_app

**Milestone 1: Basic Image Upload and Listing**  ||ACHIEVED||
The basic image uploading is done by using POST method in ImageUploadForm() in s3 using the bucket named d4ibucket.
The listing is done using list_objects_v2() 

The image will be uploaded via upload_image.html and listing and downloading will be done by list_images.html

**Milestone 2: Implementing Encryption**  ||ACHIEVED||
The original upload method is re-written with encryption. (used cryptography)
Added a checkbox labeled "Show only encrypted images."


**Milestone 3: Decryption and Advanced Download Options**  ||ACHIEVED||

download_image() method is used to decrypt and download image

**Milestone 4: User Authentication**
created signup.html page for new users  
