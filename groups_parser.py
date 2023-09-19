translation_dict = {
"sysop" : "Administrator",
"wiki-representative" : "Wiki Representative",
"content-moderator" : "Content Moderator",
"bureaucrat" : "Bureaucrat",
"bot" : "Bot"
}

order = ["bot", "wiki-representative", "bureaucrat", "sysop", "content-moderator"]

# Returns the normal readable group name based on the group code from the API
def group_name(group_code):
    if group_code in translation_dict:
        return translation_dict[group_code]
    else:
        return None

# Returns the group code with the highest power from the list of groups
def highest_group(groups):
    for group in order:
        if group in groups: return group
    
    