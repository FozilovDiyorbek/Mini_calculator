import logging


logging.basicConfig(
    filename="calc.log",        # log fayl
    level=logging.INFO,         
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def add(a: float, b: float) -> float:
    result = a + b
    logging.info(f"Qo'shish: {a} + {b} = {result}")
    return result

def subtract(a: float, b: float) -> float:
    result = a - b
    logging.info(f"Ayirish: {a} - {b} = {result}")
    return result

def multiply(a: float, b: float) -> float:
    result = a * b
    logging.info(f"Ko'paytirish: {a} * {b} = {result}")
    return result

def divide(a: float, b: float) -> float:
    try:
        result = a / b
        logging.info(f"Bo'lish: {a} / {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("0 ga bo'lish xatosi!")
        return None


def calculator():
    print("🧮 Mini Calculator")
    print("Amallar: +  -  *  /   |   chiqish uchun: exit")

    while True:
        cmd = input("\nAmalni kiriting: ").strip()
        if cmd.lower() == "exit":
            print("Chiqildi.")
            logging.info("Kalkulyator yopildi.")
            break

        try:
            a = float(input("Birinchi son: "))
            b = float(input("Ikkinchi son: "))

            if cmd == "+":
                print("Natija:", add(a, b))
            elif cmd == "-":
                print("Natija:", subtract(a, b))
            elif cmd == "*":
                print("Natija:", multiply(a, b))
            elif cmd == "/":
                res = divide(a, b)
                if res is not None:
                    print("Natija:", res)
                else:
                    print("❌ 0 ga bo'lish mumkin emas!")
            else:
                print("❌ Noto'g'ri amal!")
                logging.warning(f"Noto'g'ri amal: {cmd}")

        except ValueError:
            print("❌ Noto'g'ri son kiritildi!")
            logging.error("Son o'rniga matn kiritildi.")


if __name__ == "__main__":
    calculator()
