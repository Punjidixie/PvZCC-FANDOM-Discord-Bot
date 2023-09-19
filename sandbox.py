import requests
import caller


fandom_link = "https://pvzcc.fandom.com"

req_suffix = "api.php?action=query&list=users&usprop=groups|editcount|registration&ususers=PunjiChocoBerry&format=json"

print(caller.get_json(req_suffix))

