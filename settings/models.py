from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Settings(models.Model):
    hex_validator = RegexValidator(r'^#([A-Fa-f0-9]{6})$', 'Geçerli bir hex renk kodu girin. Örn: #0052c9')

    site_name = models.CharField(max_length=100, default='My Blog')
    header_image = models.ImageField(upload_to='headers/', null=True, blank=True)
    header_image_alt_text = models.CharField(max_length=150, blank=True)
    site_background_color = models.CharField(max_length=7, default='#0052c9', validators=[hex_validator])
    site_text_color = models.CharField(max_length=7, default='#ffffff', validators=[hex_validator])
    blog_post_background_color = models.CharField(max_length=7, default='#f0f0f0', validators=[hex_validator])

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        # Eğer yeni kayıt ekleniyorsa ve zaten bir kayıt varsa hata fırlat
        if not self.pk and Settings.objects.exists():
            raise ValidationError("Sitede yalnızca bir SiteConfiguration olmalı. Mevcut kaydı düzenleyin.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ayarlar"
        verbose_name_plural = "Ayarlar"