import os,cv2
import numpy as np


def add_noise(image, noise_factor=10):
    noise = np.random.randn(*image.shape) * noise_factor
    noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
    return noisy_image

def flip(image):
    flipped_image = cv2.flip(image, 1)
    return flipped_image

def adjust_brightness_contrast(image, alpha=2.0, beta=1.0):
    adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted

main_dir_path='/home/pasupathikumar/Downloads/2023-11-06-20231108T102522Z-001/backside_cam/data_agument_videos'
for source_video in os.listdir(main_dir_path):
    source_videopath=os.path.join(main_dir_path, source_video)
    base_file_name=os.path.basename(source_videopath).split(".")[0]
    print(base_file_name)


    cap = cv2.VideoCapture(source_videopath)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    noise_filename = os.path.dirname(source_videopath)+f"/{base_file_name}_noise.avi"
    noise_video = cv2.VideoWriter(noise_filename, fourcc, 25.0, (1920, 1080))

    flip_filename = os.path.dirname(source_videopath)+f"/{base_file_name}_flip.avi"
    flip_video = cv2.VideoWriter(flip_filename , fourcc, 25.0, (1920, 1080))


    adjust_filename = os.path.dirname(source_videopath)+f"/{base_file_name}_adjust.avi"
    adjust_video = cv2.VideoWriter(adjust_filename, fourcc, 25.0, (1920, 1080))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        noise_video.write(add_noise(frame))
        flip_video.write(flip(frame))
        adjust_video.write(adjust_brightness_contrast(frame))
        #cv2.imshow('Live Stream', add_noise(frame))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    noise_video.release()
    flip_video.release()
    adjust_video.release()
    cv2.destroyAllWindows()
