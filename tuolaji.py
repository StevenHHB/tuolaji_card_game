import random

user_input = input("Press Enter to continue: ")

# Function to safely draw a card or use the last card without removing it


def safe_draw(deck):
    if len(deck) > 1:
        return deck.pop(0)  # Remove and return the first card
    elif len(deck) == 1:
        pop = deck[0]
        deck.clear()
        return pop  # Return the first card without removing
    else:
        return None


def play():
    if user_input == "":
        # Numbering and gaming logic goes here
        numbers = list(range(1, 14))
        deck = numbers * 4
        random.shuffle(deck)
        print(len(deck))
        player1 = deck[:20]
        player2 = deck[20:40]
        starting_cards = deck[40:]
        print(len(starting_cards))
        game_array = []
        drawing_player = 1

        while True:
            # 如果谁的牌没了就输了
            if not player1 or not player2:
                winning_player = 1 if len(player1) > len(player2) else 2
                print(f"We have a winner!{winning_player} is the winner!")
                break
            # 如果两个人都有牌
            else:
                # 如果游戏里没有牌
                if not game_array:
                    # 如果牌堆里也没有牌
                    if not starting_cards:
                        if drawing_player == 1:
                            drawn_card = safe_draw(player1)
                        elif drawing_player == 2:
                            drawn_card = safe_draw(player2)
                        game_array.append(drawn_card)
                        print("Starting card:", drawn_card)
                    # 如果牌堆里有牌
                    else:
                        drawn_card = safe_draw(starting_cards)
                        game_array.append(drawn_card)
                        print("Starting card:", drawn_card)
                # 如果游戏里有牌
                else:
                    # 用户1抽牌
                    # 用户1对比现有的牌
                    # 如果有一样的牌，用户1抽走牌
                    # drawing player还是用户1
                    # 用户1把牌加到game array里
                    # drawying player
                    if drawing_player == 1:
                        drawn_card = safe_draw(player1)
                        print("Game Array", game_array)
                        print("Player 1's turn. Card:", drawn_card)
                        if drawn_card in game_array:
                            game_array.append(drawn_card)
                            first = game_array.index(drawn_card)
                            last = len(game_array) - 1 - \
                                game_array[::-1].index(drawn_card)
                            won_array = game_array[first:last + 1]
                            player1.extend(won_array)
                            game_array = game_array[:first] + \
                                game_array[last + 1:]
                            drawing_player = 1
                            print("Player 1's won this session")
                            print("Player 1's cards:", len(player1),
                                  'Player 2\'s cards:', len(player2))
                        else:
                            game_array.append(drawn_card)
                            drawing_player = 2
                    if drawing_player == 2:
                        drawn_card = safe_draw(player2)
                        print("Game Array", game_array)
                        print("Player 2's turn. Card:", drawn_card)
                        if drawn_card in game_array:
                            game_array.append(drawn_card)
                            first = game_array.index(drawn_card)
                            last = len(game_array) - 1 - \
                                game_array[::-1].index(drawn_card)
                            won_array = game_array[first:last + 1]
                            player2.extend(won_array)
                            game_array = game_array[:first] + \
                                game_array[last + 1:]
                            drawing_player = 2
                            print("Player 2's won this session")
                            print("Player 1's cards:", len(player1),
                                  'Player 2\'s cards:', len(player2))
                        else:
                            game_array.append(drawn_card)
                            drawing_player = 1


play()