import random
import re
import traceback

import gradio as gr

from modules import script_callbacks, scripts, shared
from modules.shared import opts
import requests
import bs4
from bs4 import BeautifulSoup




def on_ui_settings():
	section = ('gelbooru-prompt', "Gelbooru Prompt")

def fetch(picurl,proxy):
	print("输入: " + picurl)
	proxies = {
    "http": "%(proxy)s/" % {'proxy': proxy},
    "https": "%(proxy)s/" % {'proxy': proxy}
}
	hash = re.findall(r"([a-fA-F\d]{32})", picurl)[0] #正则提取md5
	print("提取hash: " + hash)

	url = "https://gelbooru.com/index.php?page=post&s=list&tags=md5%3a" + hash
	print(proxies)
	req = requests.get(url, 'html.parser',proxies=proxies)
	soup = BeautifulSoup(req.content , 'html.parser')
	print("拼接url：",url)
	found = None

	articles = soup.find_all("article", class_="thumbnail-preview") # 找到所有<article class="thumbnail-preview">标签
	for article in articles: # 遍历每个标签
		a = article.find("a") # 找到标签下的a标签
		link = a.get("href") # 取出a标签的href值
		print("link:",link)
		if link.startswith("https://gelbooru.com/index.php?page=post"):
			if not link.endswith("tags=all"):
				found = link
				break
	if found is not None:
		print("FOUND: " + found)
		req = requests.get(found, 'html.parser',proxies=proxies) 
		soup = BeautifulSoup(req.content , 'html.parser')
		#tag_data = soup.find_all("textarea")
		tag_data = soup.find_all("textarea", {"id": "tags"})
		if len(tag_data) > 0:
			#print(tag_data)
			tag_data = tag_data[0].string.split(" ")
		else:
			return("Invalid Image Format...")
		parsed = []
		for tag in tag_data:
			tag = tag.replace("_", " ")
			parsed.append(tag)
		#print("Parsed tags: " + str(parsed))
		parsed = (", ").join(parsed)
		#print()
		print(parsed)
		#print()
		return(parsed)
	else:
		return("No image found with that hash...")

class BooruPromptsScript(scripts.Script):
	def __init__(self) -> None:
		super().__init__()
	def title(self):
		return("Gelbooru Prompt")
	def show(self, is_img2img):
		return scripts.AlwaysVisible

	def ui(self, is_img2img):
		with gr.Group():
			with gr.Accordion("Gelbooru Prompt", open=False):
				fetch_tags = gr.Button(value='Get Tags', variant='primary')
				picurl = gr.Textbox(lines=2, placeholder="输入图片md5")
				proxy = gr.Textbox(value = "",label="代理",lines=1,placeholder="格式为http://ip:port")
				tags = gr.Textbox(value = "", label="Tags", lines=5)

		fetch_tags.click(fn=fetch, inputs=[picurl,proxy], outputs=[tags])
		return [picurl, tags, fetch_tags]


script_callbacks.on_ui_settings(on_ui_settings)
