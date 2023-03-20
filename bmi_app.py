# BMI計算アプリケーション
def calculate_bmi(height, weight):
    # 身長と体重からBMIを計算する関数
    height_m = height / 100
    bmi = weight / height_m**2
    return bmi


def calculate_proper_weight(height):
    # 身長から適正体重を計算する関数
    height_m = height / 100
    proper_weight = (height_m**2) * 22
    return proper_weight


if __name__ == "__main__":
    # 身長と体重を入力する

    while True:
        height_str = input("身長(cm)を入力してください:")
        try:
            height = float(height_str)
        except ValueError:
            print("正しい入力ではありません。再度入力してください")
            continue

        if height > 0:
            break
        print("正しい入力ではありません。再度力してください")

    while True:
        weight_str = input("体重(kg)を入力してください:")
        try:
            weight = float(weight_str)
        except ValueError:
            print("正しい入力ではありません。再度入力してください")
            continue

        if weight > 0:
            break
        print("正しい入力ではありません。再度力してください")

    # BMIと適正体重を計算する
    bmi = calculate_bmi(height, weight)
    proper_weight = calculate_proper_weight(height)

    # 結果を表示する
    print("あなたのBMI値は{:.1f}です".format(bmi))
    print("あなたの適正体重は{:.1f}kgです".format(proper_weight))
