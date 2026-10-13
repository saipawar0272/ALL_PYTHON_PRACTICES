class C1:
    def disp1(self):
        print("C1--disp1()--instance methd")

class C2(C1):
            def disp2(self):
                print("c2--disp()--Instance Method")

#main program


o2=C2()
o2.disp1()
o2.disp2()

