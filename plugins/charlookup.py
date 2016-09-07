import re
from cloudbot.util import http, web
from cloudbot import hook
from urllib.parse import urlencode

@hook.command
def char(text, bot):
	"""finds a toon and drops general information on them"""
	classes = ["Warrior", "Paladin", "Hunter", "Rogue", "Priest", "Death Knight", "Shaman", "Mage", "Warlock", "Monk", "Druid", "Demon Hunter"]
	races = ["Human", "Orc", "Dwarf", "Night Elf", "Undead", "Tauren", "Gnome", "Troll", "Goblin", "Blood Elf", "Draenei"]
	genders = ["Male", "Female"]
	factions = ["Alliance", "Horde", "Neutral"]
	try:
		api_key = bot.config.get("api_keys", {}).get("wow", None)
	except:
		return "No api key found."
	try:
		if text.count(' ') is 2: 
			name, realm, location = text.split(" ")
		else: 
			name, realm = text.split(" ")
			location = "us"
	except:
		return "You need to specify a realm."
	try:
		location = location.lower()
		if location == 'us':
			data = http.get_json("https://us.api.battle.net/wow/character/{}/{}?fields=guild&locale=en_US&apikey={}".format(realm, name, api_key))
		elif location == 'eu':
			print("location is eu")
			data = http.get_json("https://eu.api.battle.net/wow/character/{}/{}?fields=guild&locale=en_US&apikey={}".format(realm, name, api_key))
		else:
			return "I didn't understand that location. Use US, or EU."
	except Exception as e:
		return e
	try:
		battlegroup = data["battlegroup"]
		clas = classes[(data["class"]-1)]
		gender = genders[(data["gender"])]
		ach_points = data["achievementPoints"]
		level = data["level"]
		race_n = data["race"]
		if race_n is 25 or 26: race = "Pandaren"
		else: race = races[(race_n - 1)]
		faction = factions[(data["faction"])]
		kills = data["totalHonorableKills"]
		name = data["name"]
		realm = data["realm"]
		try:
			guild = data["guild"]["name"]
		except:
			guild = "Forever Alone (No Guild)"
	except Exception as e:
		return "Failed to fetch data. Error: {}.".format(e)

	return "\x02{}\x02, \x02{}\x02 is a level {}, {} {} {}. They have \x02{}\x02 kills, \x02{}\x02 achievement points, and they are a part of \x02{}\x02. Their guild is \x02{}\x02.".format(name, realm, level, gender, race, clas, kills, ach_points, battlegroup, guild)

@hook.command
def pvp(text, bot):
	"""finds a toon and drops their pvp info"""
	try:
		api_key = bot.config.get("api_keys", {}).get("wow", None)
	except:
		return "No api key found."
	try:
		if text.count(' ') is 2: 
			name, realm, location = text.split(" ")
		else: 
			name, realm = text.split(" ")
			location = "us"
	except:
		return "You need to specify a realm."
	try:
		location = location.lower()
		if location == 'us':
			data = http.get_json("https://us.api.battle.net/wow/character/{}/{}?fields=pvp&locale=en_US&apikey={}".format(realm, name, api_key))
		elif location == 'eu':
			data = http.get_json("https://eu.api.battle.net/wow/character/{}/{}?fields=pvp&locale=en_US&apikey={}".format(realm, name, api_key))
	except Exception as e:
		return "Something went wrong. Error {}".format(e)
	try:
		twos_rating = data["pvp"]["brackets"]["ARENA_BRACKET_2v2"]["rating"]
		twos_lost = data["pvp"]["brackets"]["ARENA_BRACKET_2v2"]["seasonLost"]
		twos_won = data["pvp"]["brackets"]["ARENA_BRACKET_2v2"]["seasonWon"]
		threes_rating = data["pvp"]["brackets"]["ARENA_BRACKET_3v3"]["rating"]
		threes_lost = data["pvp"]["brackets"]["ARENA_BRACKET_3v3"]["seasonLost"]
		threes_won = data["pvp"]["brackets"]["ARENA_BRACKET_3v3"]["seasonWon"]
		skrims_rating = data["pvp"]["brackets"]["ARENA_BRACKET_2v2_SKIRMISH"]["rating"]
		skrims_lost = data["pvp"]["brackets"]["ARENA_BRACKET_2v2_SKIRMISH"]["seasonLost"]
		skrims_won = data["pvp"]["brackets"]["ARENA_BRACKET_2v2_SKIRMISH"]["seasonWon"]
		rbg_rating = data["pvp"]["brackets"]["ARENA_BRACKET_RBG"]["rating"]
		rbg_lost = data["pvp"]["brackets"]["ARENA_BRACKET_RBG"]["seasonLost"]
		rbg_won = data["pvp"]["brackets"]["ARENA_BRACKET_RBG"]["seasonWon"]
		#fives_rating = data["pvp"]["brackets"]["UNKNOWN"]["rating"] //fives is gone... For now.
		#fives_lost = data["pvp"]["brackets"]["UNKNOWN"]["weeklyLost"]
		#fives_won = data["pvp"]["brackets"]["UNKNOWN"]["weeklyWon"]
	except Exception as e:
		return "Error: {}".format(e)
	return "2v2s: {} \x02\x033 {} \x03\x02-\x02\x034 {} \x03\x02 | 3v3s: {} \x02\x033 {} \x03\x02-\x02\x034 {} \x03\x02 | RBGs: {} \x02\x033 {} \x03\x02-\x02\x034 {} \x03\x02 | Skrims: {} \x02\x033 {} \x03\x02-\x02\x034 {} \x03\x02".format(twos_rating, twos_won, twos_lost, threes_rating, threes_won, threes_lost, rbg_rating, rbg_won, rbg_lost, skrims_rating, skrims_won, skrims_lost)