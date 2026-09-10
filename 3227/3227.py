"""ไพ่ 44 ใบ"""
card = input().strip().lower()
rank_code = card[:-1]
suit_code = card[-1]
rank_dict = {
    "a": "ace",
    "j": "jack",
    "q": "queen",
    "k": "king"
}
suit_dict = {
    "d": "diamonds",
    "h": "hearts",
    "s": "spades",
    "c": "clubs"
}
rank_name = rank_dict.get(rank_code, rank_code)
suit_name = suit_dict[suit_code]
print(f"{rank_name} of {suit_name}")
