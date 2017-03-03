import discord
from .utils import checks
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from __main__ import send_cmd_help
import os

#I like trains
class Customhelp:
    """Allows you to set your own server on_join message!"""
    
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command("help")
        self.weeee = "data/customhelp/settings.json"
        self.tony = dataIO.load_json(self.weeee)
    
    @checks.is_owner()
    @commands.group(pass_context=True)
    async def sethelp(self, ctx):
        """Custom Help allows you to create your very own help message for your own Red-DiscordBot"""

        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
    
    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def embedtoggle(self, ctx):
        """Turn on or off the ability to make the help mesaged embed"""
        
        if self.tony["embedToggle"] is False:
            self.tony["embedToggle"] = True
            dataIO.save_json(self.weeee, self.tony)
            await self.bot.say("The embed have been turned on!")
        else:
            self.tony["embedToggle"] = False
            dataIO.save_json(self.weeee, self.tony)
            await self.bot.say("The embed have been turned off!")
    
    @checks.is_owner()
    @sethelp.command(pass_context=True)
    async def privateset(self, ctx):
        """Turn on or off the ability to make help messages in direct message."""
        
        if self.tony["helpPrivate"] is False:
            self.tony["helpPrivate"] = True
            dataIO.save_json(self.weeee, self.tony)
            await self.bot.say("The help message will be now sent to direct message!")
        else:
            self.tony["helpPrivate"] = False
            dataIO.save_json(self.weeee, self.tony)
            await self.bot.say("The help message will not be set within the channel it has been said in??!")
          


def check_folders():
    if not os.path.exists("data/customhelp"):
        print("Creating the on_join folder, so be patient...")
        os.makedirs("data/customhelp")
        print("Finish!")

def check_files():
    twentysix = "data/customhelp/wow.json"
    json = {
        "helpMessage" : "Meep",
        "helpPrivate" : False,
        "embedColor" : "0xFFFFFF",
        "embedFooter" : "This is your footer!",
        "embedToggle" : False,
        "embedTitle" : "This is your title!",
        "messageTitle" : "Welcome to {0.name}!"
    }

    if not dataIO.is_valid_json(twentysix):
        print("Derp Derp Derp...")
        dataIO.save_json(twentysix, json)
        print("Created settings.json!")

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Customhelp(bot))