from config import ASSISTANT_PREFIX
from Yukki import BOT_NAME, BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = f"""
𝙷𝚎𝚢 MENTION !
😈  I Aᴍ [Dᴀɴɪsʜ Mᴜsɪᴄ Bᴏᴛ](https://t.me/DANISHMUSIC_BOT), A Aᴡᴇsᴏᴍᴇ Mᴜsɪᴄ Bᴏᴛ Wɪᴛʜ Lᴏᴛs Oғ  Fᴇᴀᴛᴜʀᴇs
────────────────────

✪ Bᴏᴛ Fᴏʀ Pʟᴀʏɪɴɢ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Vᴄ Iɴ Bᴏᴛʜ Aᴜᴅɪᴏ Aɴᴅ Vɪᴅᴇᴏ Fᴏʀᴍᴀᴛ..😁❤️

➼ Sᴏ Wʜᴀᴛ Yᴏᴜ Aʀᴇ Wᴀɪᴛɪɴɢ Tᴏ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Bᴀʙʏ..😉

ᴀɴᴅ ᴅᴏɴ'ᴛ ꜰᴏʀɢᴏᴛ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴡɪᴛʜ ᴀʟʟ ʀɪɢʜᴛꜱ..⚡️
─────────────────── 
"""

COMMANDS_TEXT = f"""
✨ **Hello MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="📚 Commands", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔧 Settings", callback_data="settingm"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="⚡️𝙼𝚢 𝙾𝚠𝚗𝚎𝚛⚡️", url="https://t.me/DANISH_BABA"
            ),
            InlineKeyboardButton(
                text="✨ 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝙶𝚛𝚘𝚞𝚙 ✨", url="https://t.me/WEFRIENDSCIRCLE"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="➕ Add me to Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="📚 Commands", callback_data="command_menu"
            ),                       
        ],
        [
            InlineKeyboardButton(
                text="⚡️𝙼𝚢 𝙾𝚠𝚗𝚎𝚛⚡️", url="https://t.me/DANISH_BABA"
            ),
            InlineKeyboardButton(
                text="✨ 𝚂𝚞𝚙𝚙𝚘𝚛𝚝 𝙶𝚛𝚘𝚞𝚙 ✨", url="https://t.me/WEFRIENDSCIRCLE"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Admin Commands", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="Bot Commands", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Play Commands", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="Sudo Commands", callback_data="sudo_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="Extra Commands", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="More Sudo Commands", url="https://telegra.ph/SiestaXMusic-Sudo-Commands-02-08"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
Here is the help for **Admin Commands:**


--**ADMIN ONLY COMMANDS WITH MANAGE VC RIGHT:**--

/pause 
- Pause the playing music on voice chat.

/resume
- Resume the paused music on voice chat.

/skip
- Skip the current playing music on voice chat

/end or /stop
- Stop the playout.


--**Authorised Users List:**--

**{BOT_NAME} has a additional feature for non-admin users who want to use admin commands**
- Auth users can skip, pause, stop, resume Voice Chats even without Admin Rights.


/auth [Username or Reply to a Message] 
- Add a user to AUTH LIST of the group.

/unauth [Username or Reply to a Message] 
- Remove a user from AUTH LIST of the group.

/authusers 
- Check AUTH LIST of the group.
"""

BOT_TEXT = """
Here is the help for **Bot Commands:**


/start 
- Start the Music Bot.

/help 
- Get Commands Helper Menu with detailed explanations of commands.

/settings 
- Get Settings dashboard of a group. You can manage Auth Users Mode. Commands Mode from here.

/ping
- Ping the Bot and check Ram, Cpu etc stats of Music Bot."""

PLAY_TEXT = """
Here is the help for **Play Commands:**


--**Youtube and Telegram Files:**--

/play __[Music Name]__(Bot will search on Youtube)
/play __[Youtube Track link or Playlist]__
/play __[Video, Live, M3U8 Links]__
/play __[Reply to a Audio or Video File]__
- Stream Video or Music on Voice Chat by selecting inline Buttons you get


--**Playlists:**--

/playplaylist 
- Start playing Your Saved Playlist.

/playlist 
- Check Your Saved Playlist On Servers.

/delmyplaylist
- Delete any saved music in your playlist

/delgroupplaylist
- Delete any saved music in your group's playlist [Requires Admin Rights.]
"""

SUDO_TEXT = f"""
Here is the help for **Sudo Commands:**

**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

**<u>BOT COMMANDS:</u>**
/restart - Restart Bot. 
/update - Update Bot.
/stats - Check Bots Stats

**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot

**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast message.
/broadcast_pin [Message or Reply to a Message] - Broadcast message with pin [Disabled Notifications].
/broadcast_pin_loud [Message or Reply to a Message] - Broadcast message with pin [Enabled Notifications].

**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Ban a user globally in Bot's Served Chats and prevents user from using bot commands.
/ungban [Username or Reply to a user] - Remove a user from Bot's GBan List.
"""

EXTRA_TEXT = """
Here is the help for **Extra Commands:**


/lyrics [Music Name]
- Searches Lyrics for the particular Music on web.

/sudolist 
- Check Sudo Users of Music Bot

/song [Track Name] or [YT Link]
- Download any track from youtube in mp3 or mp4 formats via Bot.

/queue
- Check Queue List of Music.
"""

BASIC_TEXT = """
💠 **Basic Commands:**

/start - start the bot
/help - get help message
/play - play songs or videos in vc
/mplay - play songs directly in vc
/vplay - play videos directly in vc
/spotify - play songs from spotify
/resso - play songs from resso
/lyrics - get lyrics of song
/ping - ping the bot
/playlist - play your playlist
/song - download a song as music or video
/settings - settings of the group
/theme - set theme for your group
/queue - get queued song
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="🔍 Basic Commands", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="📚 Advanced Commands", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
