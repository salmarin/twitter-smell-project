
import Scweet
import pandas as pd
frames=[]
datasbis=[]
# scrape top tweets with the words 'covid','covid19' in proximity and without replies.
# the process is slower as the interval is smaller (choose an interval that can divide the period of time betwee, start and max date)
for word in ["Stink","Scent","Smell","Odour","Odor","Stench","Reek","Aroma","Aromatic","Whiff","Foetor","Fetor","Fragrance","Musk","Rankness","Redolence","Pong","Pungency","Niff","Deodorant","Essence","Atmosphere","Olfaction",
                               "Stinking","Stank","Stunk","Scented","Odourless","Odoriferous","Odorous","Malodorous","Reeking","Aromatic","Whiffy","Fetid","Foetid","Fragrant","Fragranced","Redolent","Frowzy","Frowsy","Pungent","Funky","Musty","Niffy","Unscented","Scentless","Deodorized","Noisome","Smelly","Mepehitic","Muddle","Putrid","Olfactory","Musky","Pungently",
                               "Smelling","Smelled","Reeked","Sniff","Sniffed","Sniffing","Whiffed","Deodorized","Deodorizing","Snuffing","Snuffed"]:    
    
    framesbis=[]
    for k in range(1,26):
    
        data = Scweet.scrap(words=[word], start_date="2021-03-"+str(k), max_date="2021-03-"+str(k+1), from_account = None, interval=1, 
          headless=True, display_type="Top", save_images=False, 
                 resume=False, filter_replies=True, proximity=False)
        frames.append(data)
        framesbis.append(data)
        data.to_excel("tweets of "+word+ " from march"+str(k)+".xlsx")
    datasbis.append(pd.concat(framesbis, sort=False))        
        
datas=pd.concat(frames, sort=False)

datas.to_csv("tweets-test.csv")
frames.to_csv("tweetsby_day_word.csv")
    