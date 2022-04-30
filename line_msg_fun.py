import os

def read_function(filename):
    messages = []
    if not filename:
        print('請輸入檔案名稱!!!')
    try:
        with open(filename,'r',encoding='utf-8-sig') as file:
            for line in file:
                messages.append(line.strip())

    except Exception as error_message:
        print(error_message)
    return messages

def count_by_name(messages,name):
    count = 0

    if not messages:
        print("無訊息資料!!!")
    else:
        for message in messages:
            split_message = message.split(' ')
            if split_message[1] == name:
                for msg in split_message[2:]:
                    count += len(msg)
    print(name,'字數共:',count,'字')

def main():
    filename = 'line.txt'
    name = 'Viki'
    if os.path.exists(filename):
        messages = read_function(filename)
    else:
        messages = []
        print('請輸入正確的檔案名稱及路徑!!!')
    count_by_name(messages,name)

if __name__ == '__main__':
    main()