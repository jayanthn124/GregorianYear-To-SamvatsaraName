# List out the Names of the 60 Samvatsara of a cycle.
SamvatsaraList = ["Prabhava", "Vibhava", "Shukla", "Pramoduta", "Prajapati",
"Angirasa", "Srimukha", "Bhava", "Yuva", "Dhatr", "Isvara", "Bahudhanya", "Pramathi", 
"Vikrama", "Vrushapraja", "Chitrabhanu", "Svabhanu", "Tarana", "Parthiva", "Avyaya/Vyaya", 
"Sarvajit", "Sarvaradhari", "Virodhi", "Vikruti", "Khara", "Nandana", "Vijaya", "Jaya",
"Manmatha", "Durmukha", "Hevilambi", "Vilambi", "Vikari", "Sharvari", "Plava", "Shubhakruta", 
"Shobhakruta", "Krodhi", "Vishwavasu", "Parabhava", "Plavanga", "Keelaka", "Soumya", 
"Sadharana", "Virodhakruta", "Paridhavi", "Pramadi", "Ananda", "Rakshasa", "Nala/Anala", 
"Pingala", "Kalayukta", "Sidharthi", "Raudri", "Durmati", "Dundhubhi", "Rudhirodgari", 
"Raktakshi", "Krodhana/Manyu", "Akshaya"]

# Initial Variables.
SAMVATSARA_CYCLE = 60

# User Input of the Gregorian Year:
year_of_samvatsara = int(input("\n Enter a Gregorian calendar year number: \n"))

if year_of_samvatsara == 0:
    print(" Year ZERO DOES NOT EXIST.")
else:
    # Defining the Reference Cycle of 54 BCE to 6 CE.
    start_of_ref_cycle = -54
    end_of_ref_cycle = 6

    # Calculate the number of years from the Ref Start Cycle 
    num_of_years = start_of_ref_cycle - year_of_samvatsara
    print("\n Number of Years from the Start of REF Cycle (54 BCE) is = ", num_of_years)

    # If the Year falls in the Reference Cycle of 54 BCE to 6 CE
    if year_of_samvatsara >= start_of_ref_cycle and year_of_samvatsara <= end_of_ref_cycle:
        if year_of_samvatsara > 0:
            samvatsara_index = abs(num_of_years + 1) # +1, since there is no YEAR ZERO.
        else:
            samvatsara_index = abs(num_of_years)
        print("\n Samvatsara Index = ", samvatsara_index)
        print("\n The Samvatsara that falls in this year is:", SamvatsaraList[samvatsara_index])
    # If the Year falls out of the Reference Cycle of 54 BCE to 6 CE
    else:
        cycle_num = int(num_of_years / SAMVATSARA_CYCLE)
        print("\n Cycle Number = ", cycle_num)
        if year_of_samvatsara < 0:
            cycle_num += 1 # +1, since there is no YEAR ZERO.
        start_of_the_cycle = (start_of_ref_cycle - (cycle_num * SAMVATSARA_CYCLE))
        if year_of_samvatsara > 0:
            start_of_the_cycle += 1 # +1, since there is no YEAR ZERO.
        print("\n The Start of the Samvatsara Cycle is: ", start_of_the_cycle)
        samvatsara_index = abs(start_of_the_cycle - year_of_samvatsara)
        print("\n Samvatsara Index = ", samvatsara_index)
        print("\n The Samvatsara that falls in this year is:", SamvatsaraList[samvatsara_index])
        