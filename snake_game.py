import tkinter as tk
import random


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Classic Snake Game")
        self.geometry("500x500")
    

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # label
        self.label = tk.Label(self, text='Classic Snake Game')
        self.label.config(font=("Courier", 20))
        self.label.pack()

        # button
        self.play_button = tk.Button(self, text='Play Game')
        self.play_button['command'] = self.play_game
        self.play_button.pack()
        
        self.exit_button = tk.Button(self, text='Exit')
        self.exit_button['command'] = container.destroy
        self.exit_button.pack()        

        # show the frame on the container
        self.pack()
        self.canvas = tk.Canvas(container, height=300, width=300)
        self.canvas.pack()
        self.move = 1

    def play_game(self):
        if (self.move == 0):
            self.play_again.pack_forget()
            self.score_mess.pack_forget()
            self.score_label.pack_forget()
        self.play_button.pack_forget()
        self.exit_button.pack_forget()
        self.label.pack_forget()
        self.x = 5
        self.y = 0
        self.prev_x = 5
        self.prev_y = 0
        self.lead_x = 50
        self.lead_y = 50
        self.size = 1
        self.lead = self.canvas.create_oval(self.lead_x, self.lead_y, self.lead_x + 20, self.lead_y + 20, outline="#f11", fill="#1f1", width=2)
        self.snake = [self.lead]
        self.food_x = random.randint(0, 245)
        self.food_y = random.randint(0, 245)
        self.food = self.canvas.create_oval(self.food_x, self.food_y, self.food_x + 20, self.food_y + 20, fill="#1f1")
        self.canvas.create_line(3, 3, 3, 300)
        self.canvas.create_line(3, 3, 300, 3)
        self.canvas.create_line(300, 3, 300, 300)
        self.canvas.create_line(3, 300, 300, 300)
        self.move = 1
        self.movement()
        
    def movement(self):
      
        # This is where the move() method is called
        # This moves the rectangle to x, y coordinates
        #for i in range(self.size):
            #self.canvas.move(self.snake[i], self.x, self.y)
        if (self.lead_x <= 3 or self.lead_y <= 3 or self.lead_x + 20 >= 300 or self.lead_y + 20 >= 300):
            self.canvas.delete('all')
            
            score = tk.StringVar()
            score.set(str(self.size))
            self.score_mess = tk.Label(self, text='Your score was:')
            self.score_mess.config(font=("Courier", 20))
            self.score_mess.pack()
            
            self.score_label = tk.Label(self, text=score.get())
            self.score_label.config(font=("Courier", 20))
            self.score_label.pack()
            
            self.play_again = tk.Button(self, text='Play Again?')
            self.play_again['command'] = self.play_game
            self.play_again.pack()            
                       
            self.move = 0
            
        i = 5
        hit = 0
        if (self.move == 1):
            if ((self.prev_x == self.x * (-1) and self.x != 0 or self.prev_y == self.y * (-1) and self.y != 0) and self.size > 1):
                self.canvas.delete('all')
                score = tk.StringVar()
                score.set(str(self.size))
                self.score_mess = tk.Label(self, text='Your score was:')
                self.score_mess.config(font=("Courier", 20))
                self.score_mess.pack()
                
                self.score_label = tk.Label(self, text=score.get())
                self.score_label.config(font=("Courier", 20))
                self.score_label.pack()
                
                self.play_again = tk.Button(self, text='Play Again?')
                self.play_again['command'] = self.play_game
                self.play_again.pack()            
                           
                self.move = 0
                hit = 1                
            while (i < self.size and hit == 0):
                coord = self.canvas.coords(self.snake[i])
                if ((coord[0] <= self.lead_x <= coord[0] + 10 or self.lead_x <= coord[0] <= self.lead_x + 10) and (coord[1] <= self.lead_y <= coord[1] + 10 or self.lead_y <= coord[1] <= self.lead_y + 10)):
                    self.canvas.delete('all')
                    score = tk.StringVar()
                    score.set(str(self.size))
                    self.score_mess = tk.Label(self, text='Your score was:')
                    self.score_mess.config(font=("Courier", 20))
                    self.score_mess.pack()
                    
                    self.score_label = tk.Label(self, text=score.get())
                    self.score_label.config(font=("Courier", 20))
                    self.score_label.pack()
                    
                    self.play_again = tk.Button(self, text='Play Again?')
                    self.play_again['command'] = self.play_game
                    self.play_again.pack()            
                               
                    self.move = 0
                    hit = 1
                i += 1
                      
        if (self.move == 1):
            for i in range(self.size - 1, 0, -1):
                new_coords = self.canvas.coords(self.snake[i - 1])
                old_coords = self.canvas.coords(self.snake[i])
                self.canvas.move(self.snake[i], new_coords[0] - old_coords[0], new_coords[1] - old_coords[1])        
            self.canvas.move(self.lead, self.x, self.y)
            self.lead_x += self.x
            self.lead_y += self.y
            self.canvas.after(100, self.movement)
            if ((self.food_x <= self.lead_x <= self.food_x + 20 or self.lead_x <= self.food_x <= self.lead_x + 20) and (self.food_y <= self.lead_y <= self.food_y + 20 or self.lead_y <= self.food_y <= self.lead_y + 20)):
                #if (self.x == -5 and self.y == 0):
                new = self.canvas.create_oval(300, 300, 300 + 20, 300 + 20, outline="#f11", fill="#1f1", width=2)
                self.snake.append(new)
                self.size += 1            
                self.canvas.delete(self.food)
                self.food_x = random.randint(3, 280)
                self.food_y = random.randint(3, 280)
                self.food = self.canvas.create_oval(self.food_x, self.food_y, self.food_x + 20, self.food_y + 20, fill="#1f1")
            
        #for i in range(self.size - 1):
            #new_coords = self.canvas.coords(self.snake[i])
            #old_coords = self.canvas.coords(self.snake[i + 1])
            #self.canvas.move(self.snake[i + 1], new_coords[0] - old_coords[0], new_coords[1] - old_coords[1])
                
          
    # for motion in negative x direction
    def left(self, event):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = -5
        self.y = 0
          
    # for motion in positive x direction
    def right(self, event):
        self.prev_x = self.x
        self.prev_y = self.y        
        self.x = 5
        self.y = 0
          
    # for motion in positive y direction
    def up(self, event):
        self.prev_x = self.x
        self.prev_y = self.y        
        self.x = 0
        self.y = -5
          
    # for motion in negative y direction
    def down(self, event):
        self.prev_x = self.x
        self.prev_y = self.y        
        self.x = 0
        self.y = 5    
    

if __name__ == "__main__":
    app = App()
    frame = MainFrame(app)
    # This will bind arrow keys to the tkinter
    # toplevel which will navigate the image or drawing
    app.bind("<KeyPress-Left>", lambda e: frame.left(e))
    app.bind("<KeyPress-Right>", lambda e: frame.right(e))
    app.bind("<KeyPress-Up>", lambda e: frame.up(e))
    app.bind("<KeyPress-Down>", lambda e: frame.down(e))    
    app.mainloop()