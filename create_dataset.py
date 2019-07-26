import ImagePreprocess as image_preprocess


def main():
    # Number of images to create
    N = 1000
    preprocess = image_preprocess.ImagePreprocess()

    for n in range(375, N):
        preprocess.create_image_and_save(n)
        print(n)


main()
