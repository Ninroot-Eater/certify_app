import csv
import json
from PIL import Image, ImageDraw, ImageFont

# there are 5 types of  certificates (brief description)

# 1: "Big kid monthly certificate"
# the kind that's made for KET, PET, FCE and CAE classes after each month.

# 2: "Small kid monthly certificate (normal)"
# the kind that's made for Starters, Movers and Flyers classes after each month.

# 3: "Small kid monthly certificate (TOR)"
# the kind that's like type 2, but a TOR.

# 4: "Award certificate (normal)"
# the kind that's made for every class. It's with a title in the middle (no marks).

# 5: "Award certificate (Academic Excellence)"
# the kind that's like type 4, but for academic excellence.

# ** type 4 and 5 are combined to class type4


# setting up the fonts
fonts1 = {"font0":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=55),
         "font1": ImageFont.truetype('fonts/LibreBaskerville-Regular.ttf',size=80),
         "font2":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=60),
         "font3":ImageFont.truetype("fonts/LibreBaskerville-Bold.ttf", size=60),
         "font4":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=50),
         "font5":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=45)}

fonts4 = {"font0":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=45),
         "font1": ImageFont.truetype('fonts/LoveloBlack.otf',size=40),
         "font2":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=20),
         "font3":ImageFont.truetype("fonts/LibreBaskerville-Bold.ttf", size=20)}

fonts2 = {"font0":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=100),
         "font1": ImageFont.truetype('fonts/LoveloBlack.otf',size=90),
         "font2":ImageFont.truetype("fonts/Lato-Regular.ttf", size=50),
         "font3":ImageFont.truetype("fonts/LibreBaskerville-Bold.ttf", size=45)}

fonts3 = {"font0":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=55),
         "font1": ImageFont.truetype('fonts/LoveloBlack.otf',size=90),
         "font2":ImageFont.truetype("fonts/Lato-Regular.ttf", size=50),
         "font3":ImageFont.truetype("fonts/LibreBaskerville-Bold.ttf", size=45)}

fonts6 = {"font0":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=65),
          "font1":ImageFont.truetype("fonts/LibreBaskerville-Bold.ttf", size=65),
          "font2":ImageFont.truetype("fonts/LibreBaskerville-Regular.ttf", size=75)
          }


# the colors
colors = {"black": "rgb(0, 0, 0)", "name_blue": "rgb(25, 27, 109)", "red": "rgb(210,19,26)"}

# title mapper
his_or_her = {"male":"his", "female":"her"}

# gender list
gender_lst = ["male","female"]


def input_dic_creator(jsonf):
    return json.loads(open(jsonf,"r").read())


