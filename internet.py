import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, Qt, QDateTime)
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
import datetime as dt
from barcode.writer import ImageWriter
# from pyside2 import
import sqlite3
from reportlab.pdfgen import canvas
# Import user interface file
from maintry import *
import pandas as pd
import glob
import hashlib
import barcode
import random
import string
from math import ceil, floor
from PySide2 import QtXml
from cryptography.fernet import Fernet

f = Fernet('q4NdaAXSPrWN5cyx0qEW5FPpAXW_alHpyQaczWLV734=')

# Global value for the windows status
WINDOW_SIZE = 0
conn = sqlite3.connect("./Database/store1.db")


c = conn.cursor()
#c.execute("PRAGMA KEY=q4NdaAXSPrWN5cyx0qEW5FPpAXW_alHpyQaczWLV734=")

result = c.execute("SELECT * from Inventory")
list_for_product_search=[]
for r in result:
    Id = r[0]
    Name=r[1]
    list_for_product_search.append(Name)

conn.commit()

dateedit = QDate.currentDate()
d = dateedit.toString(Qt.ISODate)

products_list = []
products_price = []
product_quantity = []
labour_price = []
discount_price = []
product_selling_Price = []
product_id = []
orginal_product_price=[]
brlist=[]
brname=[]
brnumber=[]
brsp=[]
brdiscount=[]

guest=True





# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QtCore.QThreadPool()
        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to our top bar buttons
        #
        # Minimize window
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        # Close window
        self.ui.closebutton.clicked.connect(lambda: self.close())
        # Restore/Maximize window
        self.ui.restore_button.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.search_billing.clicked.connect(self.search_bd)

        self.ui.left_toggle_button.clicked.connect(lambda: self.sideleftmenu())

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.tittle_bar.mouseMoveEvent = moveWindow
        self.ui.billing_toggle_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.billing_page))
        self.ui.account_toggle_button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page))

        self.ui.table_database.setColumnWidth(0, 100)
        self.ui.table_database.setColumnWidth(1, 150)
        self.ui.table_database.setColumnWidth(2, 200)
        self.ui.table_database.setColumnWidth(3, 120)
        self.ui.table_database.setColumnWidth(4, 150)
        self.ui.table_database.setColumnWidth(5, 100)
        self.ui.table_database.setColumnWidth(6, 100)
        self.ui.table_database.setColumnWidth(7, 200)

        self.ui.add_to_database_button.clicked.connect(lambda: self.get_items())
        self.ui.clear_all_add_database.clicked.connect(lambda: self.clear_all())
        self.ui.find_ud.clicked.connect(lambda: self.search_d())
        self.ui.ud_ud.clicked.connect(lambda: self.update_d())
        self.ui.refres_button.clicked.connect(lambda: self.load_db())
        self.ui.discount_lineedit.setText('0')
        self.ui.labour_price_entry.setText('0')
        self.ui.final_price.setText('0')
        self.ui.change_button.clicked.connect(lambda: self.change_calculator())
        self.ui.clear_row_button.clicked.connect(lambda: self.del_item_from_cart())
        # self.ui.print_button.clicked.connect(lambda: self.stock_decreaser())
        self.ui.next_customer_button.clicked.connect(lambda: self.next_customer())
        self.ui.add_to_cart.clicked.connect(lambda: self.add_to_cart1())
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit_from.setDate(QDate.currentDate())
        self.ui.dateEdit_to.setDate(QDate.currentDate())
        self.ui.get_transaction.clicked.connect(lambda: self.date_transation())
        self.ui.get_bill_number.clicked.connect(lambda: self.get_transaction_billid())
        self.ui.non_mover_button.clicked.connect(lambda: self.non_moving_items())
        self.ui.nonmovingreset.clicked.connect(lambda: self.clear_movement_list())
        self.ui.update_graph_button.clicked.connect(lambda: self.update_graph())
        self.ui.invoice_button.clicked.connect(lambda: self.gen_invoice())
        self.ui.excelbutton.clicked.connect(lambda: self.daily_transaction_data())
        self.ui.update_service_button.clicked.connect(lambda: self.work_undertaken())
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
        self.ui.get_undertaken_details_button.clicked.connect(lambda: self.work_table())
        self.ui.delete_cusid_button.clicked.connect(lambda: self.delete_current_worktable())
        self.ui.truncate_table_button.clicked.connect(lambda: self.truncate_table())
        self.ui.inventory_excel_button.clicked.connect(lambda: self.inventory_transaction_data())
        self.ui.inventory_clear_button.clicked.connect(lambda: self.inventory_clear_function())
        self.ui.pushButton_2.clicked.connect(lambda: self.read_table_data())
        self.ui.product_name_search.clicked.connect(lambda:self.search_product_name())
        self.ui.login_button.clicked.connect(lambda:self.password_checker())
        self.ui.update_product_status_button.clicked.connect(lambda:self.read_productstaus())
        self.ui.service_id_button.clicked.connect(lambda:self.get_service_details())
        self.ui.dateEdit_from_log.setDate(QDate.currentDate())
        self.ui.dateEdit_log_to.setDate(QDate.currentDate())
        self.ui.log_details_button.clicked.connect(lambda:self.log_table())
        self.ui.all_files_barcode.clicked.connect(lambda:self.barcodef())
        self.ui.clear_barcode_button.clicked.connect(lambda: self.barcode_clear_function())
        self.ui.idbarcode_button.clicked.connect(lambda:self.barcodeid())
        self.ui.gen_barcode_pdf.clicked.connect(lambda:self.barcode_main_generation())
        self.ui.clearfiles_barcode.clicked.connect(lambda:self.clearbar_files())
        self.ui.barcode_add_to_database.clicked.connect(lambda:self.barcode_entry())
        self.ui.bar_product_get.clicked.connect(lambda:self.barcodename())
        self.ui.im_per_row.setText('4')
        self.ui.im_per_page.setText('32')
        self.ui.transaction_truncate_button.clicked.connect(lambda:self.transaction_list_clear())
        self.ui.register_admin.clicked.connect(lambda:self.create_admin())
        self.ui.register_employee.clicked.connect(lambda: self.create_employee())
        self.ui.view_user.clicked.connect(lambda: self.user_table())
        self.ui.login_clear_button.clicked.connect(lambda: self.clear_username())
        self.ui.single_user_remove_button.clicked.connect(lambda: self.clear_single_user())
        self.ui.bar_discount.setText('0')
        self.ui.user_logs_clear_button.clicked.connect(lambda: self.clear_user_logs())
        self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page)
        names=QCompleter(list_for_product_search)
        self.ui.logout_button.clicked.connect(lambda:self.logout())

        self.ui.product_name_search_edit.setCompleter(names)
        self.ui.bar_product_name.setCompleter(names)
        self.show()


    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def password_checker(self):


        sql = c.execute('SELECT username,password,Admin from Login')
        self.hash = hashlib.sha256(str.encode(self.ui.password_e.text())).hexdigest()
        for r in sql:
            self.user = r[0]
            self.password = r[1]
            self.user_status = r[2]
            print(self.user)
            print(self.password)
            print(self.user_status)
            if self.user == self.ui.username_e.text() and self.password == self.hash and self.user_status == 'y':
                self.admin = True
                self.ui.username_label.setText(self.ui.username_e.text())
                if self.admin:
                    self.ui.inventory_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.inventory_page))

                if self.admin:
                    self.ui.services_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.services_page))
                if self.admin:
                    self.ui.sales_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sales_page))

                if self.admin:
                    self.ui.settings_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

                if self.admin:
                    self.ui.logs_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.log_page))
                if self.admin:
                    self.ui.barcode_toggle_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.barcode_page))
                if self.admin:
                    self.ui.setting_toggle_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.setting_page))
                self.ui.inventory_toggle_button.setEnabled(True)
                self.ui.services_toggle_button.setEnabled(True)
                self.ui.sales_toggle_button.setEnabled(True)
                self.ui.settings_toggle_button.setEnabled(True)
                self.ui.logs_toggle_button.setEnabled(True)
                self.ui.barcode_toggle_button.setEnabled(True)
                self.ui.setting_toggle_button.setEnabled(True)
                self.ui.username_e.clear()
                self.ui.password_e.clear()
            elif self.user == self.ui.username_e.text() and self.password == self.hash and self.user_status == 'n':
                self.employe = True
                self.ui.username_label.setText(self.ui.username_e.text())
                if self.employe:
                    self.ui.inventory_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.inventory_page))
                if self.employe:
                    self.ui.barcode_toggle_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.barcode_page))
                if self.employe:
                    self.ui.settings_toggle_button.clicked.connect(
                        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))
                self.ui.inventory_toggle_button.setEnabled(True)
                self.ui.services_toggle_button.setEnabled(True)
                self.ui.sales_toggle_button.setEnabled(True)
                self.ui.settings_toggle_button.setEnabled(True)
                self.ui.logs_toggle_button.setEnabled(True)
                self.ui.barcode_toggle_button.setEnabled(True)
                self.ui.setting_toggle_button.setEnabled(True)
                self.ui.username_e.clear()
                self.ui.password_e.clear()

    def logout(self):
        self.admin = False
        self.employe = False
        self.ui.inventory_toggle_button.setEnabled(False)
        self.ui.services_toggle_button.setEnabled(False)
        self.ui.sales_toggle_button.setEnabled(False)
        self.ui.settings_toggle_button.setEnabled(False)
        self.ui.logs_toggle_button.setEnabled(False)
        self.ui.barcode_toggle_button.setEnabled(False)
        self.ui.setting_toggle_button.setEnabled(False)
        self.ui.username_e.clear()
        self.ui.password_e.clear()

    def get_items(self, *args, **kwargs):

        self.name = self.ui.name_e.text()  #
        self.stock = self.ui.stock_e.text()
        self.cp = self.ui.cp_e.text()
        self.sp = self.ui.sp_e.text()

        # dynamic variables
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.profit = float(self.totalsp - self.totalcp)
        # check empty entry
        if self.name == '' or self.stock == '' or self.cp == "" or self.sp == '':
            print('wrong')
        else:
            sql = "INSERT INTO Inventory(Name, Stock,Cost_Price,Selling_Price, Tcp,Tsp,Profit,temp,bar)VALUES(?,?,?,?,?,?,?,'0','0')"
            c.execute(sql, (
                self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.profit))
            conn.commit()


        sql1="INSERT INTO user_logs(user,action,date_time,product_name,stock_updated,cp_changed,sp_changed)VALUES(?,'Insert',?,?,?,?,?)"
        c.execute(sql1,(self.ui.username_label.text(),self.ui.dateEdit.text(),self.name,self.stock,self.cp,self.sp))
        conn.commit()
        query = "SELECT * FROM Inventory"
        result = c.execute(query)
        self.ui.table_database.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.table_database.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.table_database.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        QtGui.QGuiApplication.processEvents()


    def clear_all(self, *args, **kwargs):
        self.ui.name_e.clear()
        self.ui.stock_e.clear()
        self.ui.cp_e.clear()
        self.ui.sp_e.clear()

        ##########################################################################################################################
        ############################# UPDATE DATABASE FUNCTIONS #################################################################

    def search_d(self, *args, **kwargs):

        sql = "SELECT * FROM Inventory WHERE Id=?"
        result = c.execute(sql, (self.ui.ide_ud.text(),))

        for r in result:
            self.n1 = r[1]  # name
            self.n2 = r[2]  # stock
            self.n3 = r[3]  # cp
            self.n4 = r[4]  # sp
            self.n5 = r[5]  # tcp
            self.n6 = r[6]  # tsp
            self.n7 = r[7]  # profit
            conn.commit()

            # insert entries to update
            self.ui.name_ud.clear()
            self.ui.name_ud.insert(str(self.n1))
            self.ui.stock_ud.clear()
            self.ui.stock_ud.insert(str(self.n2))
            self.ui.cp_ud.clear()
            self.ui.cp_ud.insert(str(self.n3))
            self.ui.sp_ud.clear()
            self.ui.sp_ud.insert(str(self.n4))
        QtGui.QGuiApplication.processEvents()

    def update_d(self, *args, **kwargs):
        self.u1 = self.ui.name_ud.text()
        self.u2 = self.ui.stock_ud.text()
        self.u3 = self.ui.cp_ud.text()
        self.u4 = self.ui.sp_ud.text()
        self.u5 = float(self.ui.stock_ud.text()) * float(self.ui.cp_ud.text())
        self.u6 = float(self.ui.stock_ud.text()) * float(self.ui.sp_ud.text())
        self.u7 = float(self.ui.stock_ud.text()) * float(self.ui.sp_ud.text()) - float(
            self.ui.stock_ud.text()) * float(
            self.ui.cp_ud.text())
        query = "UPDATE Inventory SET Name=?, Stock=?, Cost_Price=?, Selling_Price=?, Tcp=?, Tsp=?, Profit=? WHERE Id=?"
        c.execute(query,
                  (
                      self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.ui.ide_ud.text()))
        conn.commit()
        sql1 = "INSERT INTO user_logs(user,action,date_time,product_name,stock_updated,cp_changed,sp_changed)VALUES(?,'Update',?,?,?,?,?)"
        c.execute(sql1, (self.ui.username_label.text(), self.ui.dateEdit.text(), self.u1, self.u2, self.u3, self.u4))
        conn.commit()
        QtGui.QGuiApplication.processEvents()

        query1 = "SELECT * FROM Inventory"
        result = c.execute(query1)
        self.ui.table_database.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.table_database.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.table_database.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        ##############################################################################################################################
        #######################################################################################################################

    def load_db(self):
        query = "SELECT * FROM Inventory"
        result = c.execute(query)
        self.ui.table_database.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.table_database.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.table_database.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        QtGui.QGuiApplication.processEvents()

        ################################################################################################################################################
        #####################################################################################################################################################
        ################### BULLING PAGE#####################################################

    def search_bd(self, *args, **kwargs):

        sql = "SELECT * FROM Inventory WHERE Id=?"
        result = c.execute(sql, (self.ui.ide_billing_page.text(),))

        for r in result:
            self.n11 = r[1]  # name
            self.n22 = r[2]  # stock
            self.n33 = r[3]  # cp
            self.n44 = r[4]  # sp
            self.n55 = r[5]  # tcp
            self.n66 = r[6]  # tsp
            self.n77 = r[7]  # profit
            conn.commit()

            # insert entries to update
            self.ui.pplabel.clear()
            self.ui.pplabel.setText(str(self.n11))
            self.ui.pprice_l.clear()
            self.ui.pprice_l.setText(str(self.n44))
        QtGui.QGuiApplication.processEvents()

    def search_product_name(self):
        sql='SELECT * FROM Inventory WHERE Name=?'
        result=c.execute(sql,(self.ui.product_name_search_edit.text(),))

        for r in result:
            self.n00 = r[0]
            self.n11 = r[1]  # name
            self.n22 = r[2]  # stock
            self.n33 = r[3]  # cp
            self.n44 = r[4]  # sp
            self.n55 = r[5]  # tcp
            self.n66 = r[6]  # tsp
            self.n77 = r[7]  # profit

            conn.commit()

        # insert entries to update

        self.ui.ide_billing_page.clear()
        self.ui.ide_billing_page.setText(str(self.n00))
        self.ui.pplabel.clear()
        self.ui.pplabel.setText(str(self.n11))
        self.ui.pprice_l.clear()
        self.ui.pprice_l.setText(str(self.n44))


    def add_to_cart1(self):

        if self.n22 < int(self.ui.Quantity_lineedit.text()):
            print('fuck')
        else:
            total_products_price = (float(self.n44) * float(self.ui.Quantity_lineedit.text())) + float(
                self.ui.labour_price_entry.text()) - float(self.ui.discount_lineedit.text())
            products_list.append(self.n11)
            products_price.append(total_products_price)
            product_quantity.append(int(self.ui.Quantity_lineedit.text()))
            labour_price.append(int(self.ui.labour_price_entry.text()))
            discount_price.append(int(self.ui.discount_lineedit.text()))
            product_selling_Price.append(int(self.ui.pprice_l.text()))
            product_id.append(int(self.ui.ide_billing_page.text()))
            print(product_id)

            row = 0
            for d in product_id:
                self.ui.billing_table_widget.setRowCount(len(products_list))
                self.ui.billing_table_widget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d)))
                row = row + 1

            row = 0
            for x in products_list:
                self.ui.billing_table_widget.setRowCount(len(products_list))
                self.ui.billing_table_widget.setItem(row, 1, QtWidgets.QTableWidgetItem(x))
                row = row + 1

            row = 0
            total = 0
            for y in products_price:
                self.ui.billing_table_widget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(y)))
                total = total + y
                self.ui.final_price.setText(str(total))
                self.ui.final_price1.setText(str(total))
                row = row + 1

            row = 0
            for z in product_quantity:
                self.ui.billing_table_widget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(z)))
                row = row + 1

            row = 0
            for w in labour_price:
                self.ui.billing_table_widget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(w)))

                row = row + 1

            row = 0
            for a in discount_price:
                self.ui.billing_table_widget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(a)))
                row = row + 1

            row = 0
            for b in product_selling_Price:
                self.ui.billing_table_widget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(b)))
                row = row + 1

    def del_item_from_cart(self):

        products_list.pop(-1)
        print(products_list)
        products_price.pop(-1)
        product_selling_Price.pop(-1)
        product_quantity.pop(-1)
        discount_price.pop(-1)
        labour_price.pop(-1)
        product_id.pop(-1)
        self.ui.billing_table_widget.setRowCount(len(products_list))

        total = 0
        for y in products_price:
            total = total + y
            self.ui.final_price.setText(str(total))

        print('print failed')

    # def next_customer(self):

    def change_calculator(self):
        change_rs = float(self.ui.cus_given_amount_line_edit.text()) - float(self.ui.final_price.text())
        self.ui.change_indication_label.setText(str(change_rs))

    def date_transation(self):
        self.ui.tableWidget.setRowCount(0)
        self.tr1 = self.ui.dateEdit_from.text()
        self.tr2 = self.ui.dateEdit_to.text()
        query = c.execute(('''SELECT * FROM Transactions  WHERE date BETWEEN ? AND ? ORDER BY date '''),
                          (self.tr1, self.tr2), )
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(query):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_transaction_billid(self):
        query = "SELECT * FROM Transactions WHERE Bill_id =?"
        result = c.execute(query, (self.ui.bill_identry.text(),))
        self.ui.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    # def stock_decreaser(self, *args, **kwargs):

    def non_moving_items(self):
        query = "SELECT Name,temp,Selling_Price FROM Inventory ORDER BY temp DESC"
        result = c.execute(query)
        self.ui.no_moving_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.no_moving_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.no_moving_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        QtGui.QGuiApplication.processEvents()

    def log_table(self):

        query = "SELECT * FROM user_logs WHERE date_time BETWEEN ? AND ? ORDER BY date_time"
        result=c.execute(query,(self.ui.dateEdit_from_log.text(),self.ui.dateEdit_log_to.text()))

        self.ui.log_table_widget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.log_table_widget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.log_table_widget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def clear_movement_list(self):
        query = "UPDATE Inventory SET temp = 0"
        result = c.execute(query)
        conn.commit()

    def update_graph(self):
        self.tr1 = self.ui.dateEdit_from.text()
        self.tr2 = self.ui.dateEdit_to.text()
        b = c.execute(("SELECT SUM(total),date FROM Transactions GROUP BY date HAVING date BETWEEN (?) AND (?) "),
                      (self.tr1, self.tr2), )

        z = []
        t = []
        for row in b:
            x = row[0]
            y = row[1]
            z.append(x)
            t.append(y)
        q = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in t]
        p = range((len(q)))

        self.ui.MplWidget.canvas.axes.clear()
        self.ui.MplWidget.canvas.axes.set_xticklabels(t, rotation='vertical', size=10)
        self.ui.MplWidget.canvas.axes.bar(p, z, tick_label=t)
        self.ui.MplWidget.canvas.axes.legend(('MAX Transactions', 'transactions'), loc='upper right')
        self.ui.MplWidget.canvas.axes.set_title('TRANSACTIONS')
        self.ui.MplWidget.canvas.draw()

    def daily_transaction_data(self):
        query = 'SELECT * FROM Transactions where date BETWEEN ? AND ?'
        csv = c.execute(query, (self.tr1, self.tr2))
        df = pd.DataFrame(csv)
        df.to_excel(f'{self.tr2}Transaction.xlsx',
                    header=['Bill_id', 'customer_name', 'phone_number', 'date', 'product_name', 'quantity',
                            'selling price', 'labourcharge', 'discount', 'total'])

    def inventory_transaction_data(self):
        query = 'SELECT * FROM Inventory'
        csv = c.execute(query)
        df = pd.DataFrame(csv)
        df.to_excel(f'.{self.ui.dateEdit.text()}inventory.xlsx',
                    header=['Id', 'Name', 'Stock', 'Cost price', 'Selling Price', 'Toatl Cp', 'Total selling price',
                            'profit', 'Stock movement'])

    def work_undertaken(self):
        query = 'INSERT INTO Service(customer_name,undertaken,completion,phone,service,branch) VALUES(?,?,?,?,?,?)'
        c.execute(query, (self.ui.customer_name_e.text(), self.ui.dateTimeEdit.text(), self.ui.dateTimeEdit_2.text(),
                          self.ui.phone_number_e.text(), self.ui.service_edit.text(),self.ui.comboBox.currentText()))
        conn.commit()

    def work_table(self):
        query = "SELECT * FROM Service"
        result = c.execute(query)
        self.ui.undertaken_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.undertaken_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.undertaken_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def delete_current_worktable(self):
        sql = c.execute('DELETE FROM Service WHERE cus_Id=?', (self.ui.delete_cusid_edit.text()))
        conn.commit()

    def truncate_table(self):
        sql = c.execute(" DELETE FROM Service")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'Service' ")
        conn.commit()

    def clear_user_logs(self):
        sql = c.execute(" DELETE FROM user_logs")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'user_logs' ")
        conn.commit()


    def inventory_clear_function(self):
        sql = c.execute("DELETE FROM Inventory")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'Inventory' ")
        conn.commit()
    def transaction_list_clear(self):
        sql = c.execute("DELETE FROM Transactions")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'Transactions' ")
        conn.commit()

    # Restore or maximize your window
    def restore_or_maximize_window(self):

        # Global windows state
        global WINDOW_SIZE  # The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
            # If the window is not maximized
            WINDOW_SIZE = 1  # Update value to show that the window has been maxmized
            self.showMaximized()
            # Update button icon
            self.ui.restore_button.setIcon(QtGui.QIcon(u":icons/icons/cil-window-maximize"))  # Show maximized icon
        else:
            # If the window is on its default size
            WINDOW_SIZE = 0  # Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()
            # Update button icon
            self.ui.restore_button.setIcon(QtGui.QIcon(u":icons/icons/cil-window-restore.png"))  # Show minized icon

    def read_table_data(self):
        rowcount = self.ui.billing_table_widget.rowCount()
        products_list.clear()
        product_selling_Price.clear()
        labour_price.clear()
        discount_price.clear()
        products_price.clear()
        orginal_product_price.clear()

        for row in range(rowcount):

            widgetItem = self.ui.billing_table_widget.item(row, 4)
            widgetItem1 = self.ui.billing_table_widget.item(row,5)
            widgetItem2 = self.ui.billing_table_widget.item(row, 2)
            widgetItem3 = self.ui.billing_table_widget.item(row,1)


            products_list.append(widgetItem3.text())
            labour_price.append(int(widgetItem.text()))
            discount_price.append(int(widgetItem1.text()))
            product_selling_Price.append(int(widgetItem2.text()))
            x = 0
            for item in labour_price:
                grand_total_products_price = (float(product_selling_Price[x]) * float(self.ui.Quantity_lineedit.text())) + float(
                    labour_price[x]) - float(discount_price[x])
                total_products_price = (float(product_selling_Price[x]) * float(self.ui.Quantity_lineedit.text()))
                x += 1
                total = 0

            products_price.append(grand_total_products_price)
            orginal_product_price.append(total_products_price)
        row = 0
        total = 0
        for y in products_price:
            self.ui.billing_table_widget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(y)))
            total = total + y
            self.ui.final_price.setText(str(total))
            self.ui.final_price1.setText(str(total))
            row = row + 1

            print(products_price)



    # def update_service(self,rowData):

    def read_productstaus(self):


        rowcount = self.ui.undertaken_table.rowCount()
        sql1 = c.execute('SELECT * FROM Service')
        j = []
        for t in sql1:
            self.p = t[0]
            j.append(self.p)
        print(j[0])
        self.j = 0
        self.k = 0

        for row in range(rowcount):
            janco = []
            completion=[]
            productstatus = self.ui.undertaken_table.item(row, 3)
            comp= self.ui.undertaken_table.item(row, 6)
            janco.append(productstatus.text())
            completion.append(comp.text())

            for x in janco:
                print(x)
                sql = c.execute(('UPDATE Service SET product_status=? WHERE cus_Id=?'), (x,j[self.j]),)
                conn.commit()
                self.j+=1

            for y in completion:
                sql2=c.execute(('UPDATE Service SET completion=? WHERE cus_Id=?'), (y,j[self.k]))
                conn.commit()
                self.k += 1
        query = "SELECT * FROM Service"
        result = c.execute(query)
        self.ui.undertaken_table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.undertaken_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.undertaken_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def get_service_details(self):
        sql='SELECT * FROM Service WHERE cus_Id=?'
        a=c.execute(sql,(self.ui.service_e.text()))
        for r in a:
            self.customer=r[2]
            self.phone=r[7]
            conn.commit()
        self.ui.customer_name_e.clear()
        self.ui.customer_name_e.setText(str(self.customer))
        self.ui.phone_number_e.clear()
        self.ui.phone_number_e.setText(str(self.phone))

    def next_customer(self):
        products_list.clear()
        products_price.clear()
        product_quantity.clear()
        labour_price.clear()
        discount_price.clear()
        product_selling_Price.clear()
        product_id.clear()
        self.ui.billing_table_widget.setRowCount(len(products_list))

        self.ui.final_price.setText('0')
        self.ui.final_price1.setText('0')
        self.ui.customer_name_e.setText('')
        self.ui.phone_number_e.setText('')
        self.ui.service_edit.setText('')
        self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
        self.ui.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
        self.ui.Quantity_lineedit.setText('1')
        self.ui.ide_billing_page.setText('')
        self.ui.discount_lineedit.setText('0')
        self.ui.pplabel.setText('')
        self.ui.pprice_l.setText('')
        self.ui.labour_price_entry.setText('0')
        self.ui.cus_given_amount_line_edit.setText('0')
        self.ui.change_indication_label.setText('0')






    def gen_invoice(self):
        if products_list:

            self.x = 0

            for i in products_list:
                initial = "SELECT * FROM Inventory WHERE Id=?"
                result = c.execute(initial, (product_id[self.x],))
                for u in result:
                    self.oldstock = u[2]
                    print(self.oldstock)
                self.new_stock = (int(self.oldstock) - int(product_quantity[self.x]))
                print(product_quantity)
                print(self.x)
                print(self.new_stock)
                sql = '''UPDATE Inventory SET Stock=?,temp=temp+? WHERE Id=?'''
                c.execute(sql, (self.new_stock, int(product_quantity[self.x]), product_id[self.x]))
                conn.commit()
                self.x = self.x + 1

            sql2 = 'INSERT INTO Transactions (customer_name,customer_phone_number,date,product_name,quantity,selling_price,labour_charge,discount,total) VALUES(?,?,?,?,?,?,?,?,?)'
            c.execute(sql2, (self.ui.customer_name_e.text(), self.ui.phone_number_e.text(), self.ui.dateEdit.text(),
                             ','.join(map(str, products_list)), ','.join(map(str, product_quantity)),
                             ','.join(map(str, product_selling_Price)),
                             ','.join(map(str, labour_price)), ','.join(map(str, discount_price)),
                             self.ui.final_price.text()))
            conn.commit()
            sql1 = "INSERT INTO user_logs(user,action,date_time,Sold_product,Quantity)VALUES(?,'Transaction',?,?,?)"
            c.execute(sql1, (self.ui.username_label.text(), self.ui.dateEdit.text(), ','.join(map(str, products_list)),','.join(map(str, product_quantity))))
            conn.commit()
            query1 = c.execute('SELECT Max(Bill_id) FROM Transactions')
            for r in query1:
                self.bill1 = r[0]
                conn.commit()
                self.ui.bill_line_edit.clear()
                self.ui.bill_line_edit.insert(str(self.bill1))
            # Creating Canvas
            cc = canvas.Canvas(f"./invoice/{self.ui.bill_line_edit.text()}.pdf", pagesize=(200, 250), bottomup=0)
            # Logo Section
            # Setting th origin to (10,40)
            cc.translate(10, 40)
            # Inverting the scale for getting mirror Image of logo
            cc.scale(1, -1)
            # Inserting Logo into the Canvas at required position
            # c.drawImage("logo.jpg",0,0,width=50,height=30)
            # Title Section
            # Again Inverting Scale For strings insertion
            cc.scale(1, -1)
            # Again Setting the origin back to (0,0) of top-left
            cc.translate(-10, -40)
            # Setting the font for Name title of company
            cc.setFont("Helvetica-Bold", 8)
            # Inserting the name of the company
            cc.drawCentredString(125, 20, "MURAD COMPUTER TECHNOLOGY")
            # For under lining the title
            cc.line(50, 22, 200, 22)
            # Changing the font size for Specifying Address
            cc.setFont("Helvetica-Bold", 5)
            cc.drawCentredString(125, 30, "Nassar Al Attiya Street, Al Khartiyat,")
            cc.drawCentredString(125, 35, "Ph:55965892,44780468")
            # Changing the font size for Specifying GST Number of firm
            cc.setFont("Helvetica-Bold", 6)
            cc.drawCentredString(125, 42, "DOHA QATAR")
            # Line Seprating the page header from the body
            cc.line(5, 45, 195, 45)
            # Document Information
            # Changing the font for Document title
            cc.setFont("Courier-Bold", 8)
            cc.drawCentredString(100, 55, "INVOICE")
            # This Block Consist of Costumer Details
            cc.roundRect(15, 63, 170, 40, 10, stroke=1, fill=0)
            cc.setFont("Times-Bold", 5)
            cc.drawRightString(70, 70, "INVOICE No. :")
            cc.drawCentredString(130, 70, f"{self.ui.bill_line_edit.text()}")
            cc.drawRightString(70, 80, f"DATE :")
            cc.drawRightString(130, 80, f"{self.ui.dateEdit.text()}")
            cc.drawRightString(70, 90, "CUSTOMER NAME :")
            cc.drawCentredString(130, 90, f"{self.ui.customer_name_e.text()}")
            cc.drawRightString(70, 100, "Description :")
            if sum(discount_price)!=0:
                cc.drawRightString(180, 217,f'{sum(discount_price)}')
                cc.drawRightString(80, 217, 'Discount')
            if sum(labour_price) !=0:
                cc.drawRightString(180, 205, f'{sum(labour_price)}')
                cc.drawRightString(80, 205 ,'Labour Charge')



            # This Block Consist of Item Description
            cc.roundRect(15, 108, 170, 130, 10, stroke=1, fill=0)
            cc.line(15, 120, 185, 120)
            cc.drawCentredString(25, 118, "SR No.")
            cc.drawCentredString(75, 118, "GOODS DESCRIPTION")
            cc.drawCentredString(125, 118, "RATE")
            cc.drawCentredString(148, 118, "QTY")
            cc.drawCentredString(173, 118, "TOTAL")
            # Drawing table for Item Description
            cc.line(15, 210, 185, 210)
            cc.line(35, 108, 35, 220)
            cc.line(115, 108, 115, 220)
            cc.line(135, 108, 135, 220)
            cc.line(160, 108, 160, 220)
            # Declaration and Signature
            cc.line(15, 220, 185, 220)
            cc.line(100, 220, 100, 238)
            cc.drawString(20, -20, "We declare that above mentioned")
            cc.drawString(20, 225, "We declare that above mentioned")
            cc.drawString(20, 230, "information is true.")
            cc.drawString(20, 235, "(This is system generated invoive)")
            cc.drawRightString(180, 225, f"Grand total: {self.ui.final_price1.text()}")
            cc.drawRightString(180, 235, "Authorised Signatory")
            b = 0
            i = 1
            g = 0
            for h, t in enumerate(products_list, start=1):
                cc.drawRightString(80, 130 + g, products_list[b])
                cc.drawRightString(25, 130 + g, str(h))
                cc.drawRightString(130, 130 + g, str(product_selling_Price[b]))
                cc.drawRightString(148, 130 + g, str(product_quantity[b]))
                if orginal_product_price:
                    cc.drawRightString(180, 130 + g, str(orginal_product_price[b]))
                else:
                    cc.drawRightString(180, 130 + g, str(products_price[b]))
                b += 1
                g += 5
            # End the Page and Start with new
            cc.showPage()
            # Saving the PDF
            cc.save()
            # def draw_graph(self):

            products_list.clear()
            products_price.clear()
            product_quantity.clear()
            labour_price.clear()
            discount_price.clear()
            product_selling_Price.clear()
            product_id.clear()
            self.ui.billing_table_widget.setRowCount(len(products_list))

            self.ui.final_price.setText('0')
            self.ui.final_price1.setText('0')
            self.ui.customer_name_e.setText('')
            self.ui.phone_number_e.setText('')
            self.ui.service_edit.setText('')
            self.ui.dateTimeEdit.setDateTime(QDateTime.currentDateTime())
            self.ui.dateTimeEdit_2.setDateTime(QDateTime.currentDateTime())
            self.ui.Quantity_lineedit.setText('1')
            self.ui.ide_billing_page.setText('')
            self.ui.discount_lineedit.setText('0')
            self.ui.pplabel.setText('')
            self.ui.pprice_l.setText('')
            self.ui.labour_price_entry.setText('0')
            self.ui.cus_given_amount_line_edit.setText('0')
            self.ui.change_indication_label.setText('0')

    def barcodef(self):
        sql = c.execute("DELETE FROM barcode")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'barcode' ")
        conn.commit()
        brlist.clear()
        brname.clear()
        brnumber.clear()
        sql='SELECT Id,Name FROM Inventory ORDER BY Id'
        b=c.execute(sql)
        self.ui.barcode_table.setRowCount(0)
        for row_number, row_data in enumerate(b):
            self.ui.barcode_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.barcode_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui.barcode_table.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(0)))

        rowcount1 = self.ui.barcode_table.rowCount()
        columncount1=self.ui.barcode_table.columnCount()
        for i in range(int(self.ui.range_lineEdit.text())):
            for row in range(rowcount1):
                rowdata3 = []
                for colun in range(columncount1):


                    prod_name = self.ui.barcode_table.item(row, colun)

                    rowdata3.append(prod_name.text())
                sql=c.execute("INSERT INTO barcode(Id,Name,number) VALUES(?,?,?)",(rowdata3))

                conn.commit()
    def barcodeid(self):
        for xu in range(int(self.ui.range_lineEdit.text())):
            sql='SELECT Id,Name,Selling_Price FROM Inventory where Id=?'
            b=c.execute(sql,(self.ui.barcode_lineEdit.text(),))
            for r in b:
                x=r[0]
                y=r[1]
                sp=r[2]


                brlist.append(str(x))
                brname.append(str(y))
                brsp.append(str(sp))
            brnumber.append((str(self.ui.range_lineEdit.text())))
            brdiscount.append(str(self.ui.bar_discount.text()))

            row=0
            for d in brlist:
                self.ui.barcode_table.setRowCount(len(brlist))
                self.ui.barcode_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d)))
                row = row + 1
            row=0
            for s in brname:
                self.ui.barcode_table.setRowCount(len(brlist))
                self.ui.barcode_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(s)))
                row = row + 1

            row = 0
            for q in brsp:
                self.ui.barcode_table.setRowCount(len(brsp))
                self.ui.barcode_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(q)))
                row = row + 1
            row = 0
            for f in brdiscount:
                self.ui.barcode_table.setRowCount(len(brdiscount))
                self.ui.barcode_table.setItem(row, 3, QtWidgets.QTableWidgetItem(str(f)))
                row = row + 1

    def barcodename(self):
        for xu in range(int(self.ui.range_lineEdit.text())):
            sql = 'SELECT Id,Name,Selling_Price FROM Inventory where Name=?'
            b = c.execute(sql, (self.ui.bar_product_name.text(),))
            for r in b:
                self.bid = r[0]
                self.bn = r[1]
                self.bsp = r[2]

                brlist.append(str(self.bid))
                brname.append(str(self.bn))
                brsp.append(str(self.bsp))
            brnumber.append((str(self.ui.range_lineEdit.text())))
            brdiscount.append(str(self.ui.bar_discount.text()))

            row = 0
            for d in brlist:
                self.ui.barcode_table.setRowCount(len(brlist))
                self.ui.barcode_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(d)))
                row = row + 1
            row = 0
            for s in brname:
                self.ui.barcode_table.setRowCount(len(brlist))
                self.ui.barcode_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(s)))
                row = row + 1

            row = 0
            for q in brsp:
                self.ui.barcode_table.setRowCount(len(brsp))
                self.ui.barcode_table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(q)))
                row = row + 1
            row = 0
            for f in brdiscount:
                self.ui.barcode_table.setRowCount(len(brdiscount))
                self.ui.barcode_table.setItem(row,3, QtWidgets.QTableWidgetItem(str(f)))
                row = row + 1



    def barcode_entry(self):
        sql = c.execute("DELETE FROM barcode")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'barcode' ")
        conn.commit()
        brlist.clear()
        brname.clear()
        brnumber.clear()
        rowcount1 = self.ui.barcode_table.rowCount()
        columncount1 = self.ui.barcode_table.columnCount()
        for row in range(rowcount1):
            rowdata3 = []

            for colun in range(columncount1):


                prod_name = self.ui.barcode_table.item(row, colun)

                rowdata3.append(prod_name.text())


            sql=c.execute("INSERT INTO barcode(Id,Name,number,discount) VALUES(?,?,?,?)",(rowdata3))

            conn.commit()
            #xo+=1


    def barcode_clear_function(self):
        sql = c.execute("DELETE FROM barcode")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'barcode' ")
        conn.commit()
        brlist.clear()
        brname.clear()
        brnumber.clear()
        brsp.clear()
        brdiscount.clear()
        self.ui.barcode_table.setRowCount(len(brname))



    def barcode_main_generation(self):
        data = c.execute('SELECT barcodeid,Name,number,discount FROM barcode')




        def j1():
            for i in data:
                n = i[0]
                t = i[1]
                s = i[2]
                e = i[3]
                a = barcode.get_barcode_class('code128')
                b = a(str(n), writer=ImageWriter())
                barcode.base.Barcode.default_writer_options['write_text'] = False

                d = b.save(f'./bar/{t}.{n}.{s}.{e}')

        def j2():
            for i in data:
                n = i[0]
                t = i[1]
                s = i[2]
            PATH = r"./bar"
            os.chdir(PATH)
            images = glob.glob("*.png")


            b = 0
            for x in images:
                background = Image.new('RGBA', (350, 350), (255, 255, 255, 255))
                ar = str(x)
                print(ar)

                res = f"{ar.split('.')[3]}".join(random.choices(string.ascii_uppercase +
                                                                string.ascii_lowercase , k=4))
                print(res)

                draw = ImageDraw.Draw(background)
                fnt = ImageFont.truetype('arial.ttf', 15)
                draw.text((30, 5), "Murad Computers", font=fnt, fill=(0, 0, 0)),
                draw.text((30, 250), f"{ar.split('.')[0]}\nQR:{ar.split('.')[2]}\n{res}", font=fnt, fill=(0, 0, 0))
                qr = Image.open(x)
                background.paste(qr, (0, 25))
                background.save(f'./final/back{x}.png')
                b += 1

        def j3():
            PATH = r"./final"


            frame_width = 1920
            images_per_row = int(self.ui.im_per_row.text())
            padding = 2

            os.chdir(PATH)

            ui = glob.glob("*.png")
            n = int(self.ui.im_per_page.text())
            # using list comprehension
            final = [ui[i * n:(i + 1) * n] for i in range((len(ui) + n - 1) // n)]

            for xy in final:  # get the first 30 images

                img_width, img_height = Image.open(xy[0]).size
                sf = (frame_width - (images_per_row - 1) * padding) / (images_per_row * img_width)  # scaling factor
                scaled_img_width = ceil(img_width * sf)  # s
                scaled_img_height = ceil(img_height * sf)

                number_of_rows = ceil(len(xy) / images_per_row)
                frame_height = ceil(sf * img_height * number_of_rows)

                new_im = Image.new('RGB', (frame_width, frame_height))

                i, j = 0, 0
                for num, im in enumerate(xy):
                    if num % images_per_row == 0:
                        i = 0
                    im = Image.open(im)
                    # Here I resize my opened image, so it is no bigger than 100,100
                    im.thumbnail((scaled_img_width, scaled_img_height))
                    # Iterate through a 4 by 4 grid with 100 spacing, to place my image
                    y_cord = (j // images_per_row) * scaled_img_height
                    new_im.paste(im, (i, y_cord))

                    i = (i + scaled_img_width) + padding
                    j += 1

                new_im.show()
                new_im.save(f"out {random.random()}.pdf", "PDF", save_all=True, resolution=300, quality=100,
                            optimize=True, progressive=True)

        j1()
        j2()
        j3()
        print(os.getcwd())
        os.chdir("../")
        os.chdir("../")


        def j4():
            files = glob.glob('./bar/*png')

            for f in files:
                try:
                    os.remove(f)
                except OSError as e:
                    print("Error: %s : %s" % (f, e.strerror))

        def j5():
            files = glob.glob('./bar/final/*png')

            for f in files:
                try:
                    os.remove(f)
                except OSError as e:
                    print("Error: %s : %s" % (f, e.strerror))


        j4()
        j5()
    def create_admin(self):
        if self.ui.username_create.text() and self.ui.password_create.text():
            print(self.ui.username_create.text())
            self.hash=hashlib.sha256(str.encode(self.ui.password_create.text())).hexdigest()
            sql="INSERT INTO Login(username,password,Admin) VALUES(?,?,'y')"
            b=c.execute(sql,(self.ui.username_create.text(),self.hash))
            conn.commit()
    def create_employee(self):
        if self.ui.username_create.text() and self.ui.password_create.text():
            sql="INSERT INTO Login(username,password,Admin) VALUES(?,?,'n')"
            b=c.execute(sql,(self.ui.username_create.text(),self.hash))
            conn.commit()
    def user_table(self):
        query = "SELECT username,Admin FROM Login"
        result = c.execute(query)
        self.ui.user_table1.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.ui.user_table1.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.user_table1.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def clear_username(self):
        sql = c.execute("DELETE FROM Login WHERE id!=1")
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'Login' ")
        conn.commit()
    def clear_single_user(self):
        sql = c.execute("DELETE FROM Login WHERE username=?",(self.ui.username_single.text(),),)
        sql1 = c.execute("DELETE FROM SQLITE_SEQUENCE WHERE NAME = 'Login' ")
        conn.commit()


    ##MOUSE####
    def sideleftmenu(self):
        # current menu width
        width = self.ui.left_main_frame.width()
        if width == 50:
            new_width = 150
        else:
            new_width = 50

        self.animation = QPropertyAnimation(self.ui.left_main_frame, b"minimumWidth")

        self.animation.setDuration(100)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        QtGui.QGuiApplication.processEvents()
        ############################################################################################################


# Execute app
#
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    sys.exit(app.exec_())
else:
    print(__name__, "hh")

# press ctrl+b in sublime to run
