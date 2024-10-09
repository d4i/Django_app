# Django_app

How to run the app?
1. Clone the repository:
   git clone https://github.com/yourusername/Django_app.git
   cd Django_app

2. Create a virtual environment and activate it:
    run the below command in cmd
     python -m venv env
     .\env\Scripts\activate

3. Install the required packages:
     pip install -r requirements.txt
4. Start the django development server
     python manage.py runserver 0.0.0.0:8000
5. http://13.60.167.87:8000

6. Access specific pages:
    Upload images: /upload/
    List uploaded images: /list/

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
