import click


# BMI計算アプリケーション
def calculate_bmi(h: int, w: int) -> float:
    # 身長と体重からBMIを計算する関数
    height_m = h / 100
    bmi = w / height_m**2
    return bmi


def calculate_proper_weight(h: int) -> float:
    # 身長から適正体重を計算する関数
    height_m = h / 100
    proper_weight = (height_m**2) * 22
    return proper_weight


@click.command()
@click.option("--height", type=int, required=True, help="身長(cm)")
@click.option("--weight", type=int, required=True, help="体重(kg)")
def main(height: int, weight: int) -> None:
    # BMIと適正体重を計算する
    bmi = calculate_bmi(height, weight)
    proper_weight = calculate_proper_weight(height)

    # 結果を表示する
    print("あなたのBMI値は{:.1f}です".format(bmi))
    print("あなたの適正体重は{:.1f}kgです".format(proper_weight))
