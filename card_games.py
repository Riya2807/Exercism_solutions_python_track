import statistics
def get_rounds(number):
    """
 
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    a=number+1
    b=a+1
    list_rounds=[number,a,b]
    return list_rounds
def concatenate_rounds(rounds_1, rounds_2):
    """
 
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    concatenated_list=rounds_1+rounds_2
    return concatenated_list
    
def list_contains_round(rounds, number):
    """
 
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False
def card_average(hand):
    """
 
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    total=0
    for i in range(len(hand)):
        total+=hand[i]
    avg=total/(len(hand))
    return avg
def approx_average_is_average(hand):
    """
 
    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    strategy_one=(hand[0]+hand[-1])/2
    strategy_two=statistics.median(hand)
    if strategy_one==card_average(hand) or strategy_two==card_average(hand):
        return True
    else:
        return False
def average_even_is_average_odd(hand):
    """
 
    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    sum_even=0
    sum_odd=0
    count_even=0
    count_odd=0
    for i in range(len(hand)):
        if i%2==0:
            sum_even+=hand[i]
            count_even+=1
        else:
            sum_odd+=hand[i]
            count_odd+=1
    avg_even=sum_even/count_even
    avg_odd=sum_odd/count_odd
    if avg_even==avg_odd:
        return True
    else:
        return False
def maybe_double_last(hand):
    """
 
    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    last_card=hand[-1]
    if last_card==11:
        hand[-1]=22
        return hand
    else:
        return hand
