myDict = {
    "pankha" : "fan",
    "vastu" : "item",
    "dabba" : "box"
}
print("options are ",myDict.keys())
a = input("Enter your hindi words\n")
print("The meaning of your word is ",myDict.get(a))
