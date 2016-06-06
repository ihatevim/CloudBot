import re
from cloudbot.util import http
from cloudbot import hook
import json
import requests
base_url = "http://api.genius.com/search?q=foo&access_token={}"
	
@hook.command('lyr')
@hook.command
def lyrics(text, bot, reply):
	"""lyrics <song> -- Search genius for a specific song"""
	access_token = bot.config.get("api_keys", {}).get("genius_access_token", None)
	if not access_token:
		reply("An API key is needed to use this application.")
	try:
		data = http.get_json((base_url.format(access_token)), q=text.strip())
	except Exception as e:
		reply("Could not find song: {}".format(e))
	try:
		song = data["response"]["hits"][0]["index"]
	except IndexError:
		reply("Could not find song")
	reply("{} by {} - {}".format(data["response"]["hits"][0]["result"]["title"], data["response"]["hits"][0]["result"]["primary_artist"]["name"], data["response"]["hits"][0]["result"]["url"]))