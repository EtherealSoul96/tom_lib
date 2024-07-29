
import cv2

import cv2
import numpy as np


def create_video(name, data, framerate=60):

    # out = cv2.VideoWriter(f'{name}.avi', cv2.VideoWriter_fourcc(*'DIVX'), framerate, data[0].shape[0:2])
    out = cv2.VideoWriter(f'{name}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), framerate, data[0].shape[0:2])

    for img in data:
        out.write(img)

    out.release()

def create_video_from_pngs(png_directory, output_name, fps, frame_size):
    import os

    # Get the list of PNG files in the directory
    png_files = sorted([f for f in os.listdir(png_directory) if f.endswith('.png')])

    # Initialize the video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_name+".mp4", fourcc, fps, frame_size)

    # Loop through each PNG file and write it to the video writer
    for png_file in png_files:
        image_path = os.path.join(png_directory, png_file)
        frame = cv2.imread(image_path)

        # Resize the frame if necessary
        if frame.shape[:2] != frame_size:
            frame = cv2.resize(frame, frame_size)

        video_writer.write(frame)
        # print(frame.shape)

    # Release the video writer and close the file
    video_writer.release()

if __name__ == "__main__":




    # import os
    # folder = "C:/Users/Administrator/Pictures/manar stack explanation/"
    # output_name = "ex_video"
    #
    #
    # # Set the directory containing the PNG files
    # png_directory = "C:/Users/Administrator/Pictures/manar stack explanation/"
    #
    # # Set the output video file name and parameters
    # output_name = 'ex_video.mp4'
    # fps = 1  # Frames per second
    # frame_size = (778, 652)  # Frame size (width, height)
    # # frame_size = None
    #
    #
    # create_video_from_pngs(png_directory, output_name, fps, frame_size)





    # import os
    folder = "C:/Users/Administrator/Pictures/manar stack explanation/"
    output_name = "ex_video2"
    fps = 2
    frame_size = (778, 652)
    # file_names = [file_name for file_name in os.listdir(folder) if file_name.endswith('.png')]
    # data = []
    # for file_name in file_names:
    #     print(file_name)
    #     with open(folder + file_name) as file:
    #         data.append(file)
    # # create_video(folder + "ex_video", data, 10)
    #
    # out = cv2.VideoWriter(f'{folder + output_name}.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 2,  frame_size)
    #
    # for file_name in file_names:
    #     frame = cv2.imread(folder + file_name)
    #     out.write(frame)
    #     out.write(frame)
    #
    # out.release()


    create_video_from_pngs(folder, output_name, fps, frame_size)





