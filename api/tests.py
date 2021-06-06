from api.models import FileUpload
from django.test import TestCase

# Create your tests here.

class FileUploadTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Setup static data.")
        self.title = "MyFile1"
        self.subtitle = "MySubtitle"
        self.author = "myauthor"
        self.subject_code = "my_code"
        self.documentType = "Notes"
        self.file_name = "my_file.pdf"
        self.file_size="20kb"
        self.file_text="Random text"
        self.file_location="edflix/file.pdf"
        pass

    def test_uploadFile(self):
        print("Method: FileUploadTest")
        file = FileUpload(title=self.title,subtitle=self.subtitle,author=self.author,subject_code=self.subject_code,documentType = self.documentType,file_name=self.file_name,file_text=self.file_text,file_size=self.file_size,file_location=self.file_location)
        file.save()
        self.assertTrue(file)

   