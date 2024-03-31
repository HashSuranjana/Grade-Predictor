# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution

# Student ID - w1956402 / 20221435
# Date  - 7 th December 2022

count_progress = 0
count_trailer   =    0
count_retriever  = 0
count_exclude = 0

list_1 = [ count_progress  , count_trailer  , count_retriever  , count_exclude   ]   # list for storing the looping count of the outputs .

def validations ( message , maximum = None , minimum = None , error_message = "Integer Required..... " ) :  # User Defined Function for Integer Validation

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


list_2 = [ "Progress" , "Trailer" , "Retriever" ,  "Excluded " ]

def looping ( ind_num , lists , index_1 ,index_2 ,index_3 , index_4 ) :   # User Defined Function for printing histogram 

    list_3 = [ index_1 , index_2 , index_3 , index_4 ]

    for count in ( list_3 ) :  # To loop the data in the list_2.
        
        print ( list_2 [ ind_num ] , count , ":", "*" *  ( count ) )

        ind_num += 1       # Increase index number of list_3 

    total = int ( index_1 + index_2 + index_3 + index_4 )

    print ( "\n",total , "outcomes in total ," )  # Print the total outcomes

    return lists


def decorations ( variable , option ) :   # User Defined Function to decorate the output and reduce the repition of codes.

    print ( "--" * 36 ) 

    print ( option, variable )

    print ( "--" * 36 )

list_4 = [ ]

while True :

    pass_entry =  validations  ( "Please enter your credits at pass : "  , 120 , 0 ,  )
    defer_entry =  validations  ( "Please enter your credits at defer : "  , 120 , 0 ,  )
    fail_entry    =  validations  ( "Please enter your credits at fail    : "  , 120 , 0 ,  )

    Total = pass_entry + defer_entry + fail_entry      # Get the total of the user entries

    if ( Total != 120 ) :

        print ( "Total Incorrect !!! " )

    else :

                if ( pass_entry == 120  ) :

                    printings_1 = decorations ( "Progress" , "\t" )

                    count_progress += 1

                    list_1 [ 0 ] = count_progress # Update the 1 element in the list_1

                    list_4_0 = [ "Progress",120 , 0 , 0 ]

                    list_4.append ( list_4_0 ) # Append the list_4_0 to list_4
                           
                elif  ( pass_entry == 100 )  :

                    printings_2 = decorations ( "Progress ( module trailer ) " , "\t" )

                    count_trailer += 1

                    list_1 [ 1 ] = count_trailer # Update the 2 element in the list_1

                    list_4_1 = [ "Progress ( module trailer )",100 , defer_entry, fail_entry ]

                    list_4.append ( list_4_1 ) # Append the list_4_1 to list_4
                   
                elif  ( ( pass_entry != ( 100 or 120 ) ) and ( pass_entry + defer_entry >= fail_entry ) ) :

                    printings_3 =  decorations  ( "Module Retriever " , "\t" )

                    count_retriever += 1

                    list_1 [ 2 ] = count_retriever # Update the 3 element in the list_1

                    list_4_2 = [ "Module Retriever",pass_entry , defer_entry , fail_entry ]

                    list_4.append ( list_4_2 ) # Append the list_4_1 to list_4

                elif ( pass_entry + defer_entry <  fail_entry ) :

                    printings_4 = decorations ( "Exclude" , "\t" )

                    count_exclude += 1

                    list_1 [ 3 ] = count_exclude # Update the 4 element in the list_1

                    list_4_3 = [ "Exclude", pass_entry , defer_entry , fail_entry ]

                    list_4.append ( list_4_3 ) # Append the list_4_3 to list_4
                    
    desire_1 = desire_check ( "\nWould you like to enter another set of data ? \n   Enter 'y' for yes or 'q' to quit and view results : " ,"Please enter 'y' to enter new data set or 'q' to see the histogram " ,'y' ,'q' )

    if ( desire_1 == 'y' ) : # Continue the outer while loop

        continue

    if ( desire_1 == 'q' ) :  # Exit from the outer while loop

        break
                    
print ( "\n" , "--" * 36 , "\nHistogram." )

printings_5 = looping ( 0 , list_1 , count_progress  , count_trailer  , count_retriever  , count_exclude )  # print the histogram

print ( "--" * 36  )

file = None

file_name = input ( "\nEnter a file name with extention : " )

file = open ( file_name ,"w" )

number = 0

for elements in list_4 : # To iterate the elements in list_4
    
    prints_1 = str ( list_4[ number ][ 0 ] ) + " - "   

    file.write ( prints_1 )                     # https://www.youtube.com/watch?v=6jsCbjQB3y0

    for data in list_4[ number ][ 1 : 4 ]  : 

        prints_2 = str ( data ) + ","

        file.write ( prints_2 )

    file.write ( "\n" )

    number += 1 # Increase index value caled number by 1

file.close ( )

print ( "\n...................Save Completed ...................\n " )

desire_2 = desire_check ( "Do you wish to load previous data [ y / n ] : " , "Please enter 'y' or 'n'  " , 'y' , 'n' )

if ( desire_2 == 'y' ) : # Continue the outer while loop

    while True :

        File = input ( "Enter file name with extention do you wish to load data : " )

        try :

            saved_file = open ( File )

            break

        except :

            print ( File , "does not exsists.\n  Please check again ......" )

            continue

    print ( "\n" )

    contents = saved_file.readlines ( )

    for lines in contents :

        print ( lines.strip ('\n') )

    saved_file.close ( )

if ( desire_2 == 'n' ) : 

    print ( "\n...................BYE...................\n " )  

    
    




             


        
        

    

        
        
