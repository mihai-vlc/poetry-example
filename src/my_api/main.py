from my_api.transform_string import transform


def run():
    print("welcome to my app", __name__)
    text = input("text = ")
    print(transform(text))


if __name__ == "__main__":
    run()
