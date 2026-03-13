import argparse


def build_parser():
    parser = argparse.ArgumentParser(
        description="Modify image tools (use a subcommand to run each module independently)"
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available modules",
    )

    # video2image
    v2i = subparsers.add_parser(
        "video2image",
        help="Cut video into images",
    )
    v2i.add_argument("-i", "--input", required=True, help="Input video folder path")
    v2i.add_argument("-o", "--output", required=True, help="Output image folder path")
    v2i.add_argument("-p", "--prefix", default="img", help="Image filename prefix")
    v2i.add_argument(
        "-n",
        "--interval",
        type=int,
        default=30,
        help="Frame extraction interval (default: 30)",
    )

    # deblur
    deblur = subparsers.add_parser(
        "deblur",
        help="Remove blurry images from a folder",
    )
    deblur.add_argument("-i", "--input", required=True, help="Input image folder path")
    deblur.add_argument(
        "-lt",
        "--laplacian-threshold",
        type=float,
        default=100.0,
        help="Laplacian threshold (default: 100.0)",
    )
    deblur.add_argument(
        "-nt",
        "--niqe-threshold",
        type=float,
        default=5.0,
        help="NIQE threshold (default: 5.0)",
    )

    # deduplicate
    dedup = subparsers.add_parser(
        "deduplicate",
        help="Remove duplicate images in a folder",
    )
    dedup.add_argument(
        "-m",
        "--method",
        choices=["CNN", "PHash"],
        required=True,
        help="Deduplication method",
    )
    dedup.add_argument("-i", "--input", required=True, help="Input image folder path")
    dedup.add_argument(
        "-st",
        "--similarity-threshold",
        type=float,
        default=0.90,
        help="Similarity threshold (default: 0.90)",
    )

    # search_duplicate
    sd = subparsers.add_parser(
        "search-duplicate",
        help="Search duplicate images between folders",
    )
    sd.add_argument(
        "-m",
        "--method",
        choices=["cosine", "hamming"],
        required=True,
        help="Similarity search method",
    )
    sd.add_argument(
        "-op",
        "--original-path",
        required=True,
        help="Original image folder path",
    )
    sd.add_argument(
        "-tp",
        "--target-path",
        required=True,
        help="Target image folder path",
    )
    sd.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output folder for matched images",
    )
    sd.add_argument(
        "-st",
        "--similarity-threshold",
        type=float,
        default=0.90,
        help="Similarity threshold (default: 0.90)",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "video2image":
        print("Start to cut video into picture!")
        import video2picture
        video2picture.cutvideo(args.input, args.output, args.prefix, args.interval)
        return

    if args.command == "deblur":
        print("Start to remove fuzzy image!")
        from fuzzy import remove_fuzzy
        remove_fuzzy.remove_fuzzy_picture(
            args.input,
            args.laplacian_threshold,
            args.niqe_threshold,
        )
        return

    if args.command == "deduplicate":
        print("Start to remove duplicate image!")
        from dedup import image_deduplicate
        image_deduplicate.img_deduplicate(
            args.method,
            args.input,
            args.similarity_threshold,
        )
        return

    if args.command == "search-duplicate":
        print("Start to search high similarity images!")
        from search_duplicate import search_duplicate
        search_duplicate.search_duplicate_img(
            args.method,
            args.target_path,
            args.original_path,
            args.output,
            args.similarity_threshold,
        )
        return


if __name__ == "__main__":
    main()
