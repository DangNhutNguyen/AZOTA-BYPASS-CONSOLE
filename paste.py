class colors:
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    BLUE = '\033[34m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
import pyautogui as pag
import time
import pyfiglet
import pyperclip
def main():
    # Open Termial
    time.sleep(time1)
    pag.hotkey('ctrl', 'shift', 'i')
    time.sleep(0.7)
    # Open Console
    pag.locateOnScreen("Console.png", confidence=0.7)
    time.sleep(0.5)
    pag.click("Console.png")
    time.sleep(0.5)
    # HAHA
    with open('console.txt', 'r') as file:
        code_to_paste = file.read()
    pyperclip.copy(code_to_paste)
    time.sleep(0.5)
    pag.hotkey('ctrl', 'v')
    time.sleep(0.3)
    pag.hotkey('enter')
    time.sleep(0.3)
    pag.locateOnScreen("X.png", confidence=0.7)
    time.sleep(0.1)
    pag.click("X.png")
    time.sleep(0.2)
    pag.hotkey('esc')

# Title
text = "Azota Bypassv2.0"
ascii_art = pyfiglet.figlet_format(text)
print(colors.BLUE + ascii_art + colors.END)
print(colors.RED + "Language:" + colors.END, end=' ')
# Language
lang = int(input(" 1-Vietnamese ; 2-English: "))
# Infomation1
if lang == 1:
    print(colors.RED + "Quản lý: " + colors.END, end=' ')
    print("Nguyễn Huỳnh Đăng Nhựt")
    print(colors.RED + "Liên hệ: " + colors.END, end=' ')
    print("penciltalk0910@gmail.com")
    password1 = int(input(colors.RED + "Vui lòng nhập mật khẩu: " + colors.END))
# Infomation 2
    while True:
        if password1 == 122333445:
            print("")
            print(colors.BLUE + "Chúc bạn sử dụng phần mềm vui vẻ" + colors.END)
            print(colors.BLUE + "Phiên bản hiện tại: ", text)
            print(colors.RED + 'Lưu ý: Phần mềm chỉ sử dụng dưới mục đích học tập và tìm hiểu, không dùng phần mềm dưới mục đính thực hiện trái phép các hoạt động trong kì thi' + colors.END)
            print(colors.RED + '"Bạn đồng ý chứ:' + colors.END)
            Ok1 = int(input( "1-Đồng ý ; 2-Không đồng ý: "))
            while True:
                if Ok1 == 1:
                    print(colors.BLUE + "Tôi ghi nhận ý kiến này từ bạn" + colors.END)
                    time1 = float(input(colors.YELLOW + "Nhập thời gian chờ để (Kể từ thời gian bạn chạy chương trình cho đến khi dùng AZOTA (Khuyến khích: 5): " + colors.END))
                    print("Đã ghi nhận thời gian chờ của bạn là: ", time1)
                    time.sleep(1)
                    print(colors.YELLOW + 'Sau khi bắt đầu, bạn bật AZOTA và đợi khoảng chờ hệ thống sẽ chạy sau khoảng thời gian bạn đã định sẵn' + colors.END)
                    do = int(input("Nhấn 1 - Bắt đầu, 2 - Quay lại thao tác: "))
                    while True:
                        if do == 1:
                            main()
                            print(colors.BLUE + 'Thực hiện thành công' + colors.END)
                            time.sleep(0.5)
                            print(colors.RED + "Nếu script không thể thực hiện, vui lòng kiểm tra và nâng cấp phiên bản mới tại Github" + colors.END)
                            print(colors.YELLOW + "Vui lòng tham khảo trang web: " + colors.END, end=' ')
                            print("https://github.com/DangNhutNguyen/AZOTA-BYPASS")
                            break
                        else:
                            break
                else:
                    print("")
                    print(colors.RED + "Nếu bạn không đồng ý thì không nên sử dụng phần mềm trái phép này" + colors.END)
                    break
        else:
            print(colors.RED + "Mật khẩu sai, vui lòng liên hệ Admin để nhận đúng" + colors.END)
            break
else:
        print(colors.RED + "Adminator: " + colors.END, end=' ')
        print("Nguyễn Huỳnh Đăng Nhựt")
        print(colors.RED + "Contact: " + colors.END, end=' ')
        print("penciltalk0910@gmail.com")
        password1 = int(input(colors.RED + "Please enter password: " + colors.END))
        while True:
            if password1 == 122333445:
                print("")
                print(colors.BLUE + "Good luck!" + colors.END)
                print(colors.BLUE + "Your version is: ", text)
                print(colors.RED + "This tool only use for education. Please don't use this tool for your tests and crack some thing special" + colors.END)
                print(colors.RED + 'Agree? ' + colors.END, end=' ')
                Ok1 = int(input("1 - Agree; 2 - Disagree: "))
                while True:
                    if Ok1 == 1:
                        print(colors.BLUE + "I recorded that" + colors.END)
                        time1 = float(input(colors.YELLOW + "Enter time for waiting you open the AZOTA Website (Recommend: 5): " + colors.END))
                        print("Your time is: ", time1)
                        time.sleep(1)
                        print(colors.YELLOW + 'After you run this script, open the AZOTA tab before this script working' + colors.END)
                        do = int(input("Press 1 - Start; 2 - Stop "))
                        while True:
                            if do == 1:
                                main()
                                print(colors.BLUE + 'AZOTA Bypass Successfully work' + colors.END)
                                time.sleep(0.5)
                                print(colors.RED + "If tools didn't work successfully, please check for update on Github" +colors.END)
                                print(colors.YELLOW + "Please check on this site" + colors.END, end=' ')
                                print("https://github.com/DangNhutNguyen/AZOTA-BYPASS")
                                break
                            else:
                                break
                    else:
                        print("")
                        print(colors.RED + "If you don't agree to this license, please don't work on it" + colors.END)
                        break
            else:
                print(colors.RED + "Wrong password, Contact to admin for more" + colors.END)
                break