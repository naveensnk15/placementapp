from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRoundFlatButton
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang.builder import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.clock import mainthread
import requests
import json
import threading
import pyrebase



help_str = """


ScreenManager:
    MainScreen:
    SecurityScreen:
    LoginAdminScreen:
    LoginUserScreen:
    SignupAdminScreen:
    SignupUserScreen:
    AdminScreen:
    Admin1Screen:
    User1Screen:
    RootLayout:
    

<MainScreen>:
    name: 'main'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"
    MDLabel:
        text: '  Placement  '
        halign: 'center'
        font_size : 45
        theme_text_color: "Error"



    MDRectangleFlatButton:
        text: 'Admin'
        pos_hint: {'x':0.35,'y':0.3}
        font_size: '25'
        on_press: root.manager.current = 'security'

    MDRectangleFlatButton:
        text: 'User'
        font_size: '25'
        pos_hint: {'x':0.55,'y':0.3}
        on_press: root.manager.current = 'loginuser'

<SecurityScreen>:
    name: 'security'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"

            MDTextFieldRound:
                id: security_code
                hint_text : "code"
                password: True
                password_mask: '*'

                icon_right : "eye-off"
                size_hint_x : None
                width : 220
                font_size : 20
                color_active : [1,1,1,1]
                pos_hint : {"center_x":.5}

            MDRoundFlatButton:
                text : 'GO'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press:
                    app.security()



<LoginAdminScreen>:
    name: 'loginadmin'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"

            MDLabel:
                text : 'Sign In'
                font_style : 'Button'
                font_size : 45
                halign : "center"
                size_hint_y : None
                height : self.texture_size[1]
                padding_y : 15

            MDTextFieldRound:
                id: login_email
                hint_text : "Email-Id"
                icon_right : "account"
                size_hint_x : None
                width : 220
                font_size : 20
                color_active : [1,1,1,1]
                pos_hint : {"center_x":.5}

            MDTextFieldRound:
                id: login_password
                hint_text : "Password"
                password: True
                password_mask: '*'
                icon_right : "eye-off"
                size_hint_x : None
                width : 220
                font_size : 20
                color_active : [1,1,1,1]
                pos_hint : {"center_x":.5}

            MDRoundFlatButton:
                text : 'Login'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press: 
                    app.adminlogin()

            Widget:
                size_hint_y : None
                height : 30

            MDRoundFlatButton:
                text : 'Create an Account'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press: root.manager.current = 'signupadmin'
            Widget:
                size_hint_y : None
                height : 30


<LoginUserScreen>:
    name: 'loginuser'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"

            MDLabel:
                text : 'Sign In'
                font_style : 'Button'
                font_size : 45
                halign : "center"
                size_hint_y : None
                height : self.texture_size[1]
                padding_y : 15


            MDTextFieldRound:
                id: login_email
                hint_text : "Email-Id"
                icon_right : "account"
                size_hint_x : None
                width : 220
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDTextFieldRound:
                id: login_password
                hint_text : "Password"
                password: True
                password_mask: '*'
                icon_right : "eye-off"
                size_hint_x : None
                width : 220
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDRoundFlatButton:
                text : 'Login'
                pos_hint : {"center_x":.5}
                font_size : 15
                on_press:
                    app.userlogin()

            Widget:
                size_hint_y : None
                height : 30

            MDRoundFlatButton:
                text : 'Create an Account'
                pos_hint : {"center_x":.5}
                font_size : 15
                on_press: root.manager.current = 'signupuser' 
            Widget:
                size_hint_y : None
                height : 30

<SignupAdminScreen>:
    name: 'signupadmin'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"

            MDLabel:
                text : 'Sign Up'
                font_style : 'Button'
                font_size : 40
                halign : "center"
                size_hint_y : None
                height : self.texture_size[1]
                padding_y : 20
            MDTextFieldRound:
                id: signup_username
                hint_text : "UserName"
                icon_right : "account"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDTextFieldRound:
                id: signup_email
                hint_text : "Email Id"
                icon_right : "account"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDTextFieldRound:
                id: signup_password
                hint_text : "Password"
                password: True
                password_mask: '*'
                icon_right : "eye-off"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]

            MDRoundFlatButton:
                text : 'Create'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press:
                    app.adminsignup() 
            Widget:
                size_hint_y : None
                height : 30

<SignupUserScreen>:
    name: 'signupuser'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"

            MDLabel:
                text : 'Sign Up'
                font_style : 'Button'
                font_size : 40
                halign : "center"
                size_hint_y : None
                height : self.texture_size[1]
                padding_y : 20
            MDTextFieldRound:
                id: signup_username
                hint_text : "UserName"
                icon_right : "account"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDTextFieldRound:
                id: signup_email
                hint_text : "Email Id"
                icon_right : "account"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDTextFieldRound:
                id: signup_password
                hint_text : "Password"
                password: True
                password_mask: '*'
                icon_right : "eye-off"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]

            MDRoundFlatButton:
                text : 'Create'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press:
                    app.usersignup() 
            Widget:
                size_hint_y : None
                height : 30

<AdminScreen>:
    name: 'admin'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 620,580
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"


            MDTextFieldRound:
                id: info_electrical
                hint_text : "Electrical"
                multiline: 'true'
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDIconButton:
                icon: "android"
                pos_hint: {'x':.6,'y':.1}
                on_press: app.electrical()

            MDTextFieldRound:
                id: info_electronics
                hint_text : "Electronics"
                multiline: 'true'
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDIconButton:
                icon: "android"
                pos_hint: {'x':.6,'y':.2}
                on_press: app.electronics()

            MDTextFieldRound:
                id: info_software
                hint_text : "Software"
                multiline: 'true'
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDIconButton:
                icon: "android"
                pos_hint: {'x':.6,'y':.2}
                on_press: app.software()

            MDTextFieldRound:
                id: info_dataanalytics
                hint_text : "Data Analytics"
                multiline: 'true'
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]
            MDIconButton:
                icon: "android"
                pos_hint: {'x':.6,'y':.2}
                on_press: app.dataanalytics()

        MDRoundFlatButton:
            text : 'submit'
            pos_hint : {"center_x":.5}
            font_size : 15 
            on_press: root.manager.current = 'admin1' 




<Admin1Screen>:
    name: 'admin1'
    
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"
            MDRoundFlatButton:
                text : 'Logout'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press: root.manager.current = 'main' 
            

           


<User1Screen>:
    name: 'user1'
    MDScreen :
        md_bg_color : [35/255,59/255,54/255,1]
        MDCard:
            size_hint : None,None
            size : 320,400
            pos_hint : {"center_x":.5,"center_y":.5}
            elevation : 15
            md_bg_color : [35/255,49/255,48/255,1]
            padding : 20
            spacing : 30
            orientation : "vertical"

            MDLabel:

                font_style : 'Button'
                font_size : 40
                halign : "center"
                size_hint_y : None
                height : self.texture_size[1]
                padding_y : 20
            MDTextFieldRound:
                id: user_cgpa
                hint_text : "CGPA"
                icon_right : "android"
                size_hint_x : None
                width : 280
                font_size : 20
                pos_hint : {"center_x":.5}
                color_active : [1,1,1,1]


            MDRoundFlatButton:
                text : 'Upload'
                pos_hint : {"center_x":.5}
                font_size : 15 
                on_press: app.cgpa()

<RootLayout>:
    table_box: table_box
    name: 'user2'
    MDLabel:
        pos_hint: {"center_x": .5, "top": 1}
        size_hint: .9, .1
        color: 0, 0, 0, 1
        text: "Data Table"
        halign: "center"
        font_style: "H3"
    MDBoxLayout:
        id: table_box
        pos_hint: {"center_x": .5, "top": .8}
        size_hint: .9, .6

    MDFillRoundFlatButton:
        text: "Update Table"
        pos_hint: {"center_x": .5, "top": .1}
        on_release: root.start_second_thread()




            







"""
TRIPS_SELECTED = []


