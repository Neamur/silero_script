

def source_file(filename="./source.txt"):
    """
    Takes the file and does operations to clean it up, so that it can be used by the Silero TTS.
    The default filename will be ./source.txt
    """
    with open(filename, "r") as f:
        t = f.readlines()
        p=[]

        list_remove = []
        while True: 
            to_remove = input("Enter the string you want to remove (type 'fp_clean' to comense the clean up process): ")
            if to_remove == "fp_clean":
                break
            list_remove.append(to_remove)

        for i in range(len(t)):
            for j in list_remove:
                try:
                    t[i] = t[i].replace(f"{j}","")
                except:
                    a = "hehe"
            if t[i] == '\n' or t[i] == ' \n':
                continue
            t[i] = t[i].strip()
            p.append(t[i])
    return p