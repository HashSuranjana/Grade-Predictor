# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution

# Student ID - w1956402 / 20221435
# Date  - 7 th December 2022

count_progress = 0
count_trailer   =   0
count_retriever  = 0
count_exclude = 0

list_1 = [ count_progress  , count_trailer  , count_retriever  , count_exclude   ]   # list for storing the looping count of the outputs .

def validation ( message , maximum = None , minimum = None , error_message = "Integer Required..... " ) :  # User Defined Function for Integer Validation

    tuple_1 = ( 0 , 20 , 40 , 60 , 80 , 100 , 120 )

    while True :

        try :

            entry = int ( input ( message ) )

            if ( ( entry > maximum ) or ( entry not in tuple_1 ) ) : # Check the entered value is in the range and in the tuple

                print ( "Out Of Range. " )

                continue

            if ( ( entry < minimum ) or ( entry not in tuple_1 ) ) : # Check the entered value is in the range and in the tuple

                print ( "Out Of Range. " )

                continue
            
            break

        except ValueError :

            print ( error_message )

    return entry

def desire_check ( message , error , choise_1 , choice_2 ) :

    while True  :

                desire = input ( message ).lower ( )       # To get the input whether user continue or exit.

                if ( desire == choise_1 ) :

                    break

                elif ( desire == choice_2 ) :

                    break

                else :

                    print ( error )

                    continue

    return desire

def decorations ( variable , option ) :   # User Defined Function to decorate the output and reduce the repition of codes.

    print ( "--" * 36 ) 

    print ( option, variable )

    print ( "--" * 36 )

dict_1 = { }  # Empty Dictionary

while True :

    student_ID =  input ( "Enter Student ID number : " )  # Ask user to enter student ID number

    pass_entry =  validation  ( "Please enter your credits at pass : "  , 120 , 0 ,  )
    defer_entry =  validation  ( "Please enter your credits at defer : "  , 120 , 0 ,  )
    fail_entry    =  validation  ( "Please enter your credits at fail    : "  , 120 , 0 ,  )

    Total = pass_entry + defer_entry + fail_entry      # Get the total of the user entries

    if ( Total != 120 ) :

        print ( "Total Incorrect !!! " )

    else :

        if ( pass_entry == 120  ) :

            printings_1 = decorations ( "Progress" , "\t" )

            dict_2_0 =  { "Progress" : [ 120 ,0 ,0 ] }

            dict_1.update ( { student_ID : dict_2_0 } )  # Add dict_2_0 to dict_1
            
        elif  ( pass_entry == 100 )  :

            printings_2 = decorations ( "Progress (module trailer)" , "\t" )

            dict_2_1 = { "Progress ( module trailer )" : [ 100 , defer_entry , fail_entry ] }

            dict_1.update ( { student_ID : dict_2_1 } )  # Add dict_2_1 to dict_1

        elif  ( ( pass_entry != ( 100 or 120 ) ) and ( pass_entry + defer_entry >= fail_entry ) ) :

            printings_3 =  decorations ( "Module Retriever " , "\t" )

            dict_2_2 = { "Module Retriever " : [ pass_entry , defer_entry , fail_entry ] }

            dict_1.update ( { student_ID : dict_2_2 } )  # Add dict_2_2 to dict_1 

        elif ( pass_entry + defer_entry <  fail_entry ) :

            printings_4 = decorations ( "Exclude " , "\t" )

            dict_2_3 = { "Exclude " : [ pass_entry , defer_entry , fail_entry ] }

            dict_1.update ( { student_ID : dict_2_3 } )  # Add dict_2_3 to dict_1

    desire_1 = desire_check ( "\nWould you like to enter another set of data ? \n   Enter 'y' for yes or 'q' to quit and view results : " ,"...............Please enter 'y' or 'q' ..............." ,'y' ,'q' )

    if ( desire_1 == 'y' ) : # Continue the outer while loop

        continue

    elif ( desire_1 == 'q' ) :  # Exit from the outer while loop

        break
    
print ( "\nPart : 4  \n " )

for keys in dict_1.keys ( )  :  # To iterate keys in dict_1

    print ( keys , " : " , end = "" )

    for elements in dict_1[ keys ]  :  # To iterate keys in dict_2

        print ( elements , end = "-  " )

        for data in dict_1[keys][elements]  : # To iterate list which is stored as values in dict_2

            print ( data , end = " , "  )

    print ( "\n" )

   

    

    




