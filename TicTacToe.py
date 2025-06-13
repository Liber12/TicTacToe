import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")  # ウィンドウタイトルを設定
        self.current_player = "X"  # 現在のプレイヤー
        self.board = [["" for _ in range(3)] for _ in range(3)]  # 盤面の初期化
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # ボタンの格納用
        self.create_widgets()  # ウィジェットの作成

    def create_widgets(self):
        # 3x3のボタンを作成
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn
        # ステータス表示用ラベル
        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def on_click(self, row, col):
        # クリック時の処理
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player  # 盤面を更新
            self.buttons[row][col].config(text=self.current_player)  # ボタンの表示を更新
            winner = self.check_winner()  # 勝者の判定
            if winner:
                self.status_label.config(text=f"Player {winner} wins!")  # 勝者表示
                self.disable_buttons()  # ボタンを無効化
            elif all(all(cell != "" for cell in row) for row in self.board):
                self.status_label.config(text="It's a draw!")  # 引き分け表示
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # プレイヤー交代
                self.status_label.config(text=f"Player {self.current_player}'s turn")  # 次のターン表示

    def check_winner(self):
        # 勝者判定
        lines = self.board + [list(col) for col in zip(*self.board)]  # 横と縦
        lines.append([self.board[i][i] for i in range(3)])  # 斜め（左上から右下）
        lines.append([self.board[i][2 - i] for i in range(3)])  # 斜め（右上から左下）
        for line in lines:
            if line[0] != "" and all(cell == line[0] for cell in line):
                return line[0]  # 勝者を返す
        return None  # 勝者なし

    def disable_buttons(self):
        # 全てのボタンを無効化
        for row in self.buttons:
            for btn in row:
                btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()