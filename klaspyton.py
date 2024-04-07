absen=int(input("input jumlah absen="))
uts=int(input("input jumlah uts="))
uas=int(input("input jumlah uas="))
nilai_batas=60
jumlah=absen+uts+uas
rata_rata=jumlah/3
print("jumlah nilai =",jumlah)
print(" nilai rata-rata =",rata_rata)
if rata_rata>=95:
    print("anda dinyatakan lulus dengan nilai=",rata_rata)
    print("grade : A")
elif rata_rata>=90:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= A-")
elif rata_rata>=85:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= B+")
elif rata_rata>=80:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= B")
elif rata_rata>=75:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= B-")
elif rata_rata>=70:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= C+")
elif rata_rata>=65:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= C")
elif rata_rata>=60:
    print("anda di nyatakan lulus dengan nilai=",rata_rata)
    print("anda mndapat grade= C-")
else:
    print("anda tidak lulus")
          
