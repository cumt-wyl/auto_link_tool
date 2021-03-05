from requests import get
import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
if __name__=="__main__":

    url='http://10.2.5.251:801/eportal/'
    print("CUMT_STU所在IP："+get_ip())
    print("------------------------------------------------------------------")
    print("请确保已连接CUMT_STU（右下角小图标显示有信号状态）且未超过允许设备数量")
    print("首次运行程序会生成txt文档，若希望下次直接登录请勿删除此文档")
    print("可将此程序快捷方式发送至桌面，享受一键登录的快感 ^_^")
    print("------------------------------------------------------------------")
    wlan_user_ip=get_ip()
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81'
    }

    tip=int(input("直接登录请输入1，第一次登陆或重置账号请输入2\n"))
    if tip==2:
        amount=input("请输入账号：")
        password=input("请输入密码：")
        operator=int(input("请选择运营商（输入数字）：1.移动 2.联通 3.电信 4.校园网 ："))
        if operator==1:
            user_account=amount+'@cmcc'
        elif operator==2:
            user_account=amount+'@unicom'
        elif operator==3:
            user_account=amount+'@telecom'
        elif operator==4:
            user_account=amount
        else:
            print("输入错误请重新运行！")

        with open('./login_amount.txt','w') as f:
            f.write(amount+' '+password+' '+user_account)
        param={
            'c':'Portal',
            'a':'login',
            'login_method':'1',
            #登陆账号
            'user_account': user_account,
            #登录密码
            'user_password': password,
            'wlan_user_ip' : wlan_user_ip,
        }
        respones=get(url=url,params=param,headers=headers)
        print('ok')
    elif tip==1:
        with open('./login_amount.txt','r') as f:
            data=f.readline().strip('\n')
            amount,password,user_account=data.split(' ')
        param={
            'c':'Portal',
            'a':'login',
            'login_method':'1',
            #登陆账号
            'user_account': user_account,
            #登录密码
            'user_password': password,
            'wlan_user_ip' : wlan_user_ip,
        }
        respones=get(url=url,params=param,headers=headers)
        print('ok')
    else:
        print("输入数字错误请重新运行")




