#CAP 2: Personal Income Tax Calculations and validations. 
class TaxCalculator:
    """
    A class to calculate personal income tax based on the given information.
    """
#Below are the demographic form of questions as the basic information are needed with which one will calculate the Tax Payable account. 
    def init(self):
        self.name = None
        self.age = None
        self.org_type = None
        self.emp_type = None
        self.marital_status = None
        self.salary = None
        self.no_of_children = 0
        self.school_going_children = 0

    def get_user_input(self):
        """
        Prompt the user to enter personal information and income details.
        """
        try:
            self.name = input("Enter your name: ")
            self.age = int(input("Enter your age: "))
            self.org_type = input("Enter your organization type (Government, Private, Corporate): ")
            self.emp_type = input("Enter your employment type (Regular, Contract): ")
            self.marital_status = input("Enter your marital status (Married, Single): ")
            self.salary = float(input("Enter your annual salary: "))

            if self.marital_status.lower() == "married":
                self.no_of_children = int(input("How many children do you have? "))
                self.school_going_children = int(input("How many of them are going to school? "))
        except ValueError:
            print("Invalid input. Please enter valid values.")
#In order to calculate tax,  the below are the information that should be in mind while calculation. since the assignmentg requires to follow the OOP guidelines, we use the feature of encapsulation while performin g the tax deduction function. 
    def calculate_tax(self):
        """
        Calculate the personal income tax based on the provided information.
        """
        # Deductibles
        nppf_deduction = self.calculate_nppf_deduction()
        gis_deduction = self.calculate_gis_deduction()
        child_deduction = self.calculate_child_deduction()

        # Taxable income
        taxable_income = self.salary - nppf_deduction - gis_deduction - child_deduction

        # Tax calculation based on income slabs
        tax_amount = self.calculate_tax_based_on_income_slab(taxable_income)

        # Surcharge
        surcharge = 0
        if tax_amount >= 1000000:
            surcharge = tax_amount * 0.1

        total_tax = tax_amount + surcharge

        return total_tax
#it is very important to consider all the required and necessary reductions before computing the amount for tax. 
    def calculate_nppf_deduction(self):
        """
        Calculate the deduction for NPPF (Pension Scheme/Provident Fund).
        """
        if self.emp_type.lower() == "regular" and self.org_type.lower() == "government":
            return 0.1 * self.salary
        elif self.org_type.lower() in ["private", "corporate"]:
            return 0.1 * self.salary
        else:
            return 0
#Below Describes another Deduction. 
    def calculate_gis_deduction(self):
        """
        Calculate the deduction for GIS (Group Insurance Scheme).
        """
        if self.org_type.lower() == "government":
            return 0.01 * self.salary
        else:
            return 0
#Children being a valid characteristics while computing tax, the below code describes the necessary tax deductions available if the employee has children/ Child. 
    def calculate_child_deduction(self):
        """
        Calculate the deduction for children's education.
        """
        deduction = 0
        if self.school_going_children > 0:
            deduction = min(self.school_going_children * 350000, 350000)
        return deduction
#Below is the income pay slab and it is very important. this becomes a condition for my encapsulation which is directed to abstract the tax filing. 
    def calculate_tax_based_on_income_slab(self, taxable_income):
        """
        Calculate the tax amount based on the income slabs.
        """
        tax_amount = 0
        if taxable_income <= 300000:
            tax_amount = 0
        elif taxable_income <= 400000:
            tax_amount = (taxable_income - 300000) * 0.1
        elif taxable_income <= 650000:
            tax_amount = 10000 + (taxable_income - 400000) * 0.15
        elif taxable_income <= 1000000:
            tax_amount = 52500 + (taxable_income - 650000) * 0.2
        elif taxable_income <= 1500000:
            tax_amount = 122500 + (taxable_income - 1000000) * 0.25
        else:
            tax_amount = 247500 + (taxable_income - 1500000) * 0.3

        return tax_amount
    
# Example 1
tax_calculator = TaxCalculator()
tax_calculator.get_user_input()
total_tax = tax_calculator.calculate_tax()
print(f"Total tax payable: Nu. {total_tax:.2f}")

def calculate_education_allowance(num_children, income):
    """
    Calculates the education allowance for children.
    
    Args:
        num_children (int): The number of children.
        income (float): The total adjusted gross income.
        
    Returns:
        float: The education allowance for children.
    """
    max_allowance_per_child = 350000
    total_allowance = 0
    
    for i in range(num_children):
        allowance = min(max_allowance_per_child, income)
        total_allowance += allowance
        income -= allowance
    
    return total_allowance

# Example 2
num_children = 2
income = 1000000

