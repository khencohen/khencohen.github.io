"""
Batch MP4 Compressor
Compresses MP4 files from ~20-30MB down to ~1-5MB using ffmpeg.

Requirements:
    - Python 3.6+
    - ffmpeg installed and available in PATH

Usage:
    python compress_videos.py /path/to/videos
    python compress_videos.py /path/to/videos --output /path/to/output
    python compress_videos.py /path/to/videos --crf 32 --resolution 720
"""

import subprocess
import sys
import os
import argparse
from pathlib import Path


def get_video_info(filepath: str) -> dict:
    """Get video duration and resolution using ffprobe."""
    cmd = [
        "ffprobe", "-v", "quiet",
        "-print_format", "json",
        "-show_streams", "-show_format",
        filepath
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        import json
        info = json.loads(result.stdout)
        video_stream = next(
            (s for s in info.get("streams", []) if s["codec_type"] == "video"), {}
        )
        return {
            "width": int(video_stream.get("width", 0)),
            "height": int(video_stream.get("height", 0)),
            "duration": float(info.get("format", {}).get("duration", 0)),
            "size_mb": int(info.get("format", {}).get("size", 0)) / (1024 * 1024),
        }
    except (subprocess.CalledProcessError, FileNotFoundError):
        return {}


def compress_video(
    input_path: str,
    output_path: str,
    crf: int = 30,
    max_height: int = 720,
    audio_bitrate: str = "64k",
) -> bool:
    """
    Compress a single MP4 file.

    Args:
        input_path:     Path to the source MP4.
        output_path:    Path for the compressed output.
        crf:            Constant Rate Factor (18-51). Higher = smaller file / lower quality.
                        28-32 is a good range for heavy compression.
        max_height:     Scale video down if taller than this (keeps aspect ratio).
        audio_bitrate:  Audio bitrate (e.g. "64k", "96k", "128k").
    """
    # Scale filter: only downscale, never upscale. -2 keeps width divisible by 2.
    scale_filter = f"scale=-2:'min({max_height},ih)'"

    cmd = [
        "ffmpeg", "-y",
        "-i", input_path,
        "-vf", scale_filter,
        "-c:v", "libx264",
        "-preset", "slow",        # slower preset = better compression
        "-crf", str(crf),
        "-c:a", "aac",
        "-b:a", audio_bitrate,
        "-movflags", "+faststart", # optimise for web streaming
        output_path
    ]

    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ ffmpeg error: {e.stderr[:300]}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Batch compress MP4 files.")
    parser.add_argument("input_dir", help="Directory containing MP4 files")
    parser.add_argument("--output", "-o", help="Output directory (default: <input_dir>/compressed)")
    parser.add_argument("--crf", type=int, default=30, help="CRF value 18-51 (default: 30, higher=smaller)")
    parser.add_argument("--resolution", type=int, default=720, help="Max height in pixels (default: 720)")
    parser.add_argument("--audio", default="64k", help="Audio bitrate (default: 64k)")
    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    if not input_dir.is_dir():
        sys.exit(f"Error: '{input_dir}' is not a valid directory.")

    output_dir = Path(args.output) if args.output else input_dir / "compressed"
    output_dir.mkdir(parents=True, exist_ok=True)

    mp4_files = sorted(input_dir.glob("*.mp4"))
    if not mp4_files:
        sys.exit(f"No .mp4 files found in '{input_dir}'.")

    print(f"Found {len(mp4_files)} MP4 file(s). Compressing with CRF={args.crf}, max {args.resolution}p\n")

    total_before = 0
    total_after = 0

    for i, filepath in enumerate(mp4_files, 1):
        output_path = output_dir / filepath.name
        size_before = filepath.stat().st_size / (1024 * 1024)
        total_before += size_before

        print(f"[{i}/{len(mp4_files)}] {filepath.name} ({size_before:.1f} MB)")

        success = compress_video(
            str(filepath),
            str(output_path),
            crf=args.crf,
            max_height=args.resolution,
            audio_bitrate=args.audio,
        )

        if success and output_path.exists():
            size_after = output_path.stat().st_size / (1024 * 1024)
            total_after += size_after
            ratio = (1 - size_after / size_before) * 100
            print(f"  ✓ {size_before:.1f} MB → {size_after:.1f} MB  ({ratio:.0f}% reduction)\n")
        else:
            print(f"  ✗ Failed to compress\n")

    print("=" * 50)
    print(f"Total: {total_before:.1f} MB → {total_after:.1f} MB  "
          f"({(1 - total_after / total_before) * 100:.0f}% reduction)")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
