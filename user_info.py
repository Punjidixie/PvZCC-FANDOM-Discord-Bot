import caller
import discord
import groups_parser as gp
from datetime import datetime

def call_and_get_user_json(username):
    url_segment = f"api.php?action=query&list=users&usprop=groups|editcount|registration&ususers={username}&format=json"
    
    return caller.get_json(url_segment)

def call_and_get_firstedit_json(username):
    url_segment = f"api.php?action=query&format=json&list=usercontribs&ucuser={username}&ucdir=newer&uclimit=1"
    
    return caller.get_json(url_segment)

def generate_response(username):
    
    
    
    j = call_and_get_user_json(username)
    user_info = j["query"]["users"][0]
    
    desc = "This user is on PvZCC!"
    
    # Check of the user has edited on the wiki.
    is_pvzccer = False
    if "missing" in user_info:
        desc = "This user doesn't exist. Make sure you entered the correct username (case sensitive)."
    elif user_info["editcount"] == 0:
        desc = "This user has never been in PvZCC."
    else: is_pvzccer = True
             
    # Base of the embed response
    embed = discord.Embed(
            description = f"{desc}",
            title = username.replace("_", " ")
            )
    
    # Constructing the response body
    if is_pvzccer:
        jf = call_and_get_firstedit_json(username)
        contrib = jf["query"]["usercontribs"][0]
        
        parsed_join_date = datetime.strptime(contrib["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
        formatted_join_date = parsed_join_date.strftime("%B %d, %Y")
        #join_time_difference = datetime.now() - parsed_join_date
        
        parsed_reg_date = datetime.strptime(user_info["registration"], "%Y-%m-%dT%H:%M:%SZ")
        formatted_reg_date = parsed_reg_date.strftime("%B %d, %Y")
        #reg_time_difference = datetime.now() - parsed_reg_date
        
    
        
        groups = user_info["groups"]
        group_name = gp.group_name(gp.highest_group(groups))
        edit_count = user_info["editcount"]
        
        embed.add_field(name="Edit count",value=edit_count, inline = False)
        embed.add_field(name="Group",value=group_name, inline = False)
        
        embed.add_field(name="First PvZCC edit",value=formatted_join_date)
        #embed.add_field(name="Days ago",value=join_time_difference.days)
        
        embed.add_field(name="Account creation",value=formatted_reg_date)
        #embed.add_field(name="Days ago",value=reg_time_difference.days)
        
        #embed.add_field(name="First edit time",value=formatted_join_time)
    
    return embed
                                      
    
    
    


    