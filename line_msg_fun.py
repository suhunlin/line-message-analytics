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
    found_name = None

    if not messages:
        print("無訊息資料!!!")
    else:
        for message in messages:
            split_message = message.split(' ')
            if split_message[1] == name:
                found_name = split_message[1]
                for msg in split_message[2:]:
                    count += len(msg)

    if not found_name:
        print('沒有', name, '的訊息!!!')
    else:
        print(name,'字數共:',count,'字')

def count_by_string(messages,search_string):
    count = 0

    if not messages:
        print("無訊息資料!!!")
    else:
        for message in messages:
            split_message = message.split(' ')
            for msg in split_message[2:]:
                if msg == search_string:
                    count += 1
    print(search_string,'出現：',count,'次')

def main():
    filename = 'line.txt'
    name = 'Allen'
    search_string = '圖片'
    if os.path.exists(filename):
        messages = read_function(filename)
    else:
        messages = []
        print('請輸入正確的檔案名稱及路徑!!!')
    count_by_name(messages,name)
    count_by_string(messages,'圖片')

if __name__ == '__main__':
    main()