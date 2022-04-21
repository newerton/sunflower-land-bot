import cv2

method = cv2.TM_SQDIFF_NORMED
image = cv2.imread("./screenshot.png")
target = cv2.imread("./sunflower.png", cv2.IMREAD_UNCHANGED)


def test():
    result = cv2.matchTemplate(
        image, target[..., :3], method, mask=target[..., 3])

    _, _, mnLoc, _ = cv2.minMaxLoc(result)

    MPx, MPy = mnLoc

    trows, tcols = target.shape[:2]

    cv2.rectangle(image, (MPx, MPy), (MPx+tcols, MPy+trows), (0, 0, 255), 2)
    cv2.imshow('output', image)
    cv2.waitKey(0)


if __name__ == "__main__":
    test()
