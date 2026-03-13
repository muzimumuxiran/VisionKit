import datetime
import cv2
import os

def cutvideo(video_path, out_path, prefix, interval):
    num = 0
    j = 0
    #interval = 30  # Extract one frame every 30 frames

    if not os.path.isdir(video_path):
        print(f"[Error] Input path does not exist or is not a folder: {video_path}")
        return

    os.makedirs(out_path, exist_ok=True)
    files = os.listdir(video_path)

    for filename in files:
        file_path = os.path.join(video_path, filename)

        if not os.path.isfile(file_path):
            print(f"[Skip] Not a file: {file_path}")
            continue

        try:
            vid = cv2.VideoCapture(file_path)
            if not vid.isOpened():
                print(f"[Skip] Unable to open video: {file_path}")
                continue

            total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
            print(f"🎬 Processing video: {file_path}, total frames: {total_frames}")

            fail_count = 0
            max_fail = 30
            frame_idx = 0

            while True:
                is_read, frame = vid.read()

                # Read failure or invalid frame content
                if not is_read or frame is None or frame.size == 0:
                    fail_count += 1
                    if fail_count >= max_fail:
                        print(f"[⚠️  Warning] Consecutive read failures exceeded {max_fail}, skipping video: {file_path}")
                        break
                    continue
                else:
                    fail_count = 0  # Successful read; reset counter

                if frame_idx % interval == 0:
                    j += 1
                    timestamp = datetime.datetime.now().strftime("%Y%m%d")
                    file_name = f"{prefix}{timestamp}{j:04d}.jpg"
                    save_path = os.path.join(out_path, file_name)
                    success = cv2.imwrite(save_path, frame)
                    if success:
                        print(f"[✅ Saved] {save_path}")
                    else:
                        print(f"[❌ Save failed] {save_path}")

                frame_idx += 1

            vid.release()
            print(f"[✅ Done] Video processing finished: {file_path}\n")

        except Exception as e:
            print(f"[❌ Error] An error occurred while processing video: {file_path}")
            print(f"       Error details: {str(e)}")
            continue
