"""RGB Mixed"""
def main():
    """ฟังก์ชันคำนวณค่าเฉลี่ยสี"""
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())

    ans_r = (r1 + r2) // 2
    ans_g = (g1 + g2) // 2
    ans_b = (b1 + b2) // 2

    print(ans_r, ans_g, ans_b)
main()