class Type1:

    exam_info_dict = {"KET": {"real total": 150,
                              "txt1": "International Entry (Key)*",
                              "txt2": "Key English Test",
                              "txt3": " Level A2",
                              "mrk_dic":{"Grade A":(140,151),"Grade B":(133,140),"Grade C":(120,133),"Level A1":(100,120)}
                              },

                      "PET": {"real total": 170,
                              "txt1": "International Entry (Preliminary)*",
                              "txt2": "Preliminary English Test",
                              "txt3": " Level B1",
                              "mrk_dic":{"Grade A":(160,171),"Grade B":(150,160),"Grade C":(140,150),"Level A1":(120,140)}},

                      "FCE": {"real total": 190,
                              "txt1": "International Entry (First)*",
                              "txt2": "First Certificate in English",
                              "txt3": " Level B2",
                              "mrk_dic":{"Grade A":(180,191),"Grade B":(173,180),"Grade C":(160,173),"Level A1":(140,160)}},

                      "CAE": {"real total": 210,
                              "txt1": "International Entry (Advanced)*",
                              "txt2": "Certificate in Advanced English",
                              "txt3": " Level C1",
                              "mrk_dic": {"Grade A": (200, 211), "Grade B": (193, 200), "Grade C": (180, 193), "Level A1": (160, 180)}}
                      }

    def __init__(self, std_name: str, std_l: float, std_r: float,  std_w:float,std_s: float,
                 level: str, cls_tr: str, t_l: float, t_r: float,t_w:float, t_s: float,minus_rule=False):

        self.std_name = std_name
        self.std_r = std_r
        self.std_l = std_l
        self.std_w = std_w
        self.std_s = std_s
        self.level = level
        self.cls_tr = cls_tr
        self.t_r = t_r
        self.t_l = t_l
        self.t_w = t_w
        self.t_s = t_s
        self.minus_rule = minus_rule

        self.cert = Image.open(f"templates\\type1temp.png")
        self.sign = Image.open(f"signs2\\{cls_tr}.png")
        self.current = self.exam_info_dict[self.level]

        self.state = True
        for i in [self.std_r, self.std_l, self.std_s,self.std_w, self.t_r, self.t_l, self.t_s,self.t_w]:
            try:
                float(i)
            except TypeError or ValueError:
                self.state = False

    def image_size(self):
        return self.cert.size

    def mark_calc(self):
        std_lst = [self.std_l,self.std_r,self.std_w,self.std_s]
        t_lst = [self.t_l,self.t_r,self.t_w,self.t_s]

        rt_lst = []
        if self.minus_rule == False:
            for i in range(4):
                rt_lst.append((self.current['real total'] / t_lst[i]) * std_lst[i])

        else:
            for i in range(4):
                rt_lst.append(self.current['real total'] - int(( int(t_lst[i]) - int(std_lst[i]))))

        return_lst = []
        return_lst.append(abs(sum(rt_lst)/4))
        grade = ""
        for j in self.current['mrk_dic'].keys():
            if int(abs(sum(rt_lst)/4)) in range(self.current['mrk_dic'][j][0],self.current['mrk_dic'][j][1]):
                grade = j

            else:
                return f"{self.std_name}: Marks too low to receive a certificate."

        return_lst = return_lst + rt_lst
        rt_lst = []
        title_lst = ['Overall Score',"Listening","Reading","Writing","Speaking"]
        for i in range(5):
            rt_lst.append(title_lst[i]+"   "+str(int(abs(return_lst[i]))))

        return {"grade":grade,"lst":rt_lst}


    def place_txt(self, txt: str, font: str, y_pos: int, color: str, x_pos=None):

        txt_size = fonts1[font].getsize(txt)
        if x_pos is None:
            x_pos = ((self.image_size()[0] - txt_size[0]) / 2) + (txt_size[0] / 2)

        draw = ImageDraw.Draw(self.cert)
        draw.text((x_pos, y_pos), txt, fill=colors[color], font=fonts1[font], anchor="ma")

    def place_sign(self):
        self.cert.paste(self.sign, (1870, 2870))
        txt = "Teacher " + self.cls_tr[0].upper() + self.cls_tr[1:-1] + self.cls_tr[-1]
        self.place_txt(txt, "font5", 3210, "black", 2000)

    def create(self):

        if self.state == True:
            try:
                self.place_txt("Cambridge English Entry Level Certificate in ESOL","font0",1000,"black")
                self.place_txt(f"{self.current['txt1']}", "font0", 1085, "black")

                self.place_txt(f"{self.std_name}","font1",1350,"name_blue")


                self.place_txt(f"{self.current['txt2']}","font3",1825,"black")

                txt="Council of Europe"
                txt_size = fonts1["font2"].getsize(txt)
                self.place_txt(f"Council of Europe", "font2", 1940, "black",((self.image_size()[0] - txt_size[0]) / 2)+50)
                self.place_txt(f"{self.current['txt3']}", "font2", 1940, "red",
                               ((self.image_size()[0] - txt_size[0]) / 2) + (txt_size[0] / 2) +200)

                if type(self.mark_calc()) != type({1:1}):
                    return self.mark_calc()

                self.place_txt(f"{self.mark_calc()['grade']}", "font3", 1625, "black")
                st_ypos = 2200
                y_inerval = 125
                self.place_txt(self.mark_calc()['lst'][0], "font3", st_ypos, "black")
                st_ypos += y_inerval


                for i in self.mark_calc()["lst"][1:len(self.mark_calc()["lst"])]:
                    self.place_txt(i,"font2",st_ypos,"black")
                    st_ypos+=y_inerval

                self.place_sign()

                self.cert.save(f"certificates\\t1CERT{self.std_name}.png")
                return f"Certificate successfully created for {self.std_name}"

            except IndexError:
                return f"Error in {self.std_name}"
        else:
            return f"Error in {self.std_name}"

    @staticmethod
    def create_dic(csvfile, input_dic):
        rt_dic = {}
        with open(csvfile, "r") as f:
            gen_obj = csv.reader(f)
            lst = []

            # append everything in the generator object into a list, so that it can be iterated more than once.
            for line in gen_obj:
                lst.append(line)

            c = 0
            for line in lst:
                str_c = str(c)
                while len(str(str_c)) < 3:
                    str_c = "0" + str_c
                rt_dic[f'{line[0]}{str_c}'] = (line[0], line[1], line[2], line[3],line[4], input_dic['level'],
                                               input_dic['class_tr'], input_dic['t_l'],
                                               input_dic['t_r'],input_dic['t_w'], input_dic['t_s'],input_dic['minus_rule'])
                c += 1

        return rt_dic


