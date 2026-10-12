class TextEditor:
    def __init__(self):
        # 1. 当前文本
        self.text = ""
        # 2. 历史栈（存过去的版本）
        self.undo_stack = []
        # 3. 重做栈（存未来的版本）
        self.redo_stack = []

    def write(self, new_text):
        # 写入新内容前，先把“当前内容”存入历史栈
        self.undo_stack.append(self.text)
        # 更新当前内容
        self.text = new_text
        # 关键点：写了新东西，就代表“未来”被改变了，清空重做栈
        self.redo_stack.clear()

    def undo(self):
        # 如果历史栈是空的，说明没有过去的版本可以撤销了
        if not self.undo_stack:
            return "没有可撤销的操作"
        
        # 把“当前内容”存入重做栈（相当于把当前这一刻存进“未来备忘录”）
        self.redo_stack.append(self.text)
        # 从历史栈弹出上一个版本，变成当前内容
        self.text = self.undo_stack.pop()
        return self.text

    def redo(self):
        # 如果重做栈是空的，说明没有“未来”可以重做了
        if not self.redo_stack:
            return "没有可重做的操作"
        
        # 把“当前内容”存回历史栈
        self.undo_stack.append(self.text)
        # 从重做栈弹出未来的版本，变成当前内容
        self.text = self.redo_stack.pop()
        return self.text

    def show(self):
        return self.text