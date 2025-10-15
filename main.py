import cv2
import numpy as np
print("Please choose a photo from the list, Bush.JPG, Bobcat.JPG, Rocks.JPG, Trees.JPG:")
image_path = input("Enter the path to the photo: ")
image = cv2.imread(image_path)
resized_img = cv2.resize(image, (400, 600), interpolation=cv2.INTER_LINEAR)
cv2.imwrite("resized_output.jpg", resized_img)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

color_filter = input("Please choose a type of color filter you like to apply from the list, red, green, blue: ")
if color_filter == "red":
    red_filter = np.zeros_like(resized_img)
    red_filter[:, :, 2] = 100
    filtered_image = cv2.add(resized_img, red_filter)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.imwrite("filtered_output.jpg", filtered_image)
elif color_filter == "green":
    green_filter = np.zeros_like(resized_img)
    green_filter[:, :, 1] = 100
    filtered_image = cv2.add(resized_img, green_filter)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.imwrite("filtered_output.jpg", filtered_image)
elif color_filter == "blue":
    blue_filter = np.zeros_like(resized_img)
    blue_filter[:, :, 0] = 100
    filtered_image = cv2.add(resized_img, blue_filter)
    cv2.imshow("Filtered Image", filtered_image)
    cv2.waitKey(0)
    cv2.imwrite("filtered_output.jpg", filtered_image)
