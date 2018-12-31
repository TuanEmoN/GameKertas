import random
import os, sys
# Warna
G = "\033[32m";
O = "\033[33m";
B = "\033[36m";
R = "\033[31m";
W = "\033[0m";
P = "\033[35m";
print ""
 
print W+"Created by : Mr.EmoN"
print R+"[+]===========================================================================[+]"
print B+"permainan Batu Kertas Gunting"
print G+"||++       ++|| ||  +++++     ||====== ||++        ++||   +++++   ||++       ||"
print G+"|| ++     ++ || ||++     ++   ||       ||  ++     +  || ||     || || ++      ||"
print G+"||  ++   ++  || ||        ++  ||       ||   ++   ++  || ||     || ||  ++     ||"
print B+"||    +++    || ||            ||+++++  ||    ++ ++   || ||     || ||   ++    ||"
print R+"||           || ||            ||       ||     +++    || ||     || ||    ++   ||"
print R+"||           || ||            ||       ||            || ||     || ||     ++  ||"
print R+"||           || ||            ||=====  ||            ||   +++++   ||      ++ ||"
print R+"Error Not Found"
print R+"[+]============================================================================[+]"
print ""
print R+"Pilihan :"
print ""
print O+"1. Batu"
print R+"2. Kertas"
print R"3. Gunting"
 
def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)
def permainan():
    kamu = int(input("Masukan Pilihanmu: " ))
    kom = random.choice(["Batu", "Kertas" , "Gunting"])
    if kamu == 1:
        print G+"kamu    : Batu"
        print("komputer  :", kom)
        if kom =="Batu":
            print B+"\tDraw"
        if kom =="kertas":
            print G+"\tlu menang"
        if kom =="gunting":
            print R+"\tlu kalah goblok:v"
    if kamu == 2:
        print R+"kamu     : Kertas"
        print("komputer   :", kom)
        if kom =="Batu":
            print R+"\tlu kalah goblok:v"
        if kom =="Kertas":
            print B+"\tDraw"
        if kom =="Gunting":
            print G+"\tlu menang"
    if kamu == 3:
        print G+"kamu      : Gunting"
        print("komputer   :", kom)
        if kom =="Batu":
            print G+"\tlu menang"
        if kom =="Kertas":
            print R+"\tlu kalah goblok:v"
        if kom =="Gunting":
            print R+"\tDraw"
    if kamu >=4:
        print R+"Pilihamu salah kamvank:v"
        restart()
permainan()
restart()
try:
         permainan()
except KeyboardInterrupt:
        os.system('clear')
        restart()
