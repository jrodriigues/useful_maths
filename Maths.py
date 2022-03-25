def rounding(number, dp=2):
        """Returns the input chosen decimal places. Default = 2"""
        
        number_str = str(number)
        number_list = []
        rnded_number = ""
        
        # creates a list where all the values are the input number as integers, for easy maneuverability.
        for value in number_str:
            if value != '.':
                number_list.append(int(value))
            else:
                number_list.append(value)

        # means it's a whole number
        if '.' not in number_list:
            return number
            
        else:
            dp_index = number_list.index('.')

            # gives the number of decimal places of the original number. 
            # If < required dp, returns the original number.    
            decimal_places = len(number_list) - (dp_index + 1)

            if decimal_places > dp:
                if number_list[dp_index + dp + 1] >= 5:
                    number_list[dp_index + dp] += 1

                del number_list[dp_index + dp + 1:]

                for value in number_list:
                    rnded_number += str(value)

                rnded_number = float(rnded_number)
                return rnded_number

            else:
                return number
