# List out the Names of the 60 Samvatsara of a cycle.
SamvatsaraList = ["Prabhava", "Vibhava", "Shukla", "Pramoduta", "Prajapati",
"Angirasa", "Srimukha", "Bhava", "Yuva", "Dhatr", "Isvara", "Bahudhanya", "Pramthi", 
"Vikrama", "Vrushapraja", "Chitrabhanu", "Svabhanu", "Tarana", "Parthiva", "Avyaya/Vyaya", 
"Sarvajit", "Sarvaradhari", "Virodhi", "Vikruti", "Khara", "Nandana", "Vijaya", "Jaya",
"Manmatha", "Durmukha", "Hevilambi", "Vilambi", "Vikari", "Sharvari", "Plava", "Shubhakruta", 
"Shobhakruta", "Krodhi", "Vishwavasu", "Parabhava", "Plavanga", "Keelaka", "Soumya", 
"Sadharana", "Virodhakruta", "Paridhavi", "Pramadi", "Ananda", "Rakshasa", "Nala/Anala", 
"Pingala", "Kalayukta", "Sidharthi", "Raudri", "Durmati", "Dundhubhi", "Rudhirodgari", 
"Raktakshi", "Krodhana/Manyu", "Akshaya"]
# Declare Variables
SAMVATSARA_CYCLE = 60
START_OF_CURRENT_CYCLE = 1987
END_OF_CURRENT_CYCLE = 2046

def occurances_of_samvatsara():
    year_of_samvatsara = int(input("\n Enter a Gregorian calendar year number that coincides with the Samvatsara: \n"))
    span_of_years = int(input("\n Enter a Span of Years you want to calculate its occurrences for: \n"))
    time_dir = input("\n Enter 'f' for future and 'p' for past: \n").strip().lower()
    num = 0

    if time_dir == 'p':
        print(f"\nThe Occurrence of the Samvatsara of the year {year_of_samvatsara} over a span of {span_of_years} years in the Past is: ")
        while num < span_of_years:
            num += SAMVATSARA_CYCLE
            year_of_occurrence = year_of_samvatsara - num
            print(f"The #{num // SAMVATSARA_CYCLE} Occurrence of the Samvatsara is in the Year: {year_of_occurrence}")

    elif time_dir == 'f':
        print(f"The Occurrence of the Samvatsara of the year {year_of_samvatsara} over a span of {span_of_years} years in the Future is: ")
        while num < span_of_years:
            num += SAMVATSARA_CYCLE
            year_of_occurrence = year_of_samvatsara + num
            print(f"The #{num // SAMVATSARA_CYCLE} Occurrence of the Samvatsara is in the Year: {year_of_occurrence}")

    else:
        print("INVALID INPUT")

def samvatsara_by_year_number():
    year_of_samvatsara = int(input("\n Enter a Gregorian calendar year number: \n"))

    if year_of_samvatsara >= START_OF_CURRENT_CYCLE and year_of_samvatsara <= END_OF_CURRENT_CYCLE:
        samvatsara_index = year_of_samvatsara - START_OF_CURRENT_CYCLE
        print("\n The Samvatsara that falls in the year", year_of_samvatsara, "is:", SamvatsaraList[samvatsara_index])
    else:
        years_difference = year_of_samvatsara - START_OF_CURRENT_CYCLE
        print("\n Years Difference = ", years_difference)
        cycle_number = round(years_difference / SAMVATSARA_CYCLE)
        print("\n Cycle Number = ", cycle_number)
        start_of_the_cycle = START_OF_CURRENT_CYCLE + (cycle_number * SAMVATSARA_CYCLE)
        print("\n The Start of the Samvatsara Cycle is: ", start_of_the_cycle)
        end_of_the_cycle = start_of_the_cycle + (SAMVATSARA_CYCLE - 1)
        print("\n The End of the Samvatsara Cycle is: ", end_of_the_cycle)
        samvatsara_index = abs(year_of_samvatsara - start_of_the_cycle)
        print("\n The Samvatsara that falls in the year", year_of_samvatsara, "is:", SamvatsaraList[samvatsara_index])
         


def main():
    print("\n 1. Find the Occurances of the Same Samvatsara in Past/Future. ")
    print("\n 2. Find the Samvatsara from Gregorian Calender Year Number. ")
    choice = int(input("\n Choose a number: "))

    if choice == 1:
        occurances_of_samvatsara()
    elif choice == 2:
        samvatsara_by_year_number()
    else:
        print("\n INVALID INPUT. ")


if __name__ == "__main__":
    main()

