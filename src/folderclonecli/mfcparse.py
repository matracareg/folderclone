from argparse import ArgumentParser

def main():
    from folderclone.multifolderclone import multifolderclone
    parse = ArgumentParser(description='A tool intended to copy large files from one folder to another.')
    parse.add_argument('--width', '-w', type=int, default=2, help='Set the width of the view option.')
    parse.add_argument('--path', '-p', default='accounts', help='Specify an alternative path to the service accounts.')
    parse.add_argument('--threads', type=int, default=None,help='Specify a different thread count. Cannot be greater than the amount of service accounts available.')
    parse.add_argument('--skip-bad-dests',default=False,action='store_true',help='Skip any destionations that cannot be read.')
    parsereq = parse.add_argument_group('required arguments')
    parsereq.add_argument('--source-id','--source', '-s',help='The source ID of the folder to copy.',required=True)
    parsereq.add_argument('--destination-id','--destination', '-d',action='append',help='The destination ID of the folder to copy to.',required=True)
    args = parse.parse_args()
    mfc = multifolderclone(
        source=args.source_id,
        dest=args.destination_id,
        path=args.path,
        width=args.width,
        thread_count=args.threads,
        skip_bad_dests=args.skip_bad_dests
    )
    try:
        mfc.clone()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('Quitting.')