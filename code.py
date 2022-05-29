# input: dap an cua nguoi choi
# output: kiem tra xem day co phai ten 1 tinh thanh cua Viet Nam khong
# - neu co: luu ket qua
# - neu khong: hien thi "khong tim thay ket qua"
import turtle
import pygame
screen = turtle.Screen()
pygame.init()

# Thiết lập màn hình giao diện turtle
def setup_turtle():
    
    # Màn hình Turtle
    screen = turtle.Screen()
    # Thiết lập kích thước màn hình 
    screen.setup(879, 579)
    # Thiết lập ảnh nền cho màn hình
    screen.bgpic('background-1.gif')
    # Thiết lập tiêu đề cho cửa sổ chương trình
    turtle.title("W.E.R.O")
   
# Thiet lap ham xu ly input    
def user_input():
    result = []
    index = 5
    
    cities = ['an giang','ba ria-vung tau','bac giang','bac kan','bac lieu','bac ninh','ben tre','binh dinh','binh duong','binh phuoc','binh thuan','ca mau','can tho','cao bang','da nang','dak lak','dak nong','dien bien','dong nai', 'dong thap','gia lai','ha giang','ha nam','ha noi','hai duong','ha tinh','hai duong','hai phong','hau giang','hoa binh','ho chi minh','hung yen','khanh hoa','kien giang','kon tum','lai chau','lam dong','lang son','lao cai','long an','nam dinh','nghe an','ninh binh','ninh thuan','phu tho','phu yen','quang binh','quang nam','quang ngai','quang ninh','quang tri','soc trang','son la','tay ninh','thai binh','thai nguyen','thanh hoa','thua thien hue','tien giang','tra vinh','tuyen quang','vinh long','vinh phuc','yen bai']
    for i in range(0,index):
        n = turtle.textinput('wordle vietnam','cau tra loi cua ban la gi')  #sua
        turtle.clear() #
        index += 1
        n = n.lower()
        ok = 0
        #print(n) 
        if n in cities:        
            ok = 1
        if  ok == 1:
            result.append(n)
            if len(result)== 5:
                break
        #print('ban co the an submit')
        #turtle.write('ban co the an submit',font = ('Arial', 15,'normal'))  # sua
        
        else:
            index -= 1
            print('khong tim thay')
            turtle.write('khong tim thay',font = ('Arial', 15,'normal')) #sua
            
        return result
        
    print(result)    
    
setup_turtle()
user_input()
# for i in range(0,5):
#     user_input()
    
    
    
