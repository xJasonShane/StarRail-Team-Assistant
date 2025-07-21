import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    try:
        print("测试应用程序启动...")
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle("启动测试")
        window.resize(400, 300)
        window.show()
        print("应用程序启动成功")
        sys.exit(app.exec_())
    except Exception as e:
        print(f"启动失败: {str(e)}", file=sys.stderr)
        sys.exit(1)