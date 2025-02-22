from django.db import models


class Card(models.Model):
    VALUES = {
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King',
        'A': 'Ace'
    }

    SUITS = {
        'H': 'Hearts',
        'D': 'Diamonds',
        'C': 'Clubs',
        'S': 'Spades'
    }

    value = models.CharField(max_length=5, choices=VALUES)
    suit = models.CharField(max_length=10, choices=SUITS)
    image = models.ImageField(upload_to='card_images/')

    def get_full_value(self):
        return self.VALUES.get(self.value, self.value)
    
    def __str__(self):
        return f'{self.get_full_value()} of {self.get_suit_display()}'