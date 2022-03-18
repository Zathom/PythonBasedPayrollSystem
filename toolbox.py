# CALCULATE NET PAY FUNCTION calculates the net pay of a user based on
#provided: gp = gross pay, hr = hourly rate, hw = hours worked, fwp = federal witholding percentage
#sswp = social security withholding percentage, mwp = medicare withholding percentage,
# swp = state wittholding percentage.
#returns list of calculated data:
#returns {grossPay, netPay, calculated Fed, Calculated Social Security, calculated Medicare, calculated state.}

def calculate_net_pay(gp, hr, hw, fwp, sswp, mwp, swp):
    calculated_data = {}
    calcFed = gp * (fwp / 100)
    calcSS = gp * (sswp / 100)
    calcMed = gp * (mwp / 100)
    calcSt = gp * (swp / 100)
    netPay = gp - (calcFed + calcSS + calcMed + calcSt)

    calculated_data = {gp, netPay, calcFed, calcSS, calcMed, calcSt}
    return calculated_data

def calculate_deduction(gp, deduction_code, dp, dv):
    calculated_data = {}

    #if the fixed deduction value "dv" is > gp set calculated deduction = gp
    if dv > gp:
        calculated_deduction = gp
        #for the sake of data preservation dv is set to gp
        dv = gp
        calculated_data = {gp, deduction_code, dp, dv}
        return calculated_data
    # if deduction code is set to N meaning no deduction
    if deduction_code == 'N':
        calculated_data = {gp, deduction_code, dp, dv}
        return calculated_data
    #If deduction code is set to F meaning a fixed deduction
    if deduction_code == 'F':
        calculated_deduction = gp - dv
        calculated_data = {calculated_deduction, deduction_code, dp, dv}
        return calculated_data
    #If deduction code is set to P meaning a percentage deduction
    #NOTE this also handles extra deductions if present.
    #If there is a percentage and additional fixed deduction this if
    #statement will handle it.
    if deduction_code == 'P':
        # if deduction percentage provided is >60% set it to 60%
        if dp > 60:
            dp = 60

        # calculated deduction is a percent of gross pay
        # minus the sum of any additional deductions.
        calculated_deduction = gp * (dp / 100) - dv
        # If the total deduction calculated is greater than the gross pay
        # then set the deduction equal to the gross pay supplied to prevent
        # user owing money for labor provided.
        if calculated_deduction > gp:
            calculated_data = {calculated_deduction. deduction_code, dp, dv}
            return calculated_data

        calculated_data = {calculated_deduction, deduction_code, dp, dv}
        return calculated_data

