import random

def main():
    with open("big_data_file.txt","w+") as f:
        
        for i in range (4000000000):
            a = random.randint(1, 200)
            f.write(f'{a}\n')

    

if __name__== "__main__":
  main()
