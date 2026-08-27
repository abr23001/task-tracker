from PySide6 import QtWidgets, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spooky Tracer")

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


        # Create a stacked widget to hold the pages of the main window
        self.stackedWidget = QtWidgets.QStackedWidget()
        self.stackedWidget.addWidget(self.menuPage)
        self.stackedWidget.addWidget(self.statsPage)


        # Create a stacked widget to hold the pages of the menu page
        self.planStackedWidget = QtWidgets.QStackedWidget()
        self.planStackedWidget.addWidget(self.createPage)
        self.planStackedWidget.addWidget(self.choosePage)


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


        # Set up the layout for the menu page
        self.menuPage.setLayout(QtWidgets.QVBoxLayout())
        self.menuPage.layout().addStretch()
        self.menuPage.layout().addWidget(self.createButton)
        self.menuPage.layout().addWidget(self.chooseButton)
        self.menuPage.layout().addWidget(self.planStackedWidget)
        self.menuPage.layout().addStretch()


        # Connect the buttons to their respective functions
        self.menuButton.clicked.connect(self.show_menu_page)
        self.statsButton.clicked.connect(self.show_stats_page)
        self.createButton.clicked.connect(self.show_create_page)
        self.chooseButton.clicked.connect(self.show_choose_page)




    def show_menu_page(self):
        self.stackedWidget.setCurrentWidget(self.menuPage)


    def show_stats_page(self):
        self.stackedWidget.setCurrentWidget(self.statsPage)
        

    def show_create_page(self):
        self.planStackedWidget.setCurrentWidget(self.createPage)
        

    def show_choose_page(self):
        self.planStackedWidget.setCurrentWidget(self.choosePage)
        