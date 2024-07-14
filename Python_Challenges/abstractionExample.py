from abc import ABC, abstractmethod
class homePurchase(ABC):
    def paySlip(self, amount):
        print("Your home purchase amount: ",amount)
#this function is telling us to pass in an argument, but we wont tell you how
#or what kind of data it will be.
    @abstractmethod
    def payment(self, amount):
        pass

class WireTransferPayment(homePurchase):
#here we defined how to implement the payment function from its parent payslip class.
    def payment(self, amount):
        print('Your purchase amount of {} exceeded your approved mortage limit of $550,000'.format(amount))

obj = WireTransferPayment()
obj.paySlip("$700,000")
obj.payment("$700,000")
        
