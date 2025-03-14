import re

# Load the M3U file
with open("oppu.m3u", "r", encoding="utf-8") as file:
    content = file.read()

# Define the pattern for real .m3u8 links (Modify as per actual link structure)
pattern = r"https://freelivtvoppuback.vercel.app/vishwas.m3u8?id=388817&token=freelivtv"

# Replace with Vercel URLs dynamically
new_content = re.sub(pattern, lambda m: f"https://9xp.vercel.app/{m.group().split('=')[-1]}.m3u8", content)

# Save the modified file
with open("tv_channels_modified.m3u", "w", encoding="utf-8") as file:
    file.write(new_content)

print("✅ Replacement complete! New file saved as 'oppu.m3u'")
