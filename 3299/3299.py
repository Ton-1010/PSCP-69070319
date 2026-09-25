"""แปลงดอกไม้"""
def main():
    """ฟังก์ชันคำนวณแถบสุดท้ายที่ปลูกดอกไม้"""
    l, n = map(int, input().split())
    k = 1
    while (l * k * (l * k + 1)) // 2 < n:
        k += 1
    print(k)
main()
