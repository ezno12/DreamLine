import sys
from app.app import db
class Todo():
    """ 
    """
    class Being():
        Dream = ""
        Cost = int()
        Cost_Type = "Monthly" or "One-Time"
        def __init__(self,Dream,Cost,Cost_Type):
            self.Dream = Dream
            self.Cost = Cost
            self. Cost_Type = Cost_Type
            if self.Cost_Type == "monthly":
                return(self.Cost * 6) 
            else:
                return(self.Cost)

    class Having(Being):

        def __init__(self,Dream,Cost,Cost_Type):
            self.Dream = Dream
            self.Cost = Cost
            self. Cost_Type = Cost_Type
            if self.Cost_Type == "monthly":
                return(self.Cost * 6) 
            else:
                return(self.Cost)

    class Doing(Being):

        def __init__(self,Dream,Cost,Cost_Type):
            self.Dream = Dream
            self.Cost = Cost
            self. Cost_Type = Cost_Type
            if self.Cost_Type == "monthly":
                return(self.Cost * 6) 
            else:
                return(self.Cost)

    class Monthly_expenses():
        expense = "category"
        monthly_cost = int()
        def __init__(self,expense,monthly_cost):
            self.expense = expense
            self.monthly_cost = monthly_cost
            return(monthly_cost * 1.3)

    def __repr__(self):
        self.Target_Monthly_Income = "{} = {} + {} + {} + {}".format(Todo.Being.Cost + Todo.Having.Cost + Todo.Doing.Cost,
                                                                Todo.Having.Cost,
                                                                Todo.Being.Cost,
                                                                Todo.Doing.Cost,
                                                                Todo.Monthly_expenses.monthly_cost * 1.3)

        self.Target_Daily_Income = "{}".format((Todo.Being.Cost + Todo.Having.Cost + Todo.Doing.Cost) / 30)

