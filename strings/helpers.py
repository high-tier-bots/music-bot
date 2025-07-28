HELP_1 = """
<b><u>Admin Commands :</b></u>
To use these commands for a channel, simply add <b>C</b> at the beginning of the command (e.g., /cpause).

<b> /pause </b>:Pause the currently playing stream.

<b> /resume </b>:Resume the paused stream.

<b> /skip </b>:Skip the current track and start playing the next one in the queue.

<b> /end or /stop </b>:Clear the queue and stop the current stream.

<b> /player </b>:Get an interactive player control panel.

<b> /queue </b>:View the list of queued tracks.
"""

HELP_2 = """
<b><u>Auth Users :</b></u>
Authorized users can access bot admin features without being group admins.

/auth [username/< > user_i</>d] :Add a user to the bot’s authorized user list.

/unauth [username/< > user_i</>d] :Remove a user from the authorized user list.

<b> /authusers </b>:Display the list of authorized users in the group.
"""

HELP_3 = """
<u><b>Broadcast Feature</b></u> [Only For Sudoers] :

/broadcast [message or reply to a message] – Send a broadcast message to all chats served by the bot.

<u>Broadcasting Modes :</u>

<b> -pin </b>:Pins your broadcasted message in all served chats.

<b> -pinloud </b>:Pins the message and notifies members in served chats.

<b> -user </b>:Broadcasts the message directly to users who have started the bot.

<b> -assistant </b>:Sends the broadcast message using the assistant account of the bot.

<b> -nobot </b>:Prevents the bot from broadcasting the message (forces only assistant/user to send).

<b>Example:</b> <code>/broadcast -user -assistant -pin Testing broadcast</code>
"""

HELP_4 = """
<u><b>Chat Blacklist Feature :</b></u> (Only for Sudo Users)

Restrict unwanted or abusive chats from using your bot.

/blacklistchat [chat_id] – Blacklist a chat from accessing the bot.

/whitelistchat [chat_id] – Remove a chat from the blacklist and allow access again.

/blacklistedchat – Display the list of all blacklisted chats.
"""

HELP_5 = """
<u><b>Block Users :</b></u> (Only for Sudo Users)

Prevent specific users from interacting with the bot commands by blocking them.

/block [username or reply to a user] – Block the user from using the bot.

/unblock [username or reply to a user] – Unblock the previously blocked user.

/blockedusers – Show the list of all blocked users.
"""

HELP_6 = """ 
<u><b>Channel Play Commands :</b></u>

Stream audio or video directly in a connected channel's video chat using the following commands:

/cplay – Start streaming the requested audio track in the channel's video chat.

/cvplay – Start streaming the requested video track in the channel's video chat.

/cplayforce or /cvplayforce – Force-stop the current stream and immediately start the new requested track.

/channelplay [chat username or ID] or disable – Link a channel to your group to control streaming using group commands, or disable the connection.
"""

HELP_7 = """
<u><b>Global Ban Feature</b></u> (Only for Sudo Users)

Use global ban to restrict problematic users across all chats served by the bot.

/gban [username or reply to a user] – Globally ban the user from all served chats and block their access to bot commands.

/ungban [username or reply to a user] – Remove the global ban from a user and restore access.

/gbannedusers – Display the list of all globally banned users.
"""

HELP_8 = """
<u><>Loop Stream :</></u>

Start streaming the currently playing track on loop mode.

/loop enable or disable – Enable or disable loop for the current stream.

/loop [1, 2, 3, ...] – Set the loop count to repeat the stream a specific number of times.
"""

HELP_9 = """
<u><b>Maintenance Mode</b></u> (Only for Sudo Users)

Manage your bot’s backend operations and maintenance activities.

/logs – Retrieve the latest logs of the bot.

/logger [enable/disable] – Enable or disable activity logging for the bot.

/maintenance [enable/disable] – Turn maintenance mode on or off for your bot.
"""

HELP_10 = """
<u><b>Ping & Stats :</b></u>

Basic commands to check bot status and performance.

/start – Start the music bot.

/help – Display the help menu with a full explanation of available commands.

/ping – Show the bot’s response time and system statistics.

/stats – View overall usage statistics of the bot.
"""

HELP_11 = """
<u><b>Play Commands :</b></u>

Use these commands to play or force-play audio/video tracks in the group’s video chat.

<b>v – Refers to video play.</b>

force – Refers to force play (immediately stops current stream and plays the new one).

/play or /vplay – Start streaming the requested audio or video track.

/playforce or /vplayforce – Force-stop the current stream and start the requested track instantly.
"""

HELP_12 = """
<u><b>Shuffle Queue :</b></u>

Manage the play queue in a fun, randomized way.

/shuffle – Shuffle the order of tracks in the queue.

/queue – Show the newly shuffled queue list.
"""

HELP_13 = """
<u><b>Seek Stream :</b></u>

Use these commands to move forward or backward within the currently playing stream.

/seek [duration in seconds] – Jump forward to the specified timestamp in the stream.

/seekback [duration in seconds] – Rewind the stream by the given number of seconds.
"""

HELP_14 = """
<u><b>Song Download</b></u>

/song [song name / YouTube URL] – Download any track from YouTube in MP3 or MP4 format.
"""

HELP_15 = """
<u><b>Speed Commands</b></u>

Control the playback speed of the current stream. (Admins only)

/speed or /playback – Adjust the audio playback speed in groups.

/cspeed or /cplayback – Adjust the audio playback speed in channels.
"""

HELP_16 = """
<u><b>Privacy Command</b></u>

/Privacy – View the privacy policy of the Music Bot.
"""
