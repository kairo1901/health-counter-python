
eng = ["English","eng","Eng","ENG","en","En","EN"]
vie = ["Vietnamese","vn","vi","VN","Vn","Vi","VI","vie","Vie","VIE"]
exitx = "x"
print("Bạn muốn lựa chọn ngôn ngữ nào? / Which language would you like to choose?")
print("[eng] = English\n[vie] = Vietnamese\n [x] = exit")
while True:
    a = input("vie/eng/x : ")


    if a in eng:
        print("Health Tool: BMI Index Analysis \n")

        # Validate current year input
        while True:
            try:
                CURRENT_YEAR = int(input("\nEnter the current year: "))
                break
            except ValueError:
                print("Invalid input, please enter a positive integer.")

        # Gender input options
        male_list = ["yes", "y", "Yes", "YES", "Y"]
        female_list = ["no", "n", "No", "NO", "N"]

        # Input user information
        a_name = str(input("Your last name: "))
        b_name = str(input("Your middle name: "))
        c_name = str(input("Your first name: "))

        while True:
            try:
                birth_year = int(input("Your year of birth: "))
                break
            except ValueError:
                print("Invalid input, please enter a positive integer.")

        while True:
            gender_input = input("Are you a male? (yes/no): ")
            if gender_input in male_list:
                gender = True
                break
            elif gender_input in female_list:
                gender = False
                break
            else:
                print("-> Invalid input, please try again.")

        while True:
            try:
                weight_kg = float(input("Your weight (kg): ").replace(",", "."))
                break
            except ValueError:
                print("Please enter a decimal number.")

        while True:
            try:
                height_m = float(input("Your height (m): ").replace(",", "."))
                break
            except ValueError:
                print("Please enter a decimal number.")

        # Calculate age
        age = CURRENT_YEAR - birth_year

        print("\n\n╔" + '═' * 41 + "╗\n")
        print(" " * 2 + "-> Hello, " + c_name + ".")

        print(" " * 10 + "❰ ↓ Your Information ↓ ❱\n")
        print(" " * 8 + "Full Name: " + a_name + " " + b_name + " " + c_name + ".")
        print(" " * 7 + "Age: " + str(age) + " years old, born in " + str(birth_year) + ".")
        print(" " * 13 + f"Weight: {weight_kg} kg.")
        print(" " * 13 + f"Height: {height_m} m.")

        if gender:
            if age < 18:
                print(" " * 11 + "You are a boy.")
            elif age <= 30:
                print(" " * 11 + "You are a young man.")
            elif age <= 60:
                print(" " * 9 + "You are a man, \n         possibly an adult.")
            else:
                print(" " * 12 + "You are likely elderly.")
        else:
            if age < 18:
                print(" " * 9 + "You are still a girl.")
            elif age <= 30:
                print(" " * 11 + "You are a young woman.")
            elif age <= 60:
                print(" " * 9 + "You are a woman, \n          possibly an adult.")
            else:
                print(" " * 12 + "You are likely elderly.")

        print("\n" + " " * 18 + "❰ End ❱")
        print("╚" + ('═' * 41) + "╝\n")
        print("<==================================>")

        # Ask user to open menu
        menu_yes = ["yes", "y", "Yes", "YES", "Y"]
        menu_no = ["no", "n", "No", "NO", "N"]

        while True:
            ask = str(input("Do you want to open the menu? (y/n): "))
            if ask in menu_yes:
                break
            elif ask in menu_no:
                print("Exiting.")
                exit()
            else:
                print("Invalid input. Exiting program.")
                exit()

        # Menu loop
        while True:
            print("\n┌" + "─" * 40 + "┐")
            print("│{:^40}│".format("BMI CALCULATION PROGRAM"))
            print("├" + "─" * 40 + "┤")
            print("│ {:<39}│".format("        0. Exit Program "))
            print("│ {:<39}│".format("        1. Calculate BMI "))
            print("│ {:<39}│".format("        2. Analyze BMI "))
            print("│ {:<39}│".format("        3. Calculator "))
            print("└" + "─" * 40 + "┘")

            choice = input(" → Enter your choice (0,1,2,3): ")

            bmi = weight_kg / (height_m ** 2)
            bmi = round(bmi, 2)

            if choice == "1":
                print("\nCalculating BMI:")
                print(f"  {weight_kg} / ({height_m}^2) = {bmi}")
                print(f"  Your BMI is: {bmi}")
            elif choice == "2":
                print("\nAnalyzing your BMI:")
                if bmi < 18.5:
                    print("  You are underweight.")
                elif bmi < 25:
                    print("  Your weight is normal.")
                elif bmi < 30:
                    print("  You are overweight.")
                elif bmi < 35:
                    print("  You have obesity class I.")
                elif bmi < 40:
                    print("  You have obesity class II.")
                else:
                    print("  You have obesity class III (dangerous).")

            elif choice == "3":
                while True:
                    print("\n┌" + "─" * 14 + "┐")
                    print("│{:^14}│".format("CALCULATOR"))
                    print("├" + "─" * 14 + "┤")
                    print("│ {:<11}│".format("  0. Exit    "))
                    print("│ {:<11}│".format("  1. Add (+) "))
                    print("│ {:<11}│".format("  2. Sub (-) "))
                    print("│ {:<11}│".format("  3. Mul (x) "))
                    print("│ {:<11}│".format("  4. Div (÷) "))
                    print("└" + "─" * 14 + "┘")

                    calc = input("Enter your choice (0-4): ")

                    if calc == "1":
                        print("Addition! ")
                        try:
                            one = float(input("First number: "))
                            two = float(input("Second number: "))
                            print(f"{one} + {two} = {one+two}")
                        except ValueError:
                            print("Invalid input, please enter numbers.")

                    elif calc == "2":
                        print("Subtraction! ")
                        try:
                            one = float(input("First number: "))
                            two = float(input("Second number: "))
                            print(f"{one} - {two} = {one-two}")
                        except ValueError:
                            print("Invalid input.")

                    elif calc == "3":
                        print("Multiplication! ")
                        try:
                            one = float(input("First number: "))
                            two = float(input("Second number: "))
                            print(f"{one} x {two} = {one*two}")
                        except ValueError:
                            print("Invalid input.")

                    elif calc == "4":
                        print("Division! ")
                        try:
                            one = float(input("First number: "))
                            two = float(input("Second number: "))
                            print(f"{one} ÷ {two} = {one/two}")
                        except ValueError:
                            print("Invalid input.")
                        except ZeroDivisionError:
                            print("Cannot divide by zero.")

                    elif calc == "0":
                        print("Exiting calculator.")
                        print("Note: Calculations might not be perfect.")
                        break

                    else:
                        print("Invalid choice, please try again.\n")

            elif choice == "0":
                print("Exited successfully!")
                print("These results are machine-generated and may not be 100% accurate.")
                print("It is recommended to consult a medical professional.")
                break

            else:
                print("Invalid selection, please enter again.\n")
        break


    #tiếng anh



    elif a in vie:
        print("Tool tính sức khỏe chỉ số BMI phân tích \n")
        # tk = "amin"
        # mk = "admin123"
        # tí coi lại tài liệu lỗi để chỉnh fix nếu người dùng nhập sai năm còn bắt nhập lại
        while True:
            try:
                HIEN_TAI = int(input("\nCho biết năm hiện tại là: "))
                break
            except ValueError:
                print("Nhập sai, vui lòng nhập số nguyên dương.")
        # print("\ntk/mk = amin/amin123\n")

        # #kiểm tra tk
        # while True:
        #     nhap_tk = input("Tài khoản của bạn là: ")
        #     if nhap_tk == tk:
        #         print("Đăng nhập thành công!\n")
        #         break
        #     else:
        #         print("Sai tài khoản, thử lại.")

        # #kiểm tra mk
        # while True:
        #     nhap_mk = input("Mật khẩu của bạn là: ")
        #     if nhap_mk == mk:
        #         print("Đăng nhập thành công!\n")
        #         break
        #     else:
        #         print("Sai mật khẩu, thử lại.")

        # list if 
        trai_list = ["yes","y","Yes","YES","Y"]
        gai_list = ["no","n","No","NO","N"]

        # nhập tt người ùng
        a_name = str(input("Họ của bạn là: "))
        b_name = str(input("Tên đệm của bạn là: "))
        c_name = str(input("Tên chính của bạn là: "))

        while True:
            try:
                nam_sinh = int(input("Năm sinh của bạn là: "))
                break
            except ValueError:
                print("Nhập sai, vui lòng nhập số nguyên dương.")

        while True:

            hoi_trai = input(str("Bạn có phải là một người đàn ông không(yes/no): "))

            if hoi_trai in trai_list:
                gioitinh = True
                break
            elif hoi_trai in gai_list:
                gioitinh = False
                break
            else:
                print("-> Sai cú pháp, nhập lại.")
        while True:       
            try:       
                can_kg = float(input("Cân nặng của bạn là(kg): ").replace(",", "."))
                break
            except ValueError:
                print("vui lòng nhập số thập phân.")

        while True:
            try:
                chieucao_m = float(input("Chiều cao của bạn là (m): ").replace(",", "."))
                break
            except ValueError:
                print("Vui lòng nhập số thập phân.")

        #Tính tuổi

        tuoi = HIEN_TAI - nam_sinh

        print("\n\n╔" + '═' * 41 + "╗\n")

        print(" "*2+"-> Chào "+ c_name+".")

        print(" "*10+"❰ ↓ Thông Tin của bạn"". ↓ ❱\n")

        print(" "*8+"Họ và tên: "+a_name + " "+b_name+ " " +c_name+".")

        print(" "*7+"Tuổi: "+str(tuoi)+" tuổi, sinh năm "+str(nam_sinh)+".")

        print(" "*13+"Cân nặng: "+str(can_kg)+" kg.")

        print(" "*13+"Chiều cao: "+ str(chieucao_m)+" m.")

        if gioitinh == True:
            if tuoi < 18:
                print(" "*11+"Bạn là một cậu bé.")
            elif tuoi <= 30:
                print(" "*11+"Bạn là một chàng trai.")
            elif tuoi <= 60:
                print(" "*9+"Bạn là một người đàn ông, \n         có thể bạn đã trưởng thành.")
            else:
                print(" "*12+"Bạn có lẽ đã già.")
        else:
            if tuoi < 18:
                print(" "*9+"Bạn vẫn còn là một bé gái.")
            elif tuoi <= 30:
                print(" "*11+"Bạn là một cô gái")
            elif tuoi <= 60:
                print(" "*9+"Bạn là một người phụ nữ, \n          có thể bạn đã trưởng thành.")
            else:
                print(" "*12+"Bạn có lẽ đã già.")



        print("\n"+" "*18+"❰ Hết"". ❱")

        print("╚" + ('═' * 41) + "╝\n")

        print("<==================================>")

        ask_hoimenu = ["yes","y","Yes","YES","Y"]
        asko_hoimenu = ["no","n","No","NO","N"]
        ask = "0"
        while True:
            ask = str(input("Bạn có muốn mở menu không(y,n)"))
            if ask in ask_hoimenu:
                break
            elif ask in asko_hoimenu:
                print("Thoát.")
                exit()
            else:
                print("Nhập sai, thoát chương trình.")
                exit()


        while True:
            print("\n┌" + "─" * 40 + "┐")
            print("│{:^40}│".format("CHƯƠNG TRÌNH TÍNH CHỈ SỐ BMI  "))
            print("├" + "─" * 40 + "┤")
            print("│ {:<39}│".format("        0. Thoát chương trình"))
            print("│ {:<39}│".format("        1. Tính chỉ số BMI"))
            print("│ {:<39}│".format("        2. Phân tích chỉ số BMI"))
            print("│ {:<39}│".format("        3. Tính toán"))
            print("└" + "─" * 40 + "┘")

            a = input(" → Nhập lựa chọn của bạn (0,1,2,3): ")

            bmi = can_kg / (chieucao_m ** 2)
            bmi = round(bmi, 2)

            if a == "1":
                print("\nTính toán chỉ số BMI:")
                print(f"  {can_kg} / ({chieucao_m}^2) = {bmi}")
                print(f"  Chỉ số BMI của bạn là: {bmi}")
            elif a == "2":
                print("\nPhân tích chỉ số BMI của bạn:")
                if bmi < 18.5:
                    print("  Bạn đang bị thiếu cân.")
                elif bmi < 25:
                    print("  Bạn có cân nặng bình thường.")
                elif bmi < 30:
                    print("  Bạn đang thừa cân.")
                elif bmi < 35:
                    print("  Bạn bị béo phì cấp độ I.")
                elif bmi < 40:
                    print("  Bạn bị béo phì cấp độ II.")
                else:
                    print("  Bạn bị béo phì cấp độ III (nguy hiểm).")

            elif a == "3":
                while True:
                    print("\n┌" + "─" * 14 + "┐")
                    print("│{:^14}│".format("PHÉP TÍNH"))
                    print("├" + "─" * 14 + "┤")
                    print("│ {:<10}│".format(" 0. Thoát    "))
                    print("│ {:<10}│".format(" 1. Cộng (+) "))
                    print("│ {:<10}│".format(" 2. Trừ (-)  "))
                    print("│ {:<10}│".format(" 3. Nhân (x) "))
                    print("│ {:<10}│".format(" 4. Chia (÷) "))
                    print("└" + "─" * 14 + "┘")

                    phep_tinh = input("nhập lựa chọn(0,1,2,3,4): ")

                    if phep_tinh == "1":
                        print("Phép cộng! ")
                        try:
                            mot = float(input("số thứ nhất: "))
                            hai = float(input("Nhập số thứ hai: "))
                            print(f"{mot} + {hai} = {mot+hai}")
                        except ValueError:
                            print("Nhập không hợp lệ hãy nhập số. ")

                    elif phep_tinh == "2":
                        print("Phép trừ! ")
                        try:
                            mot = float(input("số thứ nhât: "))
                            hai = float(input("Nhập số thứ hai: "))
                            print(f"{mot} - {hai} = {mot-hai}")
                        except ValueError:
                            print("Không hợp lệ.")                   

                    elif phep_tinh == "3":
                        print("Phép nhân! ")
                        try:
                            mot = float(input("số thứ nhất: "))
                            hai = float(input("Nhập số thứ hai: "))
                            print(f"{mot} x {hai} = {mot*hai}")
                        except ValueError:
                            print("Không hợp lệ.")

                    elif phep_tinh == "4":
                        print("Phép chia! ")
                        try:
                            mot = float(input("số thứ nhất: "))
                            hai = float(input("Nhập số thứ hai: "))
                            print(f"{mot} ÷ {hai} = {mot/hai}")
                        except ValueError:
                            print("Không hợp lệ.")
                        except ZeroDivisionError:
                            print("Trong phép chia không thể chia cho (0).")

                    elif phep_tinh == "0":
                        print("Thoát phép tính.")
                        print("Máy tính có thể sai sót.")
                        break

                    else:
                        print("Lựa chọn không hợp lệ, vui lòng nhập lại.\n")

            
            elif a == "0":
                print("Thoát thành công! ")
                print("Đây là số liệu từ máy, có thể sai sót, và chưa được xác minh chính xác.")
                print("Bạn nên thăm khám tại các trung tâm ý tế được chuẩn đoán.")
                break
            
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại.\n")
        break
    elif a in exitx:
        print("Thoát. / Exit. ")
        exit()
    else:
        print("Wrong input, try again. / Nhập sai nhập lại.")
