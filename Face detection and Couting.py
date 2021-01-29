import cv2
import numpy as np
import matplotlib.pyplot as plt
class FinalProject():
    def __init__(self,image):
        self.image = image
    def BinaryImage(self):
        RGB = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)  # convert RGB color to HSV
        RGB = cv2.inRange(RGB, (0, 5, 80), (20, 255, 255))  # detect skin on the range of lower and upper pixel values
        blurred = cv2.medianBlur(RGB, 5)  # use median filter
        ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)  # convert to binary using threshold method
        return thresh
    def morphologicalTransformation(self):
        kernel = np.ones((8, 8), np.uint8)  # kernel size
        img_close = cv2.morphologyEx(self.BinaryImage(), cv2.MORPH_CLOSE, kernel, iterations=5)  # closing morphological
        img_open = cv2.morphologyEx(img_close, cv2.MORPH_OPEN, kernel, iterations=5)  # opening morphological
        new_image = cv2.medianBlur(img_open, 7)  # clean all noise after closing and opening
        return new_image
    def morphologicaltransformation(self):
        kernel = np.ones((7, 7), np.uint8)
        img_close = cv2.morphologyEx(self.BinaryImage(), cv2.MORPH_CLOSE, kernel, iterations=1)
        kernel1 = np.ones((4, 4), np.uint8)
        img_erode = cv2.erode(img_close, kernel1)
        # clean all noise after dilatation and erosion
        img_open = cv2.morphologyEx(img_erode, cv2.MORPH_OPEN, kernel1, iterations=2)
        img_close = cv2.morphologyEx(img_open, cv2.MORPH_CLOSE, kernel1, iterations=1)
        new_image = cv2.medianBlur(img_close, 7)
        return new_image
    def labelandCountingFaces(self):
        img_erode = self.morphologicalTransformation()
        ret, labels = cv2.connectedComponents(img_erode)  # Map component labels to HUV values
        label_hue = np.uint8(179 * labels / np.max(labels))
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)  # convert HUV to RGB for display
        labeled_img[label_hue == 0] = 0  # set background label to black
        plt.title('Face counted:' + str(ret - 1))
        plt.imshow(labeled_img)
        print('objects number is:', ret - 1)
        plt.show()
    def label1andCountingFaces(self):
        img_erode = self.morphologicaltransformation()
        ret, labels = cv2.connectedComponents(img_erode)  # Map component labels to HUV values
        label_hue = np.uint8(179 * labels / np.max(labels))
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)  # convert HUV to RGB for display
        labeled_img[label_hue == 0] = 0  # set background label to black
        plt.title('Face counted:' + str(ret - 1))
        plt.imshow(labeled_img)
        print('objects number is:', ret - 1)
        plt.show()
if __name__ == '__main__':
    def validate_option(message):
        while True:
            try:
                choice = int(input(message))
                print('-----------------------------')
            except ValueError:
                print("Invalid input! It must be a number (1-5). Please try again!")
            else:
                if choice < 1 or choice > 5:
                    print("Invalid input! It must be a number (1-5). Please try again!")
                else:
                    return choice

    def process_option(choice):
        if choice == 1:
            image = cv2.imread("figure 1.jpg")
            FinalProject(image).labelandCountingFaces()
            return 1
        elif choice == 2:
            image = cv2.imread("figure 2.png")
            FinalProject(image).label1andCountingFaces()
            return 1
        elif choice == 3:
            image = cv2.imread("figure 3.jpg")
            FinalProject(image).labelandCountingFaces()
            return 1
        elif choice == 4:
            image = cv2.imread("figure 4.jpg")
            FinalProject(image).labelandCountingFaces()
            return 1
        else:
            return 0

    is_continue = 1
    while is_continue:
        print('Hello, please select a number (1-5) to count number of faces')
        print('*******************************')
        print('Please remember to close the image, and retype a different number(1-5) to see the result of another figure')
        print('------------------------------')
        print("Menu option:")
        print("1.Figure 1")
        print("2.Figure 2")
        print("3.Figure 3")
        print("4.Figure 4")
        print("5.Quit")
        print('------------------------------')
        choice = validate_option("Enter your choice: ")
        is_continue = process_option(choice)


