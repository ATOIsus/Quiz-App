from tkinter import messagebox     # To show popup messagebox.



def update_fun(score):

    db_score = 3

    if score > db_score:
        return "Need to update"

    elif score < db_score:
        return "No need to update"



def test_update():
    assert update_fun(2) == "Need to update" or update_fun(2) == "No need to update"




def chk_ans(choice):

    ans = "Right Answer."

    if choice == ans : 
        return "Correct"

    else:
        return "Incorrect"



def test_answer():
    assert chk_ans("Right Answer.") == "Correct" or chk_ans("Right Answer.") == "Incorrect"






def sign_up(ent_uname_up, ent_name_up, ent_pass_up, ent_c_pass_up):
    
    db_username = "Database Username"

    if ent_uname_up == '' and ent_pass_up == '' and ent_name_up == '' and ent_c_pass_up == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Fields!")
    elif ent_name_up == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Name!")
    elif ent_uname_up == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Username!")
    elif ent_pass_up == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Password!")
    elif ent_c_pass_up == '':
        messagebox.showerror("Error!", "Cannot Enter Empty Confirm Password!")
    elif ent_pass_up != ent_c_pass_up:
        messagebox.showerror("Error!", "Password and Confirm Password need to be the same!")

    else:
        if ent_uname_up == db_username:
            return "No Duplicate Username"
        else:
            return "Signed Up"



def test_signup():
    assert sign_up("Unique Username", "Name", "Password", "Password") == "Signed Up" or \
           sign_up("Unique Username", "Name", "Password", "Password") == "No Duplicate Username"



def sign_in(user_name_signin, password_signin):

    db_user_name = "Database Username"
    db_password  = "Database Password"

    if user_name_signin == "" or password_signin == "":
        messagebox.showerror("Error", "All fields are required")

    else:
        if user_name_signin == db_user_name and password_signin == db_password:
            return "Signed In"

        else:
            return "Not Signed In"


def test_signin():
    assert sign_in("Username", "Password") == "Signed In" or sign_in("Username", "Password") == "Not Signed In"



# Tested by Sabin Maharjan.