class MainScreen(Screen):
    pass


class SecurityScreen(Screen):
    pass


class LoginAdminScreen(Screen):
    pass


class LoginUserScreen(Screen):
    pass


class SignupAdminScreen(Screen):
    pass


class SignupUserScreen(Screen):
    pass


class Admin1Screen(Screen):
    pass

class AdminScreen(Screen):
    pass


class User1Screen(Screen):
    pass

class RootLayout(Screen):
    stop = threading.Event()

    def start_second_thread(self):
        threading.Thread(target=self.load_data).start()

    def load_data(self, *args):
        if TRIPS_SELECTED:
            for n_trip in TRIPS_SELECTED:
                post_request = requests.delete(
                    f'https://mobileapp-30e40.firebaseio.com/{n_trip}.json')

        get_request = requests.get(f'https://mobileapp-30e40.firebaseio.com/.json')
        trips_data = json.loads(get_request.content.decode())

        count = 0
        cols = ['data']
        values = []

        for trip, data in trips_data.items():
            lista = []
            lista.append(trip)
            for key, info in data.items():
                lista.append(info)

                if count == 0:
                    cols.append(key)
            count += 1
            values.append(lista)

        self.update_table(cols, values)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''
        if current_row[0] in TRIPS_SELECTED:
            TRIPS_SELECTED.remove(current_row[0])
        else:
            TRIPS_SELECTED.append(current_row[0])

    @mainthread
    def update_table(self, cols, values):
        self.table_box.clear_widgets()

        self.data_table = MDDataTable(
            column_data=[(col, dp(28)) for col in cols],
            row_data=values,

        )

        self.data_table.bind(on_check_press=self.on_check_press)

        self.table_box.add_widget(self.data_table)







# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(SecurityScreen(name='security'))
sm.add_widget(LoginAdminScreen(name='loginadmin'))
sm.add_widget(LoginUserScreen(name='loginuser'))
sm.add_widget(SignupAdminScreen(name='signupadmin'))
sm.add_widget(SignupUserScreen(name='signupuser'))
sm.add_widget(AdminScreen(name='admin'))
sm.add_widget(Admin1Screen(name='admin1'))
sm.add_widget(User1Screen(name='user1'))
sm.add_widget(RootLayout(name='user2'))








class MyApp(MDApp):






    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url = "https://login-setup-df2e3.firebaseio.com/.json"
        self.url1= "https://mobileapp-30e40.firebaseio.com/.json"
        return self.strng
        return RootLayout



    def adminsignup(self):
        signupEmail = self.strng.get_screen('signupadmin').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupadmin').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupadmin').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url1, json=to_database)
            self.strng.get_screen('loginadmin').manager.current = 'loginadmin'

    auth1 = 'mHxQDwCNzGPMYCZnjMaJBJ9bTLS3fDniMOa03lUB'

    def adminlogin(self):
        loginEmail = self.strng.get_screen('loginadmin').ids.login_email.text
        loginPassword = self.strng.get_screen('loginadmin').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url1 + '?auth1=' + self.auth1)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('admin').manager.current = 'admin'
        else:
            print("user no longer exists")
            self.dialog = MDDialog(title='user no longer exists', size_hint=(0.7, 0.2))
            self.dialog.open()

    def usersignup(self):
        signupEmail = self.strng.get_screen('signupuser').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupuser').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupuser').ids.signup_username.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupUsername.split() == []:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Input', text='Please Enter a valid Input', size_hint=(0.7, 0.2),
                                   buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        if len(signupUsername.split()) > 1:
            cancel_btn_username_dialogue = MDFlatButton(text='Retry', on_release=self.close_username_dialog)
            self.dialog = MDDialog(title='Invalid Username', text='Please enter username without space',
                                   size_hint=(0.7, 0.2), buttons=[cancel_btn_username_dialogue])
            self.dialog.open()
        else:
            print(signupEmail, signupPassword)
            signup_info = str(
                {f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('loginuser').manager.current = 'loginuser'

    auth = 'aPppAFeCr1a4cI6HQ1c9BbyNNdvf84l2LJuebR1P'

    def userlogin(self):
        loginEmail = self.strng.get_screen('loginuser').ids.login_email.text
        loginPassword = self.strng.get_screen('loginuser').ids.login_password.text

        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')
        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:
            self.username = data[supported_loginEmail]['Username']
            self.login_check = True
            self.strng.get_screen('user1').manager.current = 'user1'
        else:
            print("user no longer exists")
            self.dialog = MDDialog(title='user no longer exists', size_hint=(0.7, 0.2))
            self.dialog.open()

    def security(self):
        securitycode = self.strng.get_screen('security').ids.security_code.text
        if securitycode.split() == ['s''w''e''e''e']:
            self.strng.get_screen('loginadmin').manager.current = 'loginadmin'

        if securitycode.split() == [] or securitycode.split() != ['s''w''e''e''e']:
            self.dialog = MDDialog(title='Invalid code', size_hint=(0.7, 0.2))
            self.dialog.open()

    def electrical(self):
        signupEmail = self.strng.get_screen('signupadmin').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupadmin').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupadmin').ids.signup_username.text
        electricalInfo = self.strng.get_screen('admin').ids.info_electrical.text

        if electricalInfo.split() == []:
            self.dialog = MDDialog(title='Invalid text', size_hint=(0.7, 0.2))
            self.dialog.open()
        else:
            print(electricalInfo)

    auth1 = 'mHxQDwCNzGPMYCZnjMaJBJ9bTLS3fDniMOa03lUB'

    def electronics(self):
        signupEmail = self.strng.get_screen('signupadmin').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupadmin').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupadmin').ids.signup_username.text
        electricalInfo = self.strng.get_screen('admin').ids.info_electrical.text
        electronicsInfo = self.strng.get_screen('admin').ids.info_electronics.text

        if electronicsInfo.split() == []:
            self.dialog = MDDialog(title='Invalid text', size_hint=(0.7, 0.2))
            self.dialog.open()
        else:
            print(electricalInfo, electronicsInfo)

    auth1 = 'mHxQDwCNzGPMYCZnjMaJBJ9bTLS3fDniMOa03lUB'

    def software(self):
        signupEmail = self.strng.get_screen('signupadmin').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupadmin').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupadmin').ids.signup_username.text
        electricalInfo = self.strng.get_screen('admin').ids.info_electrical.text
        electronicsInfo = self.strng.get_screen('admin').ids.info_electronics.text
        softwareInfo = self.strng.get_screen('admin').ids.info_software.text

        if softwareInfo.split() == []:
            self.dialog = MDDialog(title='Invalid text', size_hint=(0.7, 0.2))
            self.dialog.open()
        else:
            print(electricalInfo, electronicsInfo, softwareInfo)

    auth1 = 'mHxQDwCNzGPMYCZnjMaJBJ9bTLS3fDniMOa03lUB'

    def dataanalytics(self):
        signupEmail = self.strng.get_screen('signupadmin').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupadmin').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupadmin').ids.signup_username.text
        electricalInfo = self.strng.get_screen('admin').ids.info_electrical.text
        electronicsInfo = self.strng.get_screen('admin').ids.info_electronics.text
        softwareInfo = self.strng.get_screen('admin').ids.info_software.text
        dataanalyticsInfo = self.strng.get_screen('admin').ids.info_dataanalytics.text

        if dataanalyticsInfo.split() == []:
            self.dialog = MDDialog(title='Invalid text', size_hint=(0.7, 0.2))
            self.dialog.open()
        else:
            print(electricalInfo, electronicsInfo, softwareInfo, dataanalyticsInfo)
            signup_info = str(
                {
                    f'\"{signupEmail}\":{{"password":\"{signupPassword}\","username":\"{signupUsername}\","Electrical companydetails":\"{electricalInfo}\", "Electronics companydetails":\"{electronicsInfo}\", "Software companydetails":\"{softwareInfo}\", "Dataanalytics companydetails":\"{dataanalyticsInfo}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url1, json=to_database)

    auth1 = 'mHxQDwCNzGPMYCZnjMaJBJ9bTLS3fDniMOa03lUB'

    def cgpa(self):
        signupEmail = self.strng.get_screen('signupuser').ids.signup_email.text
        signupPassword = self.strng.get_screen('signupuser').ids.signup_password.text
        signupUsername = self.strng.get_screen('signupuser').ids.signup_username.text
        userCGPA = self.strng.get_screen('user1').ids.user_cgpa.text

        if userCGPA.split() == []:
            self.dialog = MDDialog(title='Invalid text', size_hint=(0.7, 0.2))
            self.dialog.open()
        else:
            print(userCGPA)
            signup_info = str(
                {
                    f'\"{signupEmail}\":{{"Password":\"{signupPassword}\","Username":\"{signupUsername}\","CGPA":\"{userCGPA}\"}}'})
            signup_info = signup_info.replace(".", "-")
            signup_info = signup_info.replace("\'", "")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url=self.url, json=to_database)
            self.strng.get_screen('user2').manager.current = 'user2'

    auth = 'aPppAFeCr1a4cI6HQ1c9BbyNNdvf84l2LJuebR1P'


MyApp().run()