class Type4:

    def __init__(self,awd_title:str,des:str,std_name:str,giv_date:str,cls_name:str,gender:str,cls_tr:str):

        self.awd_title = awd_title
        self.des = des
        self.std_name = std_name
        self.giv_date = giv_date
        self.cls_name = cls_name
        self.gender = gender
        self.cls_tr = cls_tr

        self.cert = Image.open(f"templates\\type4temp.png")
        self.sign = Image.open(f"signs4\\{cls_tr}.png")

    def date_str(self):
        try:
            temp = [f"Given this on {self.giv_date},",f"for {his_or_her[self.gender]} excellence in {self.cls_name}"]
        except KeyError:
            temp = []
        return temp

    def image_size(self):
        return self.cert.size

    def place_txt(self,txt:str,font:str,y_pos:int,color:str,x_pos=None):

        txt_size = fonts4[font].getsize(txt)
        if x_pos is None:
            x_pos = ((self.image_size()[0] - txt_size[0]) / 2) + (txt_size[0]/2)

        draw = ImageDraw.Draw(self.cert)
        draw.text((x_pos,y_pos),txt,fill=colors[color],font=fonts4[font],anchor="ma")

    def place_sign(self):
        self.cert.paste(self.sign,(720,550))
        txt = "Teacher "+self.cls_tr[0].upper() + self.cls_tr[1:-1] + self.cls_tr[-1]
        self.place_txt(txt,"font3",695,"black",783)

    def create(self):
        try:
            if self.des == "":
                self.place_txt(self.awd_title, "font0", 250, "red")
            else:
                self.place_txt(self.awd_title, "font0", 225, "red")
                self.place_txt(self.des, "font2", 285, "red")

            self.place_txt(self.std_name, "font1", 390, "name_blue")
            self.place_txt(self.date_str()[0], "font2", 440, "black")
            self.place_txt(self.date_str()[1], "font2", 462, "black")

            self.place_sign()

            save_name = ""
            for i in self.std_name.split():
                save_name += i
            self.cert.save(f"certificates\\t4CERT{save_name}.png")
            return f"Certificate successfully created for {self.std_name}."
        except IndexError:
            return f"Error in {self.std_name}."

    def __repr__(self):
        return f"Type4('{self.awd_title}','{self.des}','{self.std_name}'," \
               f"'{self.giv_date}','{self.cls_name}','{self.gender}','{self.cls_tr}')"

    @staticmethod
    def create_dic(csvfile,input_dic):
        rt_dic = {}
        with open(csvfile,"r") as f:
            gen_obj = csv.reader(f)
            lst = []

            # append everything in the generator object into a list, so that it can be iterated more than once.
            for line in gen_obj:
                lst.append(line)

            # check if there are faulty data
            # in the case of Type4, only gender needs to be checked
            for line in lst:
                line[3] = line[3].lower()
                if line[3] not in gender_lst:
                    line[3] = "ERROR"

            c = 0
            for line in lst:
                str_c = str(c)
                while len(str(str_c)) <3:
                    str_c = "0" + str_c
                rt_dic[f'{line[2]}{str_c}'] = (line[0],line[1],line[2],input_dic['date'],
                                               input_dic['class_name'],line[3],input_dic['class_tr'])
                c+=1

        return rt_dic