education_allowance = calculate_education_allowance(num_children, income)
print(f"Education allowance for children: Nu. {education_allowance}")

def calculate_premium(insurance_scheme, premium_amount):
    # List of insurance schemes with 100% deduction
    full_deduction_schemes = [
        "Limited Payment Life Insurance",
        "Silver Jubilee Term Insurance",
        "Term Insurance",
        "New Life Annity Scheme"
    ]

    # List of insurance schemes with 50% deduction (Examples)
    half_deduction_schemes = [
        "Double Endowment",
        "Double Covver Endowment",
        "Education Annuity",
        "Children Anticipated Policy",
        "Endowment Assurance",
        "Money Back Policy",
        "Ashi Nangsa Living Policy",
        "Millennium Education Policy",
        "Endowment Assurance Plan for Minors",
        "Endowment Cover Endowment Planwithout profit",
        "Drongseb Kuendrel Tshe-sog Ngensung",
        "Endowment Plan for Seniour Citizenswith guarnateed additions",
        "Pho-Mo Joint Life Endowment Assurance",
        "Gaki Pelzom Life Policy",
        "Ten-Tsai Mangual Ngenchoel",
        "Quendue Ngensung Life Policy"
    ]

    # Check if the insurance scheme is eligible for 100% deduction
    if insurance_scheme in full_deduction_schemes:
        deductible_amount = premium_amount
    # Check if the insurance scheme is eligible for 50% deduction
    elif insurance_scheme in half_deduction_schemes:
        deductible_amount = premium_amount * 0.5
    # If the insurance scheme is not found, assume no deduction
    else:
        deductible_amount = 0

    return deductible_amount

# Example 3
insurance_scheme = "Double Endowment"
premium_amount = 10000

deductible_premium = calculate_premium(insurance_scheme, premium_amount)
print(f"The deductible premium for {insurance_scheme} with a premium amount of {premium_amount} is {deductible_premium}")

def calculate_self_education_allowance(num_children, expenses):
    """
    Calculates the self-education allowance for children.
    
    Args:
        num_children (int): The number of children.
        expenses (list): A list of expenses for each child.
        
    Returns:
        float: The total self-education allowance.
    """
    max_allowance_per_taxpayer = 350000
    total_allowance = 0
    
    for expense in expenses:
        if expense <= max_allowance_per_taxpayer / num_children:
            total_allowance += expense
        else:
            total_allowance += max_allowance_per_taxpayer / num_children
    
    return total_allowance

# Example 4
num_children = 3
expenses = [200000, 150000, 300000]
allowance = calculate_self_education_allowance(num_children, expenses)
print(f"The total self-education allowance is: Nu. {allowance:.2f}")

def calculate_max_donation(agi):
    """
    Calculates the maximum allowable donation amount based on an adjusted gross income (AGI)
    and a maximum donation percentage of 5%.
    
    Args:
        agi (float): The adjusted gross income.
        
    Returns:
        float: The maximum allowable donation amount.
    """
    max_donation_percentage = 0.05  # 5%
    max_donation_amount = agi * max_donation_percentage
    return max_donation_amount

# Example 5
adjusted_gross_income = float(input("Enter your adjusted gross income: "))
max_allowed_donation = calculate_max_donation(adjusted_gross_income)
print(f"The maximum allowable donation amount is: Nu.{max_allowed_donation:.2f}")

def calculate_education_deduction(expenses_per_child, num_children):
    """
    Calculates the deduction for sponsored children's education expenses.
    
    Args:
        expenses_per_child (int): The education expenses for each child.
        num_children (int): The number of sponsored children.
        
    Returns:
        int: The total deduction amount for sponsored children's education expenses.
    """
    max_deduction_per_child = 350000  # Maximum deduction per child
    total_deduction = 0
    
    for child in range(num_children):
        child_expenses = expenses_per_child[child]
        deduction_amount = min(child_expenses, max_deduction_per_child)
        total_deduction += deduction_amount
    
    return total_deduction

class Employee:
    def _init_(self, salary, bonus_rate):
        self.salary = salary
        self.bonus_rate = bonus_rate

    def calculate_bonus(self):
        # Calculate the bonus based on the salary and bonus rate
        bonus = self.salary * (self.bonus_rate / 100)
        return bonus

def calculate_tax(age, income):
    tax_rate = 0.25  # Assuming a flat tax rate of 25% for simplicity
    
    if age < 18:
        tax_amount = 0
    else:
        tax_amount = income * tax_rate
    
    return tax_amount

# Example 6
person_age = int(input("Enter your age: "))
person_income = float(input("Enter your annual income: "))

tax_to_pay = calculate_tax(person_age, person_income)
print(f"Tax amount to pay: Nu.{tax_to_pay:.2f}")