from browser.html import *


def gen_info():
	shipstats = {
		"Epheria Sailboat": {
			"HP": "1,000,000",
			"Rations": "1,000,000",
			"Base LT": "5,000",
			"Speed": "100%",
			"Accel": "100%",
			"Turn": "110%",
			"Brake": "110%",
			"Inventory": "25 slots",
			"Cabins": "10",
			"Cannon Count": "1 per side(player)",
			"Reload": "17s"
		},
		"Improved Sailboat": {
			"HP": "1,000,000",
			"Rations": "1,000,000",
			"Base LT": "5,000",
			"Speed": "100%",
			"Accel": "100%",
			"Turn": "110%",
			"Brake": "110%",
			"Inventory": "25 slots",
			"Cabins": "10",
			"Cannon Count": "2 per side(captain)",
			"Reload": "15s"
		},
		"Epheria Caravel": {
			"HP": "1,000,000",
			"Rations": "1,100,000",
			"Base LT": "10,000",
			"Speed": "100%",
			"Accel": "100%",
			"Turn": "110%",
			"Brake": "110%",
			"Inventory": "30 slots",
			"Cabins": "30",
			"Cannon Count": "2 per side(captain)",
			"Reload": "15s"
		},
		"Carrack (Advance)": {
			"HP": "1,350,000",
			"Rations": "1,300,000",
			"Base LT": "16,500",
			"Speed": "110%",
			"Accel": "100%",
			"Turn": "115%",
			"Brake": "115%",
			"Inventory": "40 slots",
			"Cabins": "50",
			"Cannon Reload": "15s"
		},
		"Carrack (Balance)": {
			"HP": "1,300,000",
			"Rations": "1,400,000",
			"Base LT": "15,000",
			"Speed": "115%",
			"Accel": "100%",
			"Turn": "115%",
			"Brake": "115%",
			"Inventory": "35 slots",
			"Cabins": "50",
			"Cannon Reload": "14s"
		},
		"Epheria Frigate": {
			"HP": "1,200,000",
			"Rations": "1,000,000",
			"Base LT": "4,000",
			"Speed": "110%",
			"Accel": "110%",
			"Turn": "120%",
			"Brake": "120%",
			"Inventory": "12 slots",
			"Cabins": "10",
			"Cannon Count": "2 per side(player)",
			"Reload": "17s"
		},
		"Improved Frigate": {
			"HP": "1,200,000",
			"Rations": "1,000,000",
			"Base LT": "4,000",
			"Speed": "110%",
			"Accel": "110%",
			"Turn": "120%",
			"Brake": "120%",
			"Inventory": "12 slots",
			"Cabins": "10",
			"Cannon Count": "4 per side(captain)",
			"Reload": "15s"
		},
		"Epheria Galleass": {
			"HP": "1,200,000",
			"Rations": "1,200,000",
			"Base LT": "8,000",
			"Speed": "110%",
			"Accel": "110%",
			"Turn": "120%",
			"Brake": "120%",
			"Inventory": "15 slots",
			"Cabins": "30",
			"Cannon Count": "4 per side(captain)",
			"Reload": "15s"
		},
		"Carrack (Volante)": {
			"HP": "1,250,000",
			"Rations": "1,400,000",
			"Base LT": "13,500",
			"Speed": "120%",
			"Accel": "110%",
			"Turn": "115%",
			"Brake": "125%",
			"Inventory": "20 slots",
			"Cabins": "50",
			"Cannon Reload": "13s"
		},
		"Carrack (Valor)": {
			"HP": "1,300,000",
			"Rations": "1,500,000",
			"Base LT": "13,500",
			"Speed": "115%",
			"Accel": "110%",
			"Turn": "115%",
			"Brake": "125%",
			"Inventory": "20 slots",
			"Cabins": "50",
			"Cannon Reload": "12s"
		},
	}
	order = [
		["Epheria Sailboat", "Improved Sailboat", "Epheria Frigate", "Improved Frigate"],
		["Epheria Caravel", "Epheria Galleass"],
		["Carrack (Advance)", "Carrack (Balance)", "Carrack (Volante)", "Carrack (Valor)"]
	]
	ret = P("More information can be found " + A("at this spreadsheet", href="https://docs.google.com/document/d/1basknMfrfcH6AzJD9PkzeUunqrIGTuS6SfXPf3a7pso/preview", target="_blank") +" or " + A("these patch notes", href="https://www.blackdesertonline.com/news/view/3216", target="_blank"))
	ret += P("Barter items that you can trade for ship parts unlock as you finish more trades.  You can always trade t1 barter items for verdant stone coupon though.")
	ret += P("Ship parts used for upgrade need to be full durability.")
	ret += P("All sea monsters can drop parts for upgrading ships.  There is no list of which drops are where yet. (Nov-6)")
	ret += P("Old Moon Guild quests for the same monster are mutually exclusive(pick 1).  EG Nineshark and Young Nineshark.")
	ret += H2("Upgrade Paths") + BR() + CANVAS(id='shipchart', width=820, height=400) + BR()
	ret += H2("Base Ship Stats")
	for table in order:
		t = TABLE()
		tr = TR(TH("Stat"))
		for ship in table:
			tr <= TH(ship)
		t <= tr

		for key in shipstats[table[0]]:
			tr = TR(TD(key))
			for ship in table:
				tr <= TD(shipstats[ship][key])
			t <= tr

		ret += t + BR()
	return ret