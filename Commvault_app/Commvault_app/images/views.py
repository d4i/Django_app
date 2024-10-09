from django.http import HttpResponse
from django.shortcuts import render, redirect
from cryptography.fernet import Fernet
from Commvault_app.forms import ImageUploadForm
from django.contrib.auth.decorators import login_required
from ..forms import ImageUploadForm
import boto3

# Create S3 client
s3 = boto3.client('s3')

# Bucket name
BUCKET_NAME = 'd4ibucket'

# Upload Image
# def upload_image(request):
    # if request.method == 'POST':
    #     form = ImageUploadForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         image = request.FILES['image']
    #         s3.upload_fileobj(image, BUCKET_NAME, image.name)
    #         return redirect('list_images')
    # else:
    #     form = ImageUploadForm()
    # return render(request, 'upload_image.html', {'form': form})

# List Images
def list_images(request):
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    images = response.get('Contents', [])
    return render(request, 'list_images.html', {'images': images})

# Generate a key for encryption/decryption (store this securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)


@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        encrypt = request.POST.get('encrypt', False)  # Checkbox for encryption
        
        if form.is_valid():
            image = request.FILES['image']
            
            if encrypt:
                encrypted_image = cipher_suite.encrypt(image.read())  # Encrypt the image
                s3.upload_fileobj(encrypted_image, BUCKET_NAME, image.name)
            else:
                s3.upload_fileobj(image, BUCKET_NAME, image.name)
            
            return redirect('list_images')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def download_image(request, file_name):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=file_name)
    encrypted_image = response['Body'].read()
    
    # Decrypt image
    decrypted_image = cipher_suite.decrypt(encrypted_image)
    
    # Return the image as an HTTP response
    return HttpResponse(decrypted_image, content_type='image/jpeg')

