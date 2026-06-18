def convert(v1 = 'erro'):
    v1 = v1.replace(':(','🙁')
    v1 = v1.replace(':)','🙂')
    return v1
def main():
    text = input()
    print(convert(text))

main()

