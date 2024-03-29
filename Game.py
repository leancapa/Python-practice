import random

suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
ranks = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
values = { 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen': 10, 'King': 10, 'Ace': 11 }

playing = True

class Card:

  def __init__ (self, suit, rank): 
    #ATTRIBUTES OF THE CARD OBJECTS
    self.suit = suit
    self.rank = rank
    

  def __str__ (self): 
    #STRING OF THE CARD OBJECTS
    return self.rank + ' of ' + self.suit
  

class Deck:
#CLASS TO CREATE A DECK OF CARD OBJECT
  def __init__(self): 
    
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit, rank))

  def __str__ (self):
    deck_comp = ''
    for card in self.deck:
      deck_comp +=  '\n ' + card.__str__()
      return 'The deck has: ' + deck_comp
  

  def shuffle(self):
    #SHUFFLE THE DECK
    random.shuffle(self.deck)

  def deal(self):
    #DEAL A CARD FROM THE DECK
    single_card = self.deck.pop()
    return single_card
  
class Hand:

  def __init__(self):
    self.cards = [] 
    self.value = 0
    self.aces = 0

  def add_card(self,card):
    self.cards.append(card)
    self.value += values[card.rank]
  
  def adjust_for_ace(self):
    while self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

class Chips:

  def __init__(self):
    self.total = 100
    self.bet = 0

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet


#FUNCTION DECLARATIONS

def take_bet(chips):
  
  while True:
    try:
      chips.bet = int(input("How many chips would you like to bet?"))
    except ValueError:
      print('Sorry, it must be an integer.')

    else:
      if chips.bet > chips.total:
        print('Sorry your bet cannot exceed', chips.total)

      else:
        break
  
def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
  global playing 
  
  while True:
    x = input('Would you like to hit or stand? Enter "h" or "s": ')

    if x[0].lower() == 'h':
      hit(deck,hand)
    
    elif x[0].lower() == 's':
      print('Player stands. dealer is playing.')
      playing = False

    else: print('Sorry, please enter "h" or "s".')
    continue
    break

def show_some(player,dealer):
  print("\n Dealer's hand: ")
  print(" <card hidden>")
  print('', dealer.cards[1])
  print("Player's hand:",*player.cards, sep='\n')

def show_all(player,dealer):
  print("\n Dealer's hand: ", *dealer.cards, sep='\n')
  print("Dealer's hand: ", dealer,values)
  print('\n Player\'s hand: ', *player.cards, sep='\n')
  print("Player's hand:", player.value)

def player_busts(player,dealer,chips):
  print("Player busts. Dealer wins.")
  chips.lose_bet()

def player_wins(player,dealer,chips):
  print("Player wins. Dealer loses.")
  chips.win_bet()

def dealer_busts(player,dealer,chips):
  print("Player busts. Dealer wins.")
  chips.win_bet()

def dealer_wins(player,dealer,chips):
  print("Dealer wins. Player loses.")
  chips.lose_bet()

def push(player,dealer):
  print("Dealer and player tie! It's a push.")



while True:

  print('Wlecome to Blackjack! Get as close to 21 as you can without going over!\n\
  Dealer hits until she reaches 17. Aces count as 1 or 11.')


  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  player_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())


  dealer_hand = Hand()
  dealer_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())


  player_chips = Chips()


  take_bet(player_chips)


  show_some(player_hand, dealer_hand)

  while playing:

    hit_or_stand(deck,player_hand)


    show_some(player_hand, dealer_hand)

    if player_hand.value > 21:
      player_busts(player_hand,dealer_hand,player_chips)
      break
  
  if player_hand.value <= 21:

    while dealer_hand.value < 17:
      hit(deck,dealer_hand)

    show_all(player_hand,dealer_hand)

    if dealer_hand.value > 21:
      dealer_busts(player_hand,dealer_hand,player_chips)
    
    elif dealer_hand.value > player_hand.value:
      dealer_wins(player_hand,dealer_hand,player_chips)

    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand,dealer_hand,player_chips)
    
    else:
      push(player_hand,dealer_hand)

    
  print("\n Player's winnings stand at", player_chips.total)

  new_game = input('Would you like to play again? Enter "y" or "n": ')

  if new_game[0].lower == 'y':
    playing = True
    continue
  else:
    print('Thanks for playing!')
    break














