from utils.filecraw import main as filecraw
from utils.urlcraw import craw as urlcraw
from utils.count import count
from utils.merged import merged

# 1. Use url to get words
# urlcraw("https://www.baidu.com")
# filecraw("links.txt")

# 2. Merge all txt in the "output" directory
# merged()

# 3. Count the number of words
# count('merged.txt')