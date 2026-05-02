

data = [
    {'name': 'Jenny\'s Lectures', 'follower_count': 1, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Cristiano Ronaldo', 'follower_count': 600, 'description': 'Footballer', 'country': 'Portugal'},
    {'name': 'Narendra Modi', 'follower_count': 90, 'description': 'Prime Minister', 'country': 'India'},
    {'name': 'Fit Tuber', 'follower_count': 7, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Virat Kohli', 'follower_count': 270, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Lionel Messi', 'follower_count': 500, 'description': 'Footballer', 'country': 'Argentina'},
    {'name': 'Selena Gomez', 'follower_count': 430, 'description': 'Singer', 'country': 'USA'},
    {'name': 'Dwayne Johnson', 'follower_count': 390, 'description': 'Actor', 'country': 'USA'},
    {'name': 'Kylie Jenner', 'follower_count': 400, 'description': 'Influencer', 'country': 'USA'},
    {'name': 'Alia Bhatt', 'follower_count': 85, 'description': 'Actress', 'country': 'India'},
    {'name': 'Shah Rukh Khan', 'follower_count': 45, 'description': 'Actor', 'country': 'India'},
    {'name': 'Taylor Swift', 'follower_count': 280, 'description': 'Singer', 'country': 'USA'},
    {'name': 'Bill Gates', 'follower_count': 65, 'description': 'Entrepreneur', 'country': 'USA'},
    {'name': 'Elon Musk', 'follower_count': 200, 'description': 'Entrepreneur', 'country': 'USA'},
    {'name': 'Mark Zuckerberg', 'follower_count': 35, 'description': 'Entrepreneur', 'country': 'USA'},
    {'name': 'Priyanka Chopra', 'follower_count': 90, 'description': 'Actress', 'country': 'India'},
    {'name': 'Deepika Padukone', 'follower_count': 80, 'description': 'Actress', 'country': 'India'},
    {'name': 'Justin Bieber', 'follower_count': 290, 'description': 'Singer', 'country': 'Canada'},
    {'name': 'Beyonce', 'follower_count': 310, 'description': 'Singer', 'country': 'USA'},
    {'name': 'Drake', 'follower_count': 150, 'description': 'Rapper', 'country': 'Canada'},
    {'name': 'Ariana Grande', 'follower_count': 370, 'description': 'Singer', 'country': 'USA'},
    {'name': 'Kim Kardashian', 'follower_count': 360, 'description': 'Influencer', 'country': 'USA'},
    {'name': 'Zendaya', 'follower_count': 180, 'description': 'Actress', 'country': 'USA'},
    {'name': 'Tom Holland', 'follower_count': 70, 'description': 'Actor', 'country': 'UK'},
    {'name': 'Chris Hemsworth', 'follower_count': 95, 'description': 'Actor', 'country': 'Australia'},
    {'name': 'Ranveer Singh', 'follower_count': 50, 'description': 'Actor', 'country': 'India'},
    {'name': 'Akshay Kumar', 'follower_count': 65, 'description': 'Actor', 'country': 'India'},
    {'name': 'MS Dhoni', 'follower_count': 45, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Rohit Sharma', 'follower_count': 35, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'Hardik Pandya', 'follower_count': 30, 'description': 'Cricketer', 'country': 'India'},
    {'name': 'MrBeast', 'follower_count': 320, 'description': 'YouTuber', 'country': 'USA'},
    {'name': 'PewDiePie', 'follower_count': 110, 'description': 'YouTuber', 'country': 'Sweden'},
    {'name': 'CarryMinati', 'follower_count': 40, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'BB Ki Vines', 'follower_count': 26, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Ashish Chanchlani', 'follower_count': 30, 'description': 'YouTuber', 'country': 'India'},
    {'name': 'Sandeep Maheshwari', 'follower_count': 28, 'description': 'Motivational Speaker', 'country': 'India'},
    {'name': 'Gary Vaynerchuk', 'follower_count': 10, 'description': 'Entrepreneur', 'country': 'USA'},
    {'name': 'Logan Paul', 'follower_count': 25, 'description': 'YouTuber', 'country': 'USA'},
    {'name': 'Jake Paul', 'follower_count': 20, 'description': 'YouTuber', 'country': 'USA'},
    {'name': 'Emma Watson', 'follower_count': 70, 'description': 'Actress', 'country': 'UK'},
    {'name': 'Daniel Radcliffe', 'follower_count': 15, 'description': 'Actor', 'country': 'UK'},
    {'name': 'Robert Downey Jr.', 'follower_count': 60, 'description': 'Actor', 'country': 'USA'},
    {'name': 'Scarlett Johansson', 'follower_count': 40, 'description': 'Actress', 'country': 'USA'},
    {'name': 'Chris Evans', 'follower_count': 25, 'description': 'Actor', 'country': 'USA'},
    {'name': 'Gal Gadot', 'follower_count': 100, 'description': 'Actress', 'country': 'Israel'},
    {'name': 'Henry Cavill', 'follower_count': 30, 'description': 'Actor', 'country': 'UK'},
    {'name': 'Keanu Reeves', 'follower_count': 20, 'description': 'Actor', 'country': 'Canada'},
    {'name': 'Will Smith', 'follower_count': 65, 'description': 'Actor', 'country': 'USA'},
    {'name': 'Jackie Chan', 'follower_count': 35, 'description': 'Actor', 'country': 'China'},
    {'name': 'Bruce Lee', 'follower_count': 10, 'description': 'Martial Artist', 'country': 'USA'}
]


game_text = ''' _   _   _           _                   
| | | | (_)   __ _  | |__     ___   _ __ 
| |_| | | |  / _` | | '_ \   / _ \ | '__|
|  _  | | | | (_| | | | | | |  __/ | |   
|_| |_| |_|  \__, | |_| |_|  \___| |_|   
| |       ___|___/      __   ___   _ __  
| |      / _ \  \ \ /\ / /  / _ \ | '__| 
| |___  | (_) |  \ V  V /  |  __/ | |    
|_____|  \___/    \_/\_/    \___| |_|    '''



vs_text = '''__     __  ____  
\ \   / / / ___| 
 \ \ / /  \___ \ 
  \ V /    ___) |
   \_/    |____/ '''

