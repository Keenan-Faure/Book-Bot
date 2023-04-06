from tkinter import Tk, BOTH, Canvas
from tkinter.messagebox import askokcancel, showinfo, WARNING
from tkinter import Menu

#Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Line
class Line:
    def __init__(self, first_point: Point, second_point: Point):
        self.first_point  = first_point
        self.second_point = second_point

    def draw(self, Canvas: Canvas, fill_color: str):
        Canvas.create_line(
            # adding 2 because the width is initially 1
            # hence if the point is located < width length it 
            # will not show on Canvas
            (self.first_point.x + 3), (self.first_point.y + 3), 
            (self.second_point.x + 3), (self.second_point.y + 3), 
            fill=fill_color, width=1
        )
        Canvas.pack()

#Window
class Window(Tk):

    # private root Tk
    # private canvas Canvas
    # private running Boolean
    def __init__(self, width: int, height: int):
        super().__init__()

        self.__root = Tk()
        self.__root.config(width=width, height=height)
        self.__root.title("Maze Runner Solution")

        #Canvas
        self.__canvas = Canvas(self.__root,bg = "black",height=height)
        self.__canvas.pack()
        self.__running = False

        #connects your close method to the "delete window" action
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        #Optional menu
        # menu = Menu(self.__root)
        # self.__root.config(menu=menu)

        # file = Menu(menu)
        # file.add_command(label="Exit", command=self.close)

        # menu.add_cascade(label="File", menu=file)

        # edit = Menu(menu)
        # edit.add_command(label="Undo")

        # menu.add_cascade(label="Edit", menu=edit)
    
    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.__running = True

        #continuously updates the windows
        while(self.__running == True):
            self.redraw()
    
    def close(self):
        # answer = askokcancel(
        #     title='Confirmation',
        #     message='Close application?',
        #     icon=WARNING)

        # #closes the application if 'Yes'
        # if answer:
        #     showinfo(
        #         title='Termination Status',
        #         message='The app was closed successfully')
        self.__running = False
    
    def draw_line(self, Line: Line, fill_color):
        Line.draw(self.__canvas, fill_color)
    
    def get_canvas(self):
        return self.__canvas

#Cell
class Cell:
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, _x1, _x2, _y1, _y2, _win: Window):
        self.has_left_wall   = has_left_wall
        self.has_right_wall  = has_right_wall
        self.has_top_wall    = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1             = _x1
        self._x2             = _x2
        self._y1             = _y1
        self._y2             = _y2
        self._win            = _win
    
    def update_points(self, top_left_x1, top_left_y1, bottom_right_x1, bottom_right_y1):
        self._x1 += top_left_x1
        self._y1 += top_left_y1
        self._x2 += bottom_right_x1
        self._y2 += bottom_right_y1
    
    def draw_move(self, to_cell, undo=False):
        #gets mid points for two cells
        p1_mid_point = self.calc_midpoint()
        to_cell_mid_point = to_cell.calc_midpoint()

        #creates and draws the lines
        line = Line(p1_mid_point,to_cell_mid_point)
        if(undo == None):
            line.draw(self._win.get_canvas(), "red")
        else:
            line.draw(self._win.get_canvas(), "grey")

    def calc_midpoint(self):
        x_1 = (self._x1 + self._x2) / 2
        y_1 = (self._y1 + self._y2) / 2
        mid_point = Point(x_1, y_1)
        return mid_point
        
    def draw(self, top_left_x1, top_left_y1, bottom_right_x1, bottom_right_y1):
        # self.update_points(top_left_x1, top_left_y1, bottom_right_x1, bottom_right_y1)

        if(self.has_left_wall):
            first_point = Point(self._x1, top_left_y1)
            second_point = Point(self._x2, self._y2)
            line = Line(first_point,second_point)
            line.draw(self._win.get_canvas(), "red")

        if(self.has_right_wall):
            first_point = Point(top_left_x1,self._y1)
            second_point = Point(bottom_right_x1, bottom_right_y1)
            line = Line(first_point,second_point)
            line.draw(self._win.get_canvas(), "red")

        if(self.has_top_wall):
            first_point = Point(self._x1, self._y1)
            second_point = Point(bottom_right_x1, self._y2)
            line = Line(first_point,second_point)
            line.draw(self._win.get_canvas(), "red")
            
        if(self.has_bottom_wall):
            first_point = Point(self._x1, top_left_y1)
            second_point = Point(bottom_right_x1, bottom_right_y1)
            line = Line(first_point,second_point)
            line.draw(self._win.get_canvas(), "red")

#Main function
def main():
    win = Window(300, 300)

    # cell format is left, right, top, bottom
    # draw format is 
    # top_left_x, top_left_y, bottom_right_x, bottom_right_y

    #to move Diagonally - increase all size + 50
    #to move to the right - increase only top_left_x & bottom_right_x + 50
    #to move downwards - increase only top_left_y & bottom_right_y + 50

    cell = Cell(True, True, True, False, 0, 0, 0, 0, win)
    cell.draw(50, 50, 50, 50)

    cell2 = Cell(True, True, False, False, 50, 50, 50, 50, win)
    cell2.draw(0, 100, 0, 100)
    cell.draw_move(cell2)

    cell3 = Cell(True, False, True, True, 100, 100, 100, 100, win)
    cell3.draw(150, 150, 150, 150)

    # cell3 = Cell(True, False, False, True, 0, 0, 0, 0, win)
    # cell3.draw(50, 100, 50, 100)

    win.wait_for_close()

main()