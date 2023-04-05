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
    
    def draw(self):
        if(self.has_left_wall):
            if(self._x1 != None and self._y1 != None):
                first_point = Point(self._x1,0)
                second_point = Point(0, self._y1)
                line = Line(first_point,second_point)
                line.draw(self._win.get_canvas(), "red")

        if(self.has_right_wall):
            if(self._x2 != None and self._y2 != None):
                first_point = Point(self._x2,0)
                second_point = Point(0, self._y2)
                line = Line(first_point,second_point)
                line.draw(self._win.get_canvas(), "red")

        if(self.has_top_wall):
            if(self._y1 != None and self._y2 != None):
                first_point = Point(0, self._y1)
                second_point = Point(0, self._y2)
                line = Line(first_point,second_point)
                line.draw(self._win.get_canvas(), "red")
            
        if(self.has_bottom_wall):
            if(self._x1 != None and self._x2 != None):
                first_point = Point(self._x1, 0)
                second_point = Point(self._x2, 0)
                line = Line(first_point,second_point)
                line.draw(self._win.get_canvas(), "red")

#Main function
def main():
    win = Window(300, 300)
    # tests for line drawing
    # first_point  = Point(10, 20)
    # second_point = Point(20, 40)

    # for iterator in range(10):
    #     first_point = Point(2 * iterator, 5 * iterator)
    #     second_point = Point(7 *  iterator, 12 * iterator)
    # cell = Cell(True, True, True, True, 10, 100, 50, 100, win)
    # cell.draw()
    # win.wait_for_close()
    first_point = Point(0, 0)
    second_point = Point(0, 0)
    line =  Line(first_point, second_point)
    line.draw(win.get_canvas(), "red")
    win.wait_for_close()

main()