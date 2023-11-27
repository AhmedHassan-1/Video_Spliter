import ffmpeg
import argparse
import os


parser = argparse.ArgumentParser(description="For split Video")
parser.add_argument(
    "-i", "--Video_Input", type=str, help="Video will be splited", required=True
)
parser.add_argument(
    "-dir", "--directory", type=str, help="your directory for output", required=False
)
parser.add_argument("-n", "-name", "--Name", type=str, help="file name", required=True)
parser.add_argument(
    "-t", "-time", "--Time", type=int, help="time for each video", required=True
)
parser.add_argument(
    "-e", "-extension", "--Extension", type=str, help="def: ts", required=False
)
args = parser.parse_args()
if args.Extension == None:
    ex = "ts"
else:
    ex = args.Extension
if args.directory == None:
    dir = os.getcwd()
else:
    dir = args.directory
ffmpeg.input(args.Video_Input).output(
    f"{dir}/{args.Name}_%03d.{ex}",
    c="copy",
    f="segment",
    segment_time=args.Time,
    reset_timestamps=1,
    segment_start_number=1,
    loglevel="quiet",
).run()
print("Split Had Finshed")
