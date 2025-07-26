def get_celebrity_suggestion(shape, gender, age):
    male_celebrities = {
        'Oval': ['Zayn Malik', 'Brad Pitt'],
        'Round': ['Chris Pratt', 'Jonah Hill'],
        'Square': ['Henry Cavill', 'David Beckham'],
        'Diamond': ['Johnny Depp', 'Harry Styles'],
        'Heart': ['Leonardo DiCaprio', 'Ryan Gosling']
    }

    female_celebrities = {
        'Oval': ['Emma Watson', 'Zendaya'],
        'Round': ['Selena Gomez', 'Adele'],
        'Square': ['Angelina Jolie', 'Margot Robbie'],
        'Diamond': ['Rihanna', 'Gal Gadot'],
        'Heart': ['Taylor Swift', 'Natalie Portman']
    }

    beard_styles = {
        'Oval': 'Short Boxed Beard',
        'Round': 'Goatee',
        'Square': 'Full Beard',
        'Diamond': 'Balbo',
        'Heart': 'Van Dyke'
    }

    celebs = male_celebrities if gender == 'male' else female_celebrities
    celebrity = celebs.get(shape, ['Unknown'])[age % 2]
    beard = beard_styles.get(shape, 'Clean Shave')
    comment = "🔥 You're about to break the internet!" if gender == 'male' else "💫 Glam Queen Vibes!"

    return celebrity, beard, comment
