## I changed a part of the code, just copy the image link to get the tag on gelbooru ##
You can use image links in the following formats：

> https://img3.gelbooru.com//samples/8f/d8/sample_8fd81ff8b57f9acd8fb8cf8785c1aa8f.jpg
> https://img3.gelbooru.com/images/8f/d8/8fd81ff8b57f9acd8fb8cf8785c1aa8f.jpg
> OR You can also directly input the md5 of the image
> 8fd81ff8b57f9acd8fb8cf8785c1aa8f

# 我更改了一些代码，可以直接输入图片的MD5就能获取图片tag，感谢原作者的代码。 #
# Gelbooru Prompt
Extension that gets tags for saved gelbooru images in AUTOMATIC1111's Stable Diffusion webui

## What is this?
This is a small extension I wrote to let you automatically pull the tags for any saved gelbooru image in [AUTOMATIC1111's stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

## Additional Info:

### How does this work?
This extension just adds a collapsing pane in the UI that allows you to drag and drop any image saved from the image board site Gelbooru.
The image file must still have it's original naming scheme:
- **The MD5 hash must be the title of the image**
- If an image's name begins with "sample_", this extension will automatically ignore it

Example:
> 9d27c7ff0afc26f47bf898c7090f151f.png

All you need to do is hit the "Get Tags" button, and it will put the fetched tags into the textbox below.

You can now use these tags in any prompt crafting you'd like to do. Enjoy!

### Requirements:
This extensions requires beautifulsoup4, you'll need to install it to either your venv or globally depending on your setup

[inside venv/Scripts]
> activate

> pip install beautifulsoup4

## Showcase / Usage:
![example_image](https://user-images.githubusercontent.com/31860133/203446389-01914338-0a1d-4d73-9341-e4101cadfcf7.png)