class Type2:

    marking_sys = {"Starters":[25,10,15],
                   "Movers":[40,25,15],
                   "Flyers":[40,25,15]}

    def __init__(self,std_name:str,std_rw:float,std_l:float,std_s:float,
                 level:str,date:str,cls_tr:str,t_rw:float,t_l:float,t_s:float):

        self.std_name = std_name
        self.std_rw = std_rw
        self.std_l = std_l
        self.std_s = std_s
        self.level = level
        self.date = date
        self.cls_tr = cls_tr
        self.t_rw = t_rw
        self.t_l = t_l
        self.t_s = t_s

        self.cert = Image.open(f"templates\\type2temp.png")
        self.sign = Image.open(f"signs2\\{cls_tr}.png")
        self.shield = Image.open(f"shield.png")
        self.shadow = Image.open(f"shadow.png")

        self.state = True
        for i in [self.std_rw,self.std_l,self.std_s,self.t_rw,self.t_l,self.t_s]:
            try:
                float(i)
            except TypeError:
                self.state = False

    def image_size(self):
        return self.cert.size

    def date_str(self):
        return [f"took YLE {self.level} at Teacher Su Language Center", f"in {self.date}"]

    def place_txt(self,txt:str,font:str,y_pos:int,color:str,x_pos=None):

        txt_size = fonts2[font].getsize(txt)
        if x_pos is None:
            x_pos = ((self.image_size()[0] - txt_size[0]) / 2)+ (txt_size[0]/2)

        draw = ImageDraw.Draw(self.cert)
        draw.text((x_pos,y_pos),txt,fill=colors[color],font=fonts2[font],anchor="ma")

    def place_sign(self):
        self.cert.paste(self.sign,(1870,2870))
        txt = "Teacher "+self.cls_tr[0].upper() + self.cls_tr[1:-1] + self.cls_tr[-1]
        self.place_txt(txt,"font3",3210,"black",2000)

    def shield_calc(self):
        t_lst = [self.t_rw,self.t_l,self.t_s]
        std_lst = [self.std_rw,self.std_l,self.std_s]

        result_lst = []
        for i in range(3):
            result_lst.append((self.marking_sys[self.level][i]/float(t_lst[i]))*float(std_lst[i]))

        rt_lst = []
        for i in range(3):
            denominator = self.marking_sys[self.level][i]/5
            if result_lst[i]%denominator != 0:
                rt_lst.append((result_lst[i]//denominator)+1)
            elif result_lst[i]%denominator == 0:
                rt_lst.append(result_lst[i] // denominator)
        return rt_lst

    def place_sheield(self):

        starting_pos_x = 800
        starting_pos_y = 2000

        x_interval = 225
        y_interval = 250

        for i in self.shield_calc():
            for sh in range(int(i)):
                self.cert.paste(self.shield,(starting_pos_x,starting_pos_y))
                starting_pos_x += x_interval
            for sh in range(int(5-i)):
                self.cert.paste(self.shadow,(starting_pos_x,starting_pos_y))
                starting_pos_x += x_interval
            starting_pos_x = 800
            starting_pos_y += y_interval

        starting_pos_y = 2080
        self.place_txt("Reading & Writing","font3",starting_pos_y,"black",550)
        starting_pos_y += y_interval
        self.place_txt("Listening", "font3", starting_pos_y, "black", 550+(fonts2['font3'].getsize("Reading & Writing")[0]/4))
        starting_pos_y += y_interval
        self.place_txt("Speaking", "font3", starting_pos_y, "black", 550+(fonts2['font3'].getsize("Reading & Writing")[0]/4))

    def create(self):

        if self.state == True:
            try:
                self.place_txt(self.level, "font0", 1000, "red")
                self.place_txt(self.std_name, "font1", 1250, "name_blue")
                self.place_sign()
                self.place_txt(self.date_str()[0], "font2", 1450, "black")
                self.place_txt(self.date_str()[1], "font2", 1530, "black")
                self.place_sheield()

                self.cert.save(f"certificates\\t2CERT{self.std_name}.png")
                return f"Certificate successfully created for {self.std_name}"

            except IndexError:
                return f"Error in {self.std_name}"
        else:
            return f"Error in {self.std_name}"
        
    @staticmethod
    def create_dic(csvfile, input_dic):
        rt_dic = {}
        with open(csvfile, "r") as f:
            gen_obj = csv.reader(f)
            lst = []

            # append everything in the generator object into a list, so that it can be iterated more than once.
            for line in gen_obj:
                lst.append(line)

            c = 0
            for line in lst:
                str_c = str(c)
                while len(str(str_c)) < 3:
                    str_c = "0" + str_c
                rt_dic[f'{line[0]}{str_c}'] = (line[0], line[1], line[2], line[3],input_dic['level'],
                                               input_dic['date'],input_dic['class_tr'],
                                               input_dic['t_rw'],input_dic['t_l'],input_dic['t_s'])
                c += 1

        return rt_dic


class Type3:

    def __init__(self, std_name: str, std_rw: float, std_l: float, std_s: float,
                 level: str, date: str, cls_tr: str, t_rw: float, t_l: float, t_s: float):

        self.std_name = std_name
        self.std_rw = std_rw
        self.std_l = std_l
        self.std_s = std_s
        self.level = level
        self.date = date
        self.cls_tr = cls_tr
        self.t_rw = t_rw
        self.t_l = t_l
        self.t_s = t_s

        self.cert = Image.open(f"templates\\type3temp.png")
        self.sign = Image.open(f"signs2\\{cls_tr}.png")

        self.state = True
        for i in [self.std_rw, self.std_l, self.std_s, self.t_rw, self.t_l, self.t_s]:
            try:
                i = float(i)
            except TypeError:
                self.state = False

    def image_size(self):
        return self.cert.size

    def place_txt(self, txt: str, font: str, y_pos: int, color: str, x_pos=None):

        txt_size = fonts3[font].getsize(txt)
        if x_pos is None:
            x_pos = ((self.image_size()[0] - txt_size[0]) / 2)

        draw = ImageDraw.Draw(self.cert)
        draw.text((x_pos, y_pos), txt, fill=colors[color], font=fonts3[font], anchor="la")

    def place_sign(self):
        self.cert.paste(self.sign, (1870, 2770))
        txt = "Teacher " + self.cls_tr[0].upper() + self.cls_tr[1:-1] + self.cls_tr[-1]
        txt_size = fonts3["font3"].getsize(txt)
        self.place_txt(txt, "font3", 3100, "black", ((self.image_size()[0] - txt_size[0] +1500) / 2))

    def create(self):

        if self.state == True:
            try:
                self.place_txt(f"{self.level} Test Report Form","font3",900,"black")
                txt = "Candidate's Name:"
                self.place_txt(txt, "font0",1200, "red", 350)
                self.place_txt(f"{self.std_name}", "font0", 1200, "black", 370 + fonts3['font0'].getsize(txt)[0] )

                starting_y_pos = 1650
                y_interval = 230
                gap = 20

                txt = "Reading&Writing:"
                self.place_txt(txt, "font0", starting_y_pos, "red", 350)
                self.place_txt(f"{self.std_rw}\\{self.t_rw}", "font0", starting_y_pos, "black",
                               370 + fonts3['font0'].getsize(txt)[0] +gap)
                starting_y_pos+=y_interval

                txt = "Listening:"
                self.place_txt(txt, "font0", starting_y_pos, "red", 867-fonts3['font0'].getsize(txt)[0])
                self.place_txt(f"{self.std_l}\\{self.t_l}", "font0", starting_y_pos, "black",
                               867 - fonts3['font0'].getsize(txt)[0] + fonts3['font0'].getsize(txt)[0] + gap)
                starting_y_pos += y_interval

                txt = "Speaking:"
                self.place_txt(txt, "font0", starting_y_pos, "red", 867 - fonts3['font0'].getsize(txt)[0])
                self.place_txt(f"{self.std_s}\\{self.t_s}", "font0", starting_y_pos, "black",
                               867 - fonts3['font0'].getsize(txt)[0] + fonts3['font0'].getsize(txt)[0] + gap)
                starting_y_pos += y_interval

                txt = "Overall score:"
                self.place_txt(txt, "font0", starting_y_pos, "red", 867 - fonts3['font0'].getsize(txt)[0])
                self.place_txt(f"{int(abs(sum([float(i) for i in [self.std_l,self.std_s,self.std_rw]])))}"
                               f"\\{int(abs(sum([float(i) for i in [self.t_l,self.t_s,self.t_rw]])))}",
                               "font0", starting_y_pos, "black",
                               867 - fonts3['font0'].getsize(txt)[0] + fonts3['font0'].getsize(txt)[0] +gap)
                starting_y_pos += y_interval

                txt = "Date:"
                self.place_txt(txt, "font0", starting_y_pos, "black", 867 - fonts3['font0'].getsize(txt)[0])
                self.place_txt(f"{self.date}",
                               "font0", starting_y_pos, "black",
                               867 - fonts3['font0'].getsize(txt)[0] + fonts3['font0'].getsize(txt)[0] + gap)
                starting_y_pos += y_interval

                self.place_sign()

                self.cert.save(f"certificates\\t3CERT{self.std_name}.png")
                return f"Certificate successfully created for {self.std_name}"

            except IndexError:
                return f"Error in {self.std_name}"
        else:
            return f"Error in {self.std_name}"

    @staticmethod
    def create_dic(csvfile, input_dic):
        rt_dic = {}
        with open(csvfile, "r") as f:
            gen_obj = csv.reader(f)
            lst = []

            # append everything in the generator object into a list, so that it can be iterated more than once.
            for line in gen_obj:
                lst.append(line)

            c = 0
            for line in lst:
                str_c = str(c)
                while len(str(str_c)) < 3:
                    str_c = "0" + str_c
                rt_dic[f'{line[0]}{str_c}'] = (line[0], line[1], line[2], line[3], input_dic['level'],
                                               input_dic['date'], input_dic['class_tr'],
                                               input_dic['t_rw'], input_dic['t_l'], input_dic['t_s'])
                c += 1

        return rt_dic


class Type6:

    def __init__(self, std_name: str, std_l: float, std_r: float, std_w: float, std_s:float, std_o:float,
                 date:str):

        self.std_name = std_name
        self.std_l = std_l
        self.std_r = std_r
        self.std_w = std_w
        self.std_s = std_s
        self.std_o = std_o
        self.date = date

        self.cert = Image.open(f"templates\\type6temp.png")

        self.state = True

        for i in [self.std_l, self.std_r, self.std_w, self.std_s]:
            try:
                i = float(i)
            except TypeError:
                self.state = False

    def image_size(self):
        return self.cert.size

    def place_txt(self, txt1: str, txt2:str, font: str, y_pos: int, color: str, x_pos):



        draw = ImageDraw.Draw(self.cert)
        draw.text((x_pos - 100, y_pos), txt1, fill=colors[color], font=fonts6[font], anchor="rm")
        draw.text((x_pos - 30, y_pos), " - ", fill=colors[color], font=fonts6[font], anchor="mm")
        draw.text((x_pos +30, y_pos), txt2, fill=colors[color], font=fonts6[font], anchor="lm")

    def create(self):

        if self.state == True:
            try:

                self.place_txt("Candidate's Name",self.std_name,"font2",1200,"black",1000)

                st_ypos = 1700
                y_inter = 200

                title_lst = ["Listening", "Reading","Writing","Speaking"]
                band_lst = [self.std_l,self.std_r,self.std_w,self.std_s]

                for i in range(4):
                    self.place_txt(title_lst[i],str(band_lst[i]),"font0",st_ypos,'black',900)
                    st_ypos += y_inter

                self.place_txt("Overall Band Score",str(self.std_o),"font1",st_ypos,"black",900)
                self.place_txt("Date",self.date,"font0",st_ypos+270,"black",450)


                self.cert.save(f"certificates\\t6CERT{self.std_name}.png")
                return f"Certificate successfully created for {self.std_name}"

            except IndexError:
                return f"Error in {self.std_name}"
        else:
            return f"Error in {self.std_name}"

    @staticmethod
    def create_dic(csvfile, input_dic):
        rt_dic = {}
        with open(csvfile, "r") as f:
            gen_obj = csv.reader(f)
            lst = []

            # append everything in the generator object into a list, so that it can be iterated more than once.
            for line in gen_obj:
                lst.append(line)

            c = 0
            for line in lst:
                str_c = str(c)
                while len(str(str_c)) < 3:
                    str_c = "0" + str_c
                rt_dic[f'{line[0]}{str_c}'] = (line[0], line[1], line[2], line[3], line[4],line[5],input_dic['date'])
                c += 1

        return rt_dic

type_dic = {"Type4":Type4, "Type2":Type2, "Type3":Type3, "Type1":Type1, "Type6":Type6}

#x = Type6("Thiha Swan Htet",9.0,8.5,7.0,6.5,8.0, "August 2020").create()


def main(jsonfile,csvfile):
    indic = input_dic_creator(jsonfile)
    dic = type_dic[indic['type']].create_dic(csvfile, indic)
    rt_lst = []
    for i in dic.values():
        rt_lst.append(eval(f"{indic['type']}{i}").create())
    return rt_lst

