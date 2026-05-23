import discord
from discord.ext import commands
import os
import hashlib
import aiohttp

# Initialize bot with required intents to read message content and attachments
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# High-risk executable extensions to intercept
DANGEROUS_EXTENSIONS = ['.exe', '.bat', '.scr', '.vbs', '.msi', '.jar', '.cmd']

@bot.event
async def on_ready():
    print(f"🛡️ Cyber-Security Bot is online as {bot.user}")

@bot.event
async def on_message(message):
    # Prevent the bot from scanning its own messages
    if message.author == bot.user:
        return

    # Check if the message contains any file attachments
    if message.attachments:
        for attachment in message.attachments:
            # Extract the file extension and convert to lowercase
            file_extension = os.path.splitext(attachment.filename)[1].lower()
            
            if file_extension in DANGEROUS_EXTENSIONS:
                print(f"🚨 Intercepted potentially dangerous file: {attachment.filename}")
                
                # 1. Immediately notify the channel with a clean embed
                embed = discord.Embed(
                    title="⚠️ High-Risk File Intercepted",
                    description=f"User {message.author.mention} uploaded an executable file type (`{file_extension}`).",
                    color=discord.Color.orange()
                )
                embed.add_field(name="File Name", value=attachment.filename, inline=False)
                embed.set_footer(text="Analyzing file hash via VirusTotal...")
                
                alert_msg = await message.channel.send(embed=embed)
                
                # ---- PHASE 2: CALCULATE SHA-256 HASH IN MEMORY ----
                try:
                    # Read the attachment file directly into memory as bytes
                    file_bytes = await attachment.read()
                    
                    # Generate the SHA-256 cryptographic hash of the raw bytes
                    file_hash = hashlib.sha256(file_bytes).hexdigest()
                    print(f"🔑 Generated SHA-256 Fingerprint: {file_hash}")
                    
                    # Update the embed to show the user the file fingerprint
                    embed.add_field(name="File Fingerprint (SHA-256)", value=f"`{file_hash}`", inline=False)
                    await alert_msg.edit(embed=embed)
                    
                    # ---- PHASE 3: VIRUSTOTAL API SCAN ----
                    # Safely pulls the key from your local system environment variables
                    VT_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
                    
                    if not VT_API_KEY:
                        print("❌ Error: VIRUSTOTAL_API_KEY environment variable is not set.")
                        embed.set_footer(text="Configuration error: Missing API Key.")
                        await alert_msg.edit(embed=embed)
                        continue

                    vt_url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
                    headers = {
                        "x-apikey": VT_API_KEY
                    }
                    
                    async with aiohttp.ClientSession() as session:
                        async with session.get(vt_url, headers=headers) as response:
                            
                            if response.status == 200:
                                data = await response.json()
                                stats = data['data']['attributes']['last_analysis_stats']
                                malicious_count = stats['malicious']
                                total_engines = sum(stats.values())
                                
                                if malicious_count > 0:
                                    embed.title = "❌ MALICIOUS FILE DETECTED"
                                    embed.color = discord.Color.red()
                                    embed.description = f"🚨 WARNING! {message.author.mention}, this file has been flagged as **malicious**."
                                    embed.add_field(name="Detections", value=f"⚠️ `{malicious_count}` / `{total_engines}` engines flagged this file.", inline=True)
                                    embed.set_footer(text="Recommendation: DO NOT download or execute this file.")
                                else:
                                    embed.title = "✅ File Verified Clean"
                                    embed.color = discord.Color.green()
                                    embed.add_field(name="Detections", value="🟢 `0` engines flagged this file.", inline=True)
                                    embed.set_footer(text="Scan complete via VirusTotal.")
                                
                                await alert_msg.edit(embed=embed)
                            
                            elif response.status == 404:
                                embed.title = "❓ Unknown File Signature"
                                embed.color = discord.Color.blue()
                                embed.add_field(name="Status", value="This file hash is not in the global database.", inline=False)
                                embed.set_footer(text="Hash not found on VirusTotal.")
                                await alert_msg.edit(embed=embed)
                                
                except Exception as e:
                    print(f"❌ Error during file processing: {e}")
                    embed.set_footer(text="Failed to complete security scan.")
                    await alert_msg.edit(embed=embed)

    # Ensure regular bot commands still work alongside on_message
    await bot.process_commands(message)

# Run the bot using your secure environment variable token
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if DISCORD_TOKEN:
    bot.run(DISCORD_TOKEN)
else:
    print("❌ Error: DISCORD_BOT_TOKEN environment variable is not set.")
