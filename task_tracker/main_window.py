from PySide6 import QtWidgets, QtCore
from .plan import Plan

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spooky Tracer")

        self.planLandingPage = QtWidgets.QWidget()

        self.plans = []

        # Create a container widget to hold the pages
        self.pageContainer = QtWidgets.QWidget()

        # Create the pages and buttons of the main window
        self.menuPage = QtWidgets.QWidget()
        self.statsPage = QtWidgets.QWidget()
        self.menuButton = QtWidgets.QPushButton("Menu")
        self.statsButton = QtWidgets.QPushButton("Stats")


        # Create buttons and pages for the menu page
        self.createPage = QtWidgets.QWidget()
        self.choosePage = QtWidgets.QWidget()
        self.createButton = QtWidgets.QPushButton("Create a Plan")
        self.chooseButton = QtWidgets.QPushButton("Choose a Plan") # dropdown menu to choose a plan
        self.createBackButton = QtWidgets.QPushButton("Back")
        self.chooseBackButton = QtWidgets.QPushButton("Back")

        # Create a stacked widget to hold the pages of the main window
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.stackedWidget.addWidget(self.menuPage)
        self.stackedWidget.addWidget(self.statsPage)


        # Create a stacked widget to hold the pages of the menu page
        self.planStackedWidget = QtWidgets.QStackedWidget()


        # Set up the layout for the buttons of the main window
        buttonRow = QtWidgets.QHBoxLayout()
        buttonRow.addWidget(self.menuButton)
        buttonRow.addWidget(self.statsButton)

        # Set up the layout for the page container
        self.pageContainer.setLayout(QtWidgets.QVBoxLayout())
        self.pageContainer.layout().addLayout(buttonRow)
        self.pageContainer.layout().addWidget(self.stackedWidget)

        # Set the page container as the central widget of the main window
        self.setCentralWidget(self.pageContainer)

        self.planLandingPage.setLayout(QtWidgets.QVBoxLayout())    
        self.planStackedWidget.addWidget(self.planLandingPage)
        self.planStackedWidget.addWidget(self.createPage)
        self.planStackedWidget.addWidget(self.choosePage)
        self.planLandingPage.layout().addWidget(self.createButton)
        self.planLandingPage.layout().addWidget(self.chooseButton)

        # Set up the layout for the menu page
        self.menuPage.setLayout(QtWidgets.QVBoxLayout())
        self.menuPage.layout().addStretch()
        self.menuPage.layout().addWidget(self.planStackedWidget)
        self.menuPage.layout().addStretch()

        # Set up the layout for the create page
        self.createPlan = QtWidgets.QComboBox()
        self.createPlan.addItem("Roblox")
        self.createPlan.addItem("Brave")

        self.createPage.setLayout(QtWidgets.QVBoxLayout())
        self.createPage.layout().addStretch()
        self.createPage.layout().addWidget(self.createBackButton)
        self.createPage.layout().addWidget(self.createPlan)
        self.createPage.layout().addStretch()

        # Set up the layout for the choose page
        self.choosePlan = QtWidgets.QComboBox()
        self.choosePlan.addItem("Study")
        self.choosePlan.addItem("Gaming")

        self.choosePage.setLayout(QtWidgets.QVBoxLayout())
        self.choosePage.layout().addStretch()
        self.choosePage.layout().addWidget(self.chooseBackButton)
        self.choosePage.layout().addStretch()
        self.choosePage.layout().addWidget(self.choosePlan)
        self.choosePage.layout().addStretch()


        # Connect the buttons to their respective functions
        self.menuButton.clicked.connect(self.show_menu_page)
        self.statsButton.clicked.connect(self.show_stats_page)
        self.createButton.clicked.connect(self.show_create_page)
        self.chooseButton.clicked.connect(self.show_choose_page)
        self.createBackButton.clicked.connect(self.show_plan_landing_page)
        self.chooseBackButton.clicked.connect(self.show_plan_landing_page)



    def show_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.menuPage)


    def show_stats_page(self):
        self.stackedWidget.setCurrentWidget(self.statsPage)
        

    def show_create_page(self):
        self.planStackedWidget.setCurrentWidget(self.createPage)
        

    def show_choose_page(self):
        self.planStackedWidget.setCurrentWidget(self.choosePage)

    def show_plan_landing_page(self):
        self.planStackedWidget.setCurrentWidget(self.planLandingPage)