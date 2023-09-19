import caller
import discord
import groups_parser as gp
from datetime import datetime

def call_and_get_user_json(username):
    url_segment = f"api.php?action=query&list=users&usprop=groups|editcount|blockinfo&ususers={username}&format=json"
    
    return caller.get_json(url_segment)

def call_and_get_firstedit_json(username):
    url_segment = f"api.php?action=query&format=json&list=usercontribs&ucuser={username}&ucdir=newer&uclimit=1"
    
    return caller.get_json(url_segment)

def call_and_get_lastedit_json(username):
    url_segment = f"api.php?action=query&format=json&list=usercontribs&ucuser={username}&ucdir=older&uclimit=1"
    
    return caller.get_json(url_segment)

def time_diff_to_string(diff):
    
    num = 0
    unit = "minute"
    suffix = 's'
    
    if diff.seconds // 60 == 0: return "Just now"
    elif diff.seconds // 3600 == 0:
        num = diff.seconds // 60
        unit = "minute"
    elif diff.days == 0:
        num = diff.seconds // 3600
        unit = "hour"
    else:
        num = diff.days
        unit = "day"
    
    if num == 1: suffix = ''
    
    return f"{num} {unit}{suffix} ago"
        
def generate_response(username):
    
    
    
    j = call_and_get_user_json(username)
    user_info = j["query"]["users"][0]
    
    desc = ":white_check_mark: This user is on PvZCC!"
    
    # Check of the user has edited on the wiki + is blocked or not
    is_pvzccer = False
    is_blocked = "blockid" in user_info
    
    if "missing" in user_info:
        desc = ":grey_question: This user doesn't exist. Make sure you entered the correct username (case sensitive)."
    elif user_info["editcount"] == 0:
        desc = ":warning: This user has never been in PvZCC."
    else:
        is_pvzccer = True
        if is_blocked: desc = ":no_entry: This user is blocked in PvZCC."
             
    # Base of the embed response
    embed = discord.Embed(
            description = f"{desc}",
            title = username.replace("_", " ")
            )
    
    # Constructing the response body
    if is_pvzccer:
    
        jf = call_and_get_firstedit_json(username)
        contrib = jf["query"]["usercontribs"][0]
        
        jl = call_and_get_lastedit_json(username)
        final_contrib = jl["query"]["usercontribs"][0]
        
        # Blocked info
        if is_blocked:
            formatted_blocked_until = ":skull: *The end of time* :skull:"
            if user_info["blockexpiry"] != "infinite":
                parsed_blocked_until = datetime.strptime(user_info["blockexpiry"], "%Y-%m-%dT%H:%M:%SZ")
                formatted_blocked_until = parsed_blocked_until.strftime("%B %d, %Y")
            embed.add_field(name="Block expiry",value=formatted_blocked_until, inline = False)
            

        # Edit count
        edit_count = user_info["editcount"]
        embed.add_field(name="Edit count",value=edit_count, inline = False)
        
        # User group
        groups = user_info["groups"]
        group_name = gp.group_name(gp.highest_group(groups))
        embed.add_field(name="Group",value=group_name, inline = False)
        
        # Join date
        parsed_join_date = datetime.strptime(contrib["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
        formatted_join_date = parsed_join_date.strftime("%B %d, %Y")
        embed.add_field(name="First edit",value=formatted_join_date)
        
        # Most recent edit
        parsed_final_date = datetime.strptime(final_contrib["timestamp"], "%Y-%m-%dT%H:%M:%SZ")
        final_time_difference = datetime.now() - parsed_final_date
        embed.add_field(name="Most recent edit",value=time_diff_to_string(final_time_difference))
        
        #parsed_reg_date = datetime.strptime(user_info["registration"], "%Y-%m-%dT%H:%M:%SZ")
        #formatted_reg_date = parsed_reg_date.strftime("%B %d, %Y")

    return embed
                                      
    
    
    


    