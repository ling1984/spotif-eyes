











def main():
    while True:
        usin = input(">")
        match usin:
            case "start":
                print("here it will load in the hashmap from file and start listening to your friends")
            case "update":
                print("here it will fetch your top artists and liked songs and change the hashmap and save it to file")
            case "status":
                print("here it will print what your mates are listening to, number of new recs since recs called")
            case "recs":
                print("will give you ur list of recs, with spotify links to listen")
            case "saverecs":
                print("saves your recs to your liked songs")
            case "exit":
                print("saves your recs to a file, quits")
                exit()

main()
