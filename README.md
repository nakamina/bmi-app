# BMI 計算くん🐶

身長(cm)と体重(kg)からBMIを計算するコマンドラインアプリケーション

## 環境構築

- pyenvとpyenv-virtualenvを使用します

```shell!
cd /path/to/bmi-app
pyenv virtualenv 3.9.9 bmi-app
pyenv local bmi-app

pip install -U pip setuptools wheel poetry
```
- poetryを使用して依存ライブラリをインストールします

```shell
poetry install
```

## 動かし方
```shell
🐱❯ bmi-app --help
Usage: bmi-app [OPTIONS]

Options:
  --height INTEGER  身長(cm)  [required]
  --weight INTEGER  体重(kg)  [required]
  --help            Show this message and exit.
```

### 身長(cm)と体重(kg)を入力する

```shell
🐱❯ bmi-app --height 200 --weight 100
あなたのBMI値は25.0です
あなたの適正体重は88.0kgです
```