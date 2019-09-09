from tkinter import *
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import dataset
import threading

DB = dataset.connect("sqlite:///./mydb.db")
USER_INFO_TAB = DB["user_info"]
NICKNAME = "nickname"
FIRST_NAME = "first_name"
LAST_NAME = "last_name"
ZIP_CODE = "zip_code"
STATE = "state"
CITY = "city"
ADDRESS = "address"
PHONE = "phone"
MAIL = "mail"
PAY_TYPE = "pay_type"
CARD_NUMBER = "card_number"
CARD_LIMIT_MONTH = "card_limit_month"
CARD_LIMIT_YEAR = "card_limit_year"
CVV_NUMBER = "cvv_number"
PAYMENT_METHOD = "payment_method"
ORDER_ID_OR_NAME = "order_id_or_name"
RETURN_ACCOUNT = "return_account"
TWITTER_NAME = "twitter_name"
NOTE = "note"

TARGET_SITE_URL = "https://tayori.com/form/7016e619cfb10fdafa3027141cc75eec60dea703"
CHROME_DRIVER_PATH = "./chromedriver.exe"
HTML_FIRST_NAME_ID = '//*[@id="form-parts"]/div[1]/div/div/input'
HTML_LAST_NAME_ID = '//*[@id="form-parts"]/div[2]/div/div/input'
HTML_ZIP_CODE_ID = '//*[@id="form-parts"]/div[3]/div/div/input'
HTML_STATE_ID = '//*[@id="form-parts"]/div[4]/div/div/div/div/label/select'
HTML_CITY_ID = '//*[@id="form-parts"]/div[5]/div/div/input'
HTML_ADDRESS_ID = '//*[@id="form-parts"]/div[6]/div/div/input'
HTML_PHONE_ID = '//*[@id="form-parts"]/div[7]/div/div/input'
HTML_MAIL_ID = '//*[@id="form-parts"]/div[8]/div/div/input'
HTML_PAY_TYPE_ID = '//*[@id="form-parts"]/div[12]/div/div/div/div/label/select'
HTML_CARD_NUM_ID = '//*[@id="form-parts"]/div[13]/div/div/input'
HTML_CARD_LIM_MONTH_ID = '//*[@id="form-parts"]/div[14]/div/div/div/div/label/select'
HTML_CARD_LIM_YEAR_ID = '//*[@id="form-parts"]/div[15]/div/div/div/div/label/select'
HTML_CVV_NUM_ID = '//*[@id="form-parts"]/div[16]/div/div/input'
HTML_PAY_METHOD_ID = '//*[@id="form-parts"]/div[17]/div/div/div/div/label/select'
HTML_ORDER_ID_NAME_ID = '//*[@id="form-parts"]/div[18]/div/div/textarea'
HTML_RETURN_ACCOUNT_ID = '//*[@id="form-parts"]/div[19]/div/div/textarea'
HTML_TWITTER_ID = '//*[@id="form-parts"]/div[20]/div/div/input'
HTML_NOTE_ID = '//*[@id="form-parts"]/div[21]/div/div/textarea'

STATE_TUPLE = (
    "北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県",
    "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県",
    "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県",
    "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県",
    "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県"
)

PAY_TYPE_TUPLE = ("Visa", "American Express", "Mastercard", "JCB", "代金引換")
MONTH_TUPLE = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
YEAR_TUPLE = (18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)
PAY_METHOD_TUPLE = ("BASE支払い", "銀行振込")

BUTTON_STATE = "state"
BUTTON_ENABLED = "enbaled"
BUTTON_DISABLED = "disabled"
WM_DELETE_WINDOW = "WM_DELETE_WINDOW"


class UserInfo:
    def __init__(self):
        self.entry_nickname = None
        self.entry_first_name = None
        self.entry_last_name = None
        self.entry_zip_code = None
        self.box_state = None
        self.entry_city = None
        self.entry_address = None
        self.entry_phone = None
        self.entry_mail = None
        self.box_pay_type = None
        self.entry_card_number = None
        self.box_month = None
        self.box_year = None
        self.entry_cvv_number = None
        self.box_payment_method = None
        self.entry_order_id_or_name = None
        self.entry_return_account = None
        self.entry_twitter_name = None
        self.entry_note = None


class SitePasteThread(threading.Thread):
    def __init__(self, userinfo_rec):
        super(SitePasteThread, self).__init__()
        self.userinfo_rec = userinfo_rec

    def run(self):
        self.exec_selenium()

    def select_box(self, driver, html_id, target_val):
        try:
            Select(driver.find_element_by_xpath(html_id)).select_by_value(target_val)
        except:
            pass

    def exec_selenium(self):
        try:
            driver = webdriver.Chrome(CHROME_DRIVER_PATH)
            driver.get(TARGET_SITE_URL)

            driver.find_element_by_xpath(HTML_FIRST_NAME_ID).send_keys(self.userinfo_rec[FIRST_NAME])
            driver.find_element_by_xpath(HTML_LAST_NAME_ID).send_keys(self.userinfo_rec[LAST_NAME])
            driver.find_element_by_xpath(HTML_ZIP_CODE_ID).send_keys(self.userinfo_rec[ZIP_CODE])
            self.select_box(driver, HTML_STATE_ID, self.userinfo_rec[STATE])
            driver.find_element_by_xpath(HTML_CITY_ID).send_keys(self.userinfo_rec[CITY])
            driver.find_element_by_xpath(HTML_ADDRESS_ID).send_keys(self.userinfo_rec[ADDRESS])
            driver.find_element_by_xpath(HTML_PHONE_ID).send_keys(self.userinfo_rec[PHONE])
            driver.find_element_by_xpath(HTML_MAIL_ID).send_keys(self.userinfo_rec[MAIL])
            self.select_box(driver, HTML_PAY_TYPE_ID, self.userinfo_rec[PAY_TYPE])
            driver.find_element_by_xpath(HTML_CARD_NUM_ID).send_keys(self.userinfo_rec[CARD_NUMBER])
            self.select_box(driver, HTML_CARD_LIM_MONTH_ID, self.userinfo_rec[CARD_LIMIT_MONTH])
            self.select_box(driver, HTML_CARD_LIM_YEAR_ID, self.userinfo_rec[CARD_LIMIT_YEAR])
            driver.find_element_by_xpath(HTML_CVV_NUM_ID).send_keys(self.userinfo_rec[CVV_NUMBER])
            self.select_box(driver, HTML_PAY_METHOD_ID, self.userinfo_rec[PAYMENT_METHOD])
            driver.find_element_by_xpath(HTML_ORDER_ID_NAME_ID).send_keys(self.userinfo_rec[ORDER_ID_OR_NAME])
            driver.find_element_by_xpath(HTML_RETURN_ACCOUNT_ID).send_keys(self.userinfo_rec[RETURN_ACCOUNT])
            driver.find_element_by_xpath(HTML_TWITTER_ID).send_keys(self.userinfo_rec[TWITTER_NAME])
            driver.find_element_by_xpath(HTML_NOTE_ID).send_keys(self.userinfo_rec[NOTE])

            while True:
                tmp = driver.page_source
                sleep(2)
        except:
            print("OK")
            pass
        finally:
            driver.quit()


def get_select_nickname():
    global lb
    for i in lb.curselection():
        return lb.get(i)


def is_duplicate_record(nickname):
    rec = USER_INFO_TAB.find_one(nickname=nickname)
    return (rec is not None)


def popup_confirm_window(root, parent_frame, msg, is_ok):
    sub_w = Toplevel(root)
    sub_w.title("")
    sub_w.protocol(WM_DELETE_WINDOW, do_nothing)
    frame = ttk.Frame(sub_w, padding=10)
    frame.grid()
    label = Label(frame, text=msg)
    label.grid(row=0, column=0)
    if is_ok:
        button = Button(frame, text="OK", command=lambda: close_subwindow(root))
    else:
        button = Button(frame, text="OK", command=lambda: enable_parent_frame_and_destroy(parent_frame, root))
    button.grid()


def delete_insert(root, sub_w, parent_frame, old_nickname):
    global userinfo

    new_nickname = userinfo.entry_nickname.get()

    if len(new_nickname) == 0:
        popup_confirm_window(sub_w, parent_frame, "表示名を設定してください。", False)
        disable_parent_frame(parent_frame)
        return

    if old_nickname != new_nickname and is_duplicate_record(new_nickname):
        popup_confirm_window(sub_w, parent_frame, "表示名 「%s」は既に登録済みです。別の表示名を設定してください。" % new_nickname, False)
        disable_parent_frame(parent_frame)
        return

    new_data = dict(
        nickname=new_nickname,
        first_name=userinfo.entry_first_name.get(),
        last_name=userinfo.entry_last_name.get(),
        zip_code=userinfo.entry_zip_code.get(),
        state=userinfo.box_state.get(),
        city=userinfo.entry_city.get(),
        address=userinfo.entry_address.get(),
        phone=userinfo.entry_phone.get(),
        mail=userinfo.entry_mail.get(),
        pay_type=userinfo.box_pay_type.get(),
        card_number=userinfo.entry_card_number.get(),
        card_limit_month=userinfo.box_month.get(),
        card_limit_year=userinfo.box_year.get(),
        cvv_number=userinfo.entry_cvv_number.get(),
        payment_method=userinfo.box_payment_method.get(),
        order_id_or_name=userinfo.entry_order_id_or_name.get(),
        return_account=userinfo.entry_return_account.get(),
        twitter_name=userinfo.entry_twitter_name.get(),
        note=userinfo.entry_note.get()
    )

    if old_nickname == new_nickname:
        USER_INFO_TAB.update(new_data, ['nickname'])
    else:
        USER_INFO_TAB.delete(nickname=old_nickname)
        USER_INFO_TAB.insert(new_data)

    popup_confirm_window(root, parent_frame, "情報を登録しました", True)
    disable_parent_frame(parent_frame)
    reload_user_info_list()


def insert_or_update(root, parent_frame, is_update, nickname):
    if is_update:
        label_text = "情報の修正を決定しますか？"
    else:
        label_text = "情報の追加を決定しますか？"
    sub_w = Toplevel(root)
    sub_w.title("")
    sub_w.protocol(WM_DELETE_WINDOW, do_nothing)
    frame = ttk.Frame(sub_w, padding=10)
    frame.grid()
    label = Label(frame, text=label_text)
    label.grid(row=0, column=0)
    button_y = Button(frame, text="はい", command=lambda: delete_insert(root, sub_w, frame, nickname))
    button_n = Button(frame, text="いいえ", command=lambda: enable_parent_frame_and_destroy(parent_frame, sub_w))
    button_y.grid(row=1, column=0, sticky=E)
    button_n.grid(row=1, column=1, sticky=W)
    disable_parent_frame(parent_frame)


def enable_parent_frame_and_destroy(parent_frame, window):
    enable_parent_frame(parent_frame)
    window.destroy()

def enable_parent_frame(parent_frame):
    for child in parent_frame.winfo_children():
        try:
            child.configure(state='active')
        except:
            child.configure(state='normal')


def disable_parent_frame(parent_frame):
    for child in parent_frame.winfo_children():
        child.configure(state='disable')


def setup_editable_form(frame, is_update):
    global userinfo
    row = 0
    userinfo.entry_nickname = mk_label_entry("本ツールの[登録済みリスト]の表示名", frame, row)
    row += 1
    userinfo.entry_first_name = mk_label_entry("名前(性)", frame, row)
    row += 1
    userinfo.entry_last_name = mk_label_entry("名前(名)", frame, row)
    row += 1
    userinfo.entry_zip_code = mk_label_entry("郵便番号(半角数字ハイフン不要)", frame, row)
    row += 1
    userinfo.box_state = mk_label_box("都道府県", STATE_TUPLE, frame, row)
    row += 1
    userinfo.entry_city = mk_label_entry("市区群", frame, row)
    row += 1
    userinfo.entry_address = mk_label_entry("町村番地・建物名・部屋番号", frame, row)
    row += 1
    userinfo.entry_phone = mk_label_entry("電話番号(半角数字ハイフン不要)", frame, row)
    row += 1
    userinfo.entry_mail = mk_label_entry("メールアドレス", frame, row)
    row += 1
    userinfo.box_pay_type = mk_label_box("お支払方法", PAY_TYPE_TUPLE, frame, row)
    row += 1
    userinfo.entry_card_number = mk_label_entry("カード番号(代引き時は空欄)", frame, row)
    row += 1
    userinfo.box_month = mk_label_box("有効期限（月 代引き時は選択不要）", MONTH_TUPLE, frame, row)
    row += 1
    userinfo.box_year = mk_label_box("有効期限（年 代引き時は選択不要）", YEAR_TUPLE, frame, row)
    row += 1
    userinfo.entry_cvv_number = mk_label_entry("CVV番号（代引き時は空欄）", frame, row)
    row += 1
    userinfo.box_payment_method = mk_label_box("決済方法", PAY_METHOD_TUPLE, frame, row)
    row += 1
    userinfo.entry_order_id_or_name = mk_label_entry("BASEお支払い時のご注文IDもしくはお名前\nor 銀行お振込時のお名前", frame, row)
    row += 1
    userinfo.entry_return_account = mk_label_entry("銀行振込時のご返金先口座\n（銀行振込ではない方記載不要）", frame, row)
    row += 1
    userinfo.entry_twitter_name = mk_label_entry("Twitter名", frame, row)
    row += 1
    userinfo.entry_note = mk_label_entry("備考", frame, row)
    row += 1

    if is_update:
        inject_select_info_to_form()

    return row


def open_insert_window():
    global edit_win
    if edit_win is not None and edit_win.winfo_exists():
        return
    open_edit_window(False, "")


def delete_rec(root, parent_frame, nickname):
    USER_INFO_TAB.delete(nickname=nickname)
    popup_confirm_window(root, parent_frame, "%sの情報を削除しました。" % nickname, True)
    disable_parent_frame(parent_frame)
    reload_user_info_list()


def open_delete_window():
    global edit_win
    nickname = get_select_nickname()
    if nickname is None:
        return
    if edit_win is not None and edit_win.winfo_exists():
        return
    disable_buttons()
    edit_win = Toplevel()
    edit_win.title("")
    edit_win.protocol(WM_DELETE_WINDOW, lambda: close_subwindow(edit_win))
    frame = ttk.Frame(edit_win, padding=10)
    frame.grid()
    label = Label(frame, text="%sの情報を削除しますか？" % nickname)
    label.grid(row=0, column=0)
    button_y = Button(frame, text="はい", command=lambda: delete_rec(edit_win, frame, nickname))
    button_n = Button(frame, text="いいえ", command=lambda: close_subwindow(edit_win))
    button_y.grid(row=1, column=0, sticky=E)
    button_n.grid(row=1, column=1, sticky=W)


def open_edit_window(is_update, nickname):
    disable_buttons()
    global edit_win
    if is_update:
        title = "情報更新"
    else:
        title = "新規登録"

    edit_win = Toplevel()
    edit_win.title(title)
    edit_win.protocol(WM_DELETE_WINDOW, lambda: close_subwindow(edit_win))
    frame = ttk.Frame(edit_win, padding=10)
    frame.grid()
    row = setup_editable_form(frame, is_update)
    insert_button = Button(frame, text=title, command=lambda: insert_or_update(edit_win, frame, is_update, nickname))
    insert_button.grid(row=row, column=0)


def inject_select_info_to_form():
    global userinfo
    nickname = get_select_nickname()
    userinfo_rec = USER_INFO_TAB.find_one(nickname=nickname)
    userinfo.entry_nickname.insert(0, nickname)
    userinfo.entry_first_name.insert(0, userinfo_rec[FIRST_NAME])
    userinfo.entry_last_name.insert(0, userinfo_rec[LAST_NAME])
    userinfo.entry_zip_code.insert(0, userinfo_rec[ZIP_CODE])
    userinfo.box_state.set(userinfo_rec[STATE])
    userinfo.entry_city.insert(0, userinfo_rec[CITY])
    userinfo.entry_address.insert(0, userinfo_rec[ADDRESS])
    userinfo.entry_phone.insert(0, userinfo_rec[PHONE])
    userinfo.entry_mail.insert(0, userinfo_rec[MAIL])
    userinfo.box_pay_type.set(userinfo_rec[PAY_TYPE])
    userinfo.entry_card_number.insert(0, userinfo_rec[CARD_NUMBER])
    userinfo.box_month.set(userinfo_rec[CARD_LIMIT_MONTH])
    userinfo.box_year.set(userinfo_rec[CARD_LIMIT_YEAR])
    userinfo.entry_cvv_number.insert(0, userinfo_rec[CVV_NUMBER])
    userinfo.box_payment_method.set(userinfo_rec[PAYMENT_METHOD])
    userinfo.entry_order_id_or_name.insert(0, userinfo_rec[ORDER_ID_OR_NAME])
    userinfo.entry_return_account.insert(0, userinfo_rec[RETURN_ACCOUNT])
    userinfo.entry_twitter_name.insert(0, userinfo_rec[TWITTER_NAME])
    userinfo.entry_note.insert(0, userinfo_rec[NOTE])


def open_update_window():
    global edit_win
    nickname = get_select_nickname()
    if nickname is None:
        return
    if edit_win is not None and edit_win.winfo_exists():
        return
    open_edit_window(True, nickname)


def mk_label_box(label_name, box_list, frame, row):
    label = Label(frame, text=label_name)
    label.grid(row=row, column=0)

    box = ttk.Combobox(frame, width=27, state="readonly")
    box["values"] = box_list
    box.grid(row=row, column=1, padx=10)

    return box


def mk_label_entry(label_name, frame, row):
    label = Label(frame, text=label_name)
    entry = Entry(frame, width=30)
    label.grid(row=row, column=0)
    entry.grid(row=row, column=1, padx=10)
    return entry


def get_nickname_list():
    list = []
    for rec in USER_INFO_TAB.find(order_by=NICKNAME):
        list.append(rec[NICKNAME])
    return tuple(list)


def reload_user_info_list():
    global lb
    global button_paste
    global button_update
    global button_delete

    for i in range(lb.size()):
        lb.delete(0)

    for nickname in get_nickname_list():
        lb.insert(END, nickname)
        lb.selection_set(0)

def site_paste():
    nickname = get_select_nickname()
    if nickname is None:
        return
    userinfo_rec = USER_INFO_TAB.find_one(nickname=nickname)
    site_paste_thread = SitePasteThread(userinfo_rec)
    site_paste_thread.start()


def close_subwindow(sub_w):
    enable_buttons(None)
    sub_w.destroy()


def enable_buttons(event):
    global button_paste
    global button_update
    global button_delete
    global button_insert

    if len(get_nickname_list()) > 0:
        button_paste[BUTTON_STATE] = BUTTON_ENABLED
        button_update[BUTTON_STATE] = BUTTON_ENABLED
        button_delete[BUTTON_STATE] = BUTTON_ENABLED

    button_insert[BUTTON_STATE] = BUTTON_ENABLED


def disable_buttons():
    global button_paste
    global button_update
    global button_delete
    global button_insert

    button_paste[BUTTON_STATE] = BUTTON_DISABLED
    button_update[BUTTON_STATE] = BUTTON_DISABLED
    button_delete[BUTTON_STATE] = BUTTON_DISABLED
    button_insert[BUTTON_STATE] = BUTTON_DISABLED


def do_nothing():
    pass


def main():
    global lb
    global button_paste
    global button_update
    global button_delete
    global button_insert
    root = Tk()
    root.title('サイトペーストツール')

    # Frame
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()
    label = Label(frame1, text="登録済みリスト")
    label.grid(row=0, column=0)

    # Listbox
    #currencies = get_nickname_list()
    #v1 = StringVar(value=currencies)
    #lb = Listbox(frame1, listvariable=v1, height=10)
    lb = Listbox(frame1, height=10)
    lb.grid(row=1, column=0, rowspan=4)

    # Scrollbar
    scrollbar = ttk.Scrollbar(
        frame1,
        orient=VERTICAL,
        command=lb.yview)
    lb['yscrollcommand'] = scrollbar.set
    scrollbar.grid(row=1, column=1, rowspan=4, sticky=(N, S))

    button_paste = ttk.Button(frame1, text='サイトを開いてペースト', command=site_paste, state=BUTTON_DISABLED)
    button_paste.grid(row=1, column=2, sticky=W, padx=10)
    button_update = ttk.Button(frame1, text='編集', command=open_update_window, state=BUTTON_DISABLED)
    button_update.grid(row=2, column=2, sticky=W, padx=10)
    button_delete = ttk.Button(frame1, text='削除', command=open_delete_window, state=BUTTON_DISABLED)
    button_delete.grid(row=3, column=2, sticky=W, padx=10)
    button_insert = ttk.Button(frame1, text='追加', command=open_insert_window)
    button_insert.grid(row=4, column=2, sticky=W, padx=10)

    lb.bind("<<ListboxSelect>>", enable_buttons)
    reload_user_info_list()
    enable_buttons(None)

    root.mainloop()


if __name__ == '__main__':
    edit_win = None
    lb = None
    button_paste = None
    button_update = None
    button_delete = None
    button_insert = None
    userinfo = UserInfo()
    main()
