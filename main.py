import argparse
import downloadfw
import tools

parser = argparse.ArgumentParser(description="A multi-functional tool for modding Tolino eReaders")

parser.add_argument("--download", type=str, help="Download a device's firmware and specify the filename. Needs the --device argument.")
parser.add_argument("--device", type=str, help="Choose the device you want to download the firmware for.", choices=["page2", "shine3", "vision5", "epos2", "vision2", "page"])
parser.add_argument("--downloadnook", type=str, help="Download the firmware for the Nook Glowlight Plus and specify the filename.")
parser.add_argument("--assemblenook", action="store_true", help="Assemble a Tolino-compatible firmware package with parts of the Nook firmware. Will be saved in 'nookolino.zip' (Not really usable due to missing nook SN)")
parser.add_argument("--nookfw", type=str, help="Path to a Nook firmware package. (Required by --assemblenook)")
parser.add_argument("--tolinofw", type=str, help="Path to a Tolino firmware package. (Required by --assemblenook)")
parser.add_argument("--board", type=str, help="Specify the tolino's board. Example: E60QV0. (Required by --assemblenook)")

args = parser.parse_args()
if args.download:
    if not args.device:
        print("Error: --device is required when using --download.")
    else:
        downloadfw.download(args.download, args.device)

if args.downloadnook:
    downloadfw.downloadnookfw(args.downloadnook)

if args.assemblenook:
    if not args.nookfw or not args.tolinofw or not args.board:
        print("Error: --nookfw, --board and --tolinofw are required for --assemblenook.")
    else:
        tools.generatenookolinopackage(args.nookfw, args.tolinofw, "nookolino", args.board)
