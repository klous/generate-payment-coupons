import json
import datetime
import dateutil.relativedelta


def lambda_handler(event, context):

    # the Loan Origination System determines the start payment date based on the close date and passes that data here
    first_payment_date = event['start_payment_date']

    term_in_months_number = int(event['number_of_payment_coupons'])
    
    payment_amount = event['payment_amount']
    lender_company = event['lender_company']
    late_charge = event['late_charge']
    property_address = event['property_address']
    
    # sets up variable that converts our date string into a format so that we can increment months 
    a_date = datetime.datetime.strptime(first_payment_date, "%Y-%m-%d")

    # sets up a month difference so that you can add
    a_month = dateutil.relativedelta.relativedelta(months=1)

    payment_date = a_date

    # converts date to the date format needed for the payment coupons
    a_date_converted = a_date.strftime("%m/%d/%Y")


    current_term = 1

    # set up the output dictionary format so that the document automation workflow can read the output
    format_output_list = [{"entry":[{"key":"paymentDueDate","value":a_date_converted},{"key":"loanPayment","value":payment_amount},{"key":"lenderName","value":lender_company},{"key":"lateChargeFee","value":late_charge},{"key":"propertyAddress","value":property_address}]}]
    
    # the number of payment coupons needed is term_in_months_number - 1, so using the range function to create the number of payment coupons
    for i in range(1, term_in_months_number):
        
        # initialize an empty current payment list or reset the list back to zero
        # current_payment_list = []
        
        # initialize an empty current_entry list or reset the list back to being empty
        current_entry = []
        
        a_month = dateutil.relativedelta.relativedelta(months=i)
        current_date = payment_date + a_month
        formatted_current_date = current_date.strftime("%m/%d/%Y")  
        
        # build the data for a single payment coupon and format it to be usable in the closing docs generation workflow
        current_entry.append({"key":"paymentDueDate", "value":formatted_current_date})
        current_entry.append({"key":"loanPayment", "value":payment_amount})
        current_entry.append({"key":"lenderName", "value":lender_company})
        current_entry.append({"key":"lateChargeFee", "value":late_charge})
        current_entry.append({"key":"propertyAddress", "value":property_address})
        
        format_output_list.append({"entry":current_entry})
        
    return_dict = {'payments_list':format_output_list}

    return {
        "statusCode": 200,
        "body": json.dumps(return_dict)
    }
