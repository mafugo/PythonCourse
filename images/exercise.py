import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 1)
    img_resized = cv2.resize(img, (100, 100))
    cv2.imshow("Photo", img_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, img_resized)

# img1 = cv2.imread("kangaroos-rain-australia_71370_990x742.jpg", 1)
# img2 = cv2.imread("Lighthouse.jpg", 1)
# img3 = cv2.imread("Moon sinking, sun rising.jpg", 1)

# img1_resized = cv2.resize(img1, (100,100))
# img2_resized = cv2.resize(img2, (100,100))
# img3_resized = cv2.resize(img3, (100,100))

# cv2.imwrite("resized1.jpg", img1_resized)
# cv2.imwrite("resized2.jpg", img2_resized)
# cv2.imwrite("resized3.jpg", img3_resized)
