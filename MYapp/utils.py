def image_saver(image_obj, image, category):
    if  image_obj:
        if image:
            image_obj.image = image
        if category:
            image_obj.image_category = category
        image_obj.save()
