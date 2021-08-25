from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from PIL import Image

from .models import Produto


@receiver(post_save, sender=Produto, dispatch_uid="update_produto_image")
def resize_image(sender, instance, **kwargs):
    NEW_WIDTH = 800
    img = Image.open(instance.imagem.path)

    width, height = img.size

    new_height = round((NEW_WIDTH * height) / width)
    if width <= NEW_WIDTH:
        img.close()
        return

    img.resize((NEW_WIDTH, new_height)).save(instance.imagem.path)
    img.close()


@receiver(pre_save, sender=Produto)
def slugify_product(sender: Produto, instance: Produto, **kwargs):
    if not instance.slug:
        slug: str = slugify(f"{instance.nome}-{instance.pk}")
        instance.slug = slug
