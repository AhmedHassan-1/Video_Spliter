import ffmpeg
import argparse
import os


parser = argparse.ArgumentParser(description="For split Video")
parser.add_argument(
    "-i", "--Video_Input", type=str, help="Video will be splited", required=True
)
parser.add_argument(
    "-dir",
    "--directory",
    type=str,
    help="your directory for output",
    required=False,
    default=os.getcwd(),
)
parser.add_argument(
    "-n",
    "-name",
    "--Name",
    type=str,
    help="file name",
    required=False,
    default="output",
)
parser.add_argument(
    "-t", "-time", "--Time", type=int, help="time for each video", required=True
)
parser.add_argument(
    "-e",
    "-extension",
    "--Extension",
    type=str,
    help="default : mp4",
    required=False,
    default="mp4",
)
args = parser.parse_args()

ffmpeg.input(args.Video_Input).output(
    f"{args.directory}/{args.Name}_%03d.{args.Extension}",
    c="copy",
    f="segment",
    segment_time=args.Time,
    reset_timestamps=1,
    segment_start_number=1,
    loglevel="quiet",
).run()
print("Split Had Finshed")
