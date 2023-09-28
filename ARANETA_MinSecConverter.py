SecondsInput = eval(input("Enter an integer in seconds: "))
ConvertedMinute = int(SecondsInput/60)
ConvertedSeconds = int(SecondsInput - (60*ConvertedMinute))
print(SecondsInput, "seconds is", ConvertedMinute, "minutes and", ConvertedSeconds, "seconds")
