from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


# Create your models here.

class Client(models.Model):
    prenomClient = models.CharField(max_length=200, null=True)
    nomClient = models.CharField(max_length=200, null=True)
    ageClient = models.IntegerField(null=True)
    emailClient = models.CharField(max_length=200, null=True)
    telClient = models.CharField(max_length=15, null=True)
    adresse_rueClient = models.CharField(max_length=600, null=True)
    adresse_appartementClient = models.CharField(max_length=600, null=True)
    adresse_villeClient = models.CharField(max_length=600, null=True)
    adresse_cpClient = models.CharField(max_length=600, null=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.prenomClient)

    def save(self, *args, **kwargs):
        adresseClient = self.adresse_villeClient + self.adresse_cpClient + self.adresse_rueClientzonq
        qrcode_img = qrcode.make(adresseClient)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.nomClient}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
