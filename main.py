# Edge Detection and Filtering using OpenCV

import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_image(image, title="Image"):
    plt.figure(figsize=(8, 8))

    if len(image.shape) == 2:
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    plt.title(title)
    plt.axis("off")
    plt.show()


def Interactive_edge_detection(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not load image.")
        return

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    display_image(gray_image, "Grayscale Image")

    print("\nEDGE DETECTION AND FILTERING")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":

            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)

            sobel_combined = cv2.magnitude(sobelx, sobely)
            sobel_combined = cv2.convertScaleAbs(sobel_combined)

            display_image(sobel_combined, "Sobel Edge Detection")

        elif choice == "2":

            lower_thresh = int(input("Enter lower threshold (default 100): "))
            upper_thresh = int(input("Enter upper threshold (default 200): "))

            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)

            display_image(edges, "Canny Edge Detection")

        elif choice == "3":

            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            laplacian_abs = cv2.convertScaleAbs(laplacian)

            display_image(laplacian_abs, "Laplacian Edge Detection")

        elif choice == "4":

            kernel_size = int(input("Enter Gaussian kernel size (odd number, e.g. 5): "))

            if kernel_size < 1 or kernel_size % 2 == 0:
                print("Invalid size. Using 5.")
                kernel_size = 5

            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

            display_image(blurred, "Gaussian Smoothing")

        elif choice == "5":

            kernel_size = int(input("Enter Median kernel size (odd number, e.g. 5): "))

            if kernel_size < 3 or kernel_size % 2 == 0:
                print("Invalid size. Using 5.")
                kernel_size = 5

            median_filtered = cv2.medianBlur(image, kernel_size)

            display_image(median_filtered, "Median Filtering")

        elif choice == "6":

            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    Interactive_edge_detection("image.jpg")