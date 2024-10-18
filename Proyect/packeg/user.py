
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class User  :
    def __init__(self , username , passowrd):
        self.username = username
        self.password = passowrd
    @property
    def username(self):
        return self._username  


    @username.setter
    def username(self, value):
        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def check_Pasword (self , user , pswd):
        success = (user == self.username and pswd == self.password)
        if not success:
            messagebox.showerror(title="Loging Error",message="Please Check your password or Username")
        else:
            messagebox.showinfo(title="Loging Success",message="Success Full")
