import sys
import threading

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        tree[i] = []
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def height(node):
        if not tree[node]:
            return 1
        else:
            return 1 + max(height(child) for child in tree[node])
    return height(root)

def main():

    text = input("Choose the input method 'I' for manual, 'F' for file")
    if "I" in text:
        n = int(input())
        parents = list(map(int, input().split()))
    elif "F" in text:
        path = './test/'
        file_name = input("Enter file name: ")
        folder = path + file_name
        if 'a' in file_name:
            print("File contains letter 'a'")
            return
        try:
            with open(folder, 'r', encoding='utf-8') as file:
                n = int(file.readline())
                parents = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("Error: File not found")
            return
        except ValueError:
            print("Error: Invalid input format")
            return
    else:
        print("Enter 'I' or 'F':")
        return 
       
    print(compute_height(n, parents))

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
