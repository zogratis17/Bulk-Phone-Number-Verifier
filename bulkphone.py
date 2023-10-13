import phonenumbers
from phonenumbers import geocoder,carrier,timezone
import csv,openpyxl


excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Verified Phone Number'
sheet.append(['Phone Numbers','Country Code','National Number','Location','Carrier','Time Zone','Possible Number','Valid Number','Line Type'])


with open('phonenumbers.csv',encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    phoneNumbersList=[]
    for row in reader:
       phoneNumbersList.append(row['Phone Numbers']) 

countryCodeList=[]
nationalNumberList=[]
LocationList=[]
CarrierList=[]
TimeZoneList=[]
PossibleNumberList=[]
ValidNumberList=[]
lineType=[]

def lineTypeNumber(phone_number):
    if phonenumbers.number_type(phone_number) == phonenumbers.PhoneNumberType.MOBILE:
        lineType.append("Mobile phone number" )
    elif phonenumbers.number_type(phone_number) == phonenumbers.PhoneNumberType.FIXED_LINE:
        lineType.append("Fixed-line phone number" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.TOLL_FREE:
        lineType.append("Toll Free" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.PREMIUM_RATE:
        lineType.append("Premium Rate") 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.PAGER:
        lineType.append("Pager" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.PERSONAL_NUMBER:
        lineType.append("Personal Number" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.UAN:
        lineType.append("UAN" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.SHARED_COST:
        lineType.append("Shared Cost" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.VOIP:
        lineType.append("VOIP" )
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.UNKNOWN:
        lineType.append("Unknown")
    else:
        lineType.append("-")



def verifyPhoneNumber(phone_number):
    
    Valid_Number=phonenumbers.is_valid_number(phone_number)

    if Valid_Number==True:

        Country_Code=phone_number.country_code

        National_Number=phone_number.national_number

        Country=geocoder.description_for_number(phone_number,'en')

        Carrier=carrier.name_for_number(phone_number, 'en')

        Time_Zone_Num=timezone.time_zones_for_number(phone_number)

        Valid_Number=phonenumbers.is_valid_number(phone_number)

        Number_Possible=phonenumbers.is_possible_number(phone_number)

        timezones=str(Time_Zone_Num)
        Time_Zones=timezones[2:len(timezones)-3]

        lineTypeNumber(phone_number)

        countryCodeList.append(str(Country_Code))
        nationalNumberList.append(str(National_Number))
        LocationList.append(Country)
        CarrierList.append(Carrier)
        TimeZoneList.append(Time_Zones)
        PossibleNumberList.append(str(Number_Possible))
        ValidNumberList.append(str(Valid_Number))
    else:

        print("Wrong Number")


try:
    for i in range(0,len(phoneNumbersList)):    
        Number=phoneNumbersList[i]
        phone_number = phonenumbers.parse(Number)        
        verifyPhoneNumber(phone_number)
        sheet.append([phoneNumbersList[i],countryCodeList[i],nationalNumberList[i],LocationList[i],CarrierList[i],TimeZoneList[i],PossibleNumberList[i],ValidNumberList[i],lineType[i]])
        excel.save('Phone Number Verification.xlsx')
    print("Successful.....")

except Exception:
    print("Type the number with country code")

