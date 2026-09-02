from PySide6 import QtWidgets, QtGui, QtCore
from .plan import Plan
import win32gui
import win32process
import psutil


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spooky Tracer")

        # --- State ---
        self.plans = []          # List to hold created plans
        self.selectedApps = []   # List to hold apps selected on the create page
        self.app_rows = {}  # Dict to map app names to their row widgets
        self.selectedIconPath = "" # Path to the selected icon file
        self.currentPlan = None
        self.foregroundCheckTimer = QtCore.QTimer(self)


        self.trayicon = QtWidgets.QSystemTrayIcon(self)
        self.setup_tray_icon()


        # Widgets: (Menu / Stats)
        self.pageContainer = QtWidgets.QWidget()
        self.menuPage = QtWidgets.QWidget()
        self.statsPage = QtWidgets.QWidget()
        self.menuButton = QtWidgets.QPushButton("Menu")
        self.statsButton = QtWidgets.QPushButton("Stats")

        # Widgets: menu page's inner pages (landing / create / choose)
        self.planLandingPage = QtWidgets.QWidget()
        self.createPage = QtWidgets.QWidget()
        self.choosePage = QtWidgets.QWidget()
        self.createButton = QtWidgets.QPushButton("Create a Plan")
        self.chooseButton = QtWidgets.QPushButton("Choose a Plan")  # dropdown menu to choose a plan
        self.createBackButton = QtWidgets.QPushButton("Back")
        self.chooseBackButton = QtWidgets.QPushButton("Back")

        # Widgets: "create a plan" form
        self.planNameInput = QtWidgets.QLineEdit(placeholderText="Coding Project")
        self.planDescription = QtWidgets.QTextEdit(placeholderText="Describe your plan")
        self.iconButton = QtWidgets.QPushButton("Choose Icon")
        self.iconPreview = QtWidgets.QLabel()
        self.iconPreview.setFixedSize(64, 64)
        self.createPlan = QtWidgets.QComboBox()
        self.savePlanButton = QtWidgets.QPushButton("Save")
        self.createPlan.addItem("Roblox")
        self.createPlan.addItem("Brave")

        self.appListContainer = QtWidgets.QWidget()
        self.appListContainer.setLayout(QtWidgets.QVBoxLayout())
        self.appListContainer.layout().addWidget(QtWidgets.QLabel("Selected Apps:"))

        # Widgets: "choose a plan" form
        self.choosePlan = QtWidgets.QComboBox()
        self.startPlanButton = QtWidgets.QPushButton("Choose")

        # Stacks
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.stackedWidget.addWidget(self.menuPage)
        self.stackedWidget.addWidget(self.statsPage)

        self.planStackedWidget = QtWidgets.QStackedWidget()
        self.planStackedWidget.addWidget(self.planLandingPage)
        self.planStackedWidget.addWidget(self.createPage)
        self.planStackedWidget.addWidget(self.choosePage)

        # Layout: top-level + central widget
        buttonRow = QtWidgets.QHBoxLayout()
        buttonRow.addWidget(self.menuButton)
        buttonRow.addWidget(self.statsButton)

        self.pageContainer.setLayout(QtWidgets.QVBoxLayout())
        self.pageContainer.layout().addLayout(buttonRow)
        self.pageContainer.layout().addWidget(self.stackedWidget)
        self.setCentralWidget(self.pageContainer)

        # Layout: menu page (just holds the plan sub-stack, centered)
        self.menuPage.setLayout(QtWidgets.QVBoxLayout())
        self.menuPage.layout().addStretch()
        self.menuPage.layout().addWidget(self.planStackedWidget)
        self.menuPage.layout().addStretch()

        # Layout: plan landing page
        self.planLandingPage.setLayout(QtWidgets.QVBoxLayout())
        self.planLandingPage.layout().addWidget(self.createButton)
        self.planLandingPage.layout().addWidget(self.chooseButton)

        # Layout: create page
        self.createPage.setLayout(QtWidgets.QVBoxLayout())
        self.createPage.layout().addStretch()
        self.createPage.layout().addWidget(self.createBackButton)
        self.createPage.layout().addWidget(self.iconButton)
        self.createPage.layout().addWidget(self.iconPreview)
        self.createPage.layout().addWidget(self.planNameInput)
        self.createPage.layout().addWidget(self.planDescription)
        self.createPage.layout().addWidget(self.createPlan)
        self.createPage.layout().addWidget(self.appListContainer)
        self.createPage.layout().addWidget(self.savePlanButton)
        self.createPage.layout().addStretch()

        # Layout: choose page
        self.choosePage.setLayout(QtWidgets.QVBoxLayout())
        self.choosePage.layout().addStretch()
        self.choosePage.layout().addWidget(self.chooseBackButton)
        self.choosePage.layout().addStretch()
        self.choosePage.layout().addWidget(self.choosePlan)
        self.choosePage.layout().addWidget(self.startPlanButton)
        self.choosePage.layout().addStretch()

        # Signal connections
        self.menuButton.clicked.connect(self.show_menu_page)
        self.statsButton.clicked.connect(self.show_stats_page)
        self.createButton.clicked.connect(self.show_create_page)
        self.chooseButton.clicked.connect(self.show_choose_page)
        self.createBackButton.clicked.connect(self.show_plan_landing_page)
        self.chooseBackButton.clicked.connect(self.show_plan_landing_page)
        self.createPlan.textActivated.connect(self.add_selected_app)
        self.iconButton.clicked.connect(self.choose_icon)
        self.savePlanButton.clicked.connect(self.save_plan)
        self.startPlanButton.clicked.connect(self.start_plan)
        self.foregroundCheckTimer.timeout.connect(self.check_foreground_app)

    # Top-level nav handlers
    def show_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.menuPage)


    def show_stats_page(self):
        self.stackedWidget.setCurrentWidget(self.statsPage)


    # Menu sub-page handlers
    def show_create_page(self):
        self.planStackedWidget.setCurrentWidget(self.createPage)


    def show_choose_page(self):
        self.planStackedWidget.setCurrentWidget(self.choosePage)


    def show_plan_landing_page(self):
        self.planStackedWidget.setCurrentWidget(self.planLandingPage)


    # App-list handlers (create page)
    def add_selected_app(self, app_name):
        if app_name not in self.selectedApps:
            self.selectedApps.append(app_name)
            rowWidget = QtWidgets.QWidget()
            rowWidget.setLayout(QtWidgets.QHBoxLayout())
            rowWidget.layout().addWidget(QtWidgets.QLabel(app_name))
            removeButton = QtWidgets.QPushButton("x")
            removeButton.clicked.connect(lambda checked, app=app_name: self.remove_selected_app(app))
            rowWidget.layout().addWidget(removeButton)
            self.appListContainer.layout().addWidget(rowWidget)
            self.app_rows[app_name] = rowWidget


    def remove_selected_app(self, app_name):
        if app_name in self.selectedApps:
            self.selectedApps.remove(app_name)
            rowWidget = self.app_rows.pop(app_name, None)
            if rowWidget:
                self.appListContainer.layout().removeWidget(rowWidget)
                rowWidget.setParent(None)
                rowWidget.deleteLater()


    def choose_icon(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Image",
                                                             "", "Image Files (*.png *.jpg *.bmp)")
        if path:
            self.selectedIconPath = path
            pixmap = QtGui.QPixmap(self.selectedIconPath)
            pixmap = pixmap.scaled(64, 64, QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)
            self.iconPreview.setPixmap(pixmap)


    def start_plan(self):
        self.currentPlan = self.choosePlan.currentData()
        if self.currentPlan:
            self.foregroundCheckTimer.start(2000)
        self.hide()

    def save_plan(self):
        name = self.planNameInput.text()
        desc = self.planDescription.toPlainText()
        icon = self.selectedIconPath
        apps = list(self.selectedApps)

        savedPlan = Plan(name=name, description=desc, icon=icon, apps=apps)
        self.plans.append(savedPlan)

        self.planNameInput.clear()
        self.planDescription.clear()
        self.selectedIconPath = ""
        self.iconPreview.clear()
        for app_name in list(self.selectedApps):
            self.remove_selected_app(app_name)

        self.show_plan_landing_page()
        self.refresh_choose_plan_dropdown()



    def refresh_choose_plan_dropdown(self):
        self.choosePlan.clear()
        for plan in self.plans:
            self.choosePlan.addItem(plan.name, userData=plan)


    def setup_tray_icon(self):
        self.trayicon.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ComputerIcon))
        self.trayicon.show()

        trayMenu = QtWidgets.QMenu()
        quitAction = QtGui.QAction("Quit", self)
        trayMenu.addAction(quitAction)
        self.trayicon.setContextMenu(trayMenu)
        quitAction.triggered.connect(QtWidgets.QApplication.instance().quit)

        self.trayicon.activated.connect(self.on_tray_activated)

    def on_tray_activated(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.ActivationReason.Trigger:
            self.show()


    def get_foreground_app_name(self):
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        try:
            return psutil.Process(pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return None

    def check_foreground_app(self):
        foreground_app = self.get_foreground_app_name()
        if foreground_app:
            print(foreground_app)