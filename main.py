# arr1 = [-2, 4, -6, 5, 7]
# arr2 = [6, 3, 4, 0, 1, 10]
#
# for index, item1 in enumerate(arr1):
#     if item1+arr2[index] == 8:
#         print(item1, arr2[index])



# arr1 = [-2, 4, -6, 5, 7]
# arr2 = [6, 3, 4, 0, 1, 10]
#
# x = 8
# for a1 in arr1:
#     if x-a1 in arr2:
#         print(a1, x-a1)



# import csv
# import pprint
#
# reader = csv.DictReader(open("titanic_full.csv"), quoting=csv.QUOTE_ALL)
#
# data = []
#
# for line in reader:
#     temp_line = line.copy()
#     if temp_line["Age"]:
#         temp_line["Age"] = float(temp_line["Age"])
#     else:
#         temp_line["Age"] = -1
#     data.append(temp_line)
#
# filter(lambda x: x["Age"] >= 0, data)
#
# pprint.pprint(data)



# with open('bag_of_words.txt', encoding="mbcs") as f:
#     contents = f.read()
#
# words = contents.split(" ");
#
# trimmed_words = []
# for word in words:
#     trimmed_words.append(word.replace(",", ""))
#
#
# strategy = ["organization", "direction", "decision", "choice", "vision", "risk"]
# strategy_count = 0
# tactical = ["control", "objective", "finance", "marketing"]
# tactical_count = 0
# operational = ["execution", "operation", "production", "solution"]
# operational_count = 0
#
# found_words_strategic = []
# found_words_tactical = []
# found_words_operational = []
# for word in trimmed_words:
#     if word in strategy:
#         strategy_count += 1
#         found_words_strategic.append(word)
#     if word in tactical:
#         tactical_count += 1
#         found_words_tactical.append(word)
#     if word in operational:
#         operational_count += 1
#         found_words_operational.append(word)
#
# # print(strategy_count, tactical_count, operational_count)
# # print(found_words_strategic)
# # print(found_words_tactical)
# # print(found_words_operational)
#
# dictOfElemsStrategy = dict()
# # Iterate over each element in list
# for elem in found_words_strategic:
#     # If element exists in dict then increment its value else add it in dict
#     if elem in dictOfElemsStrategy:
#         dictOfElemsStrategy[elem] += 1
#     else:
#         dictOfElemsStrategy[elem] = 1
#
# dictOfElemsOperational = dict()
# # Iterate over each element in list
# for elem in found_words_operational:
#     # If element exists in dict then increment its value else add it in dict
#     if elem in dictOfElemsOperational:
#         dictOfElemsOperational[elem] += 1
#     else:
#         dictOfElemsOperational[elem] = 1
#
# dictOfElemsTactical = dict()
# # Iterate over each element in list
# for elem in found_words_tactical:
#     # If element exists in dict then increment its value else add it in dict
#     if elem in dictOfElemsTactical:
#         dictOfElemsTactical[elem] += 1
#     else:
#         dictOfElemsTactical[elem] = 1
#
# print(dictOfElemsStrategy)
# print(dictOfElemsOperational)
# print(dictOfElemsTactical)
#
# f = open("stratagicWords.txt", "w")
# f.write("Bulunan Kelimeler:\n")
# for item in dictOfElemsStrategy:
#         f.write("%s\n" % item)
# f.write("Kelime SAyısı:\n")
# f.write(str(strategy_count))
# f.close()
#
# f = open("tacticalWords.txt", "w")
# f.write("Bulunan Kelimeler:\n")
# for item in dictOfElemsTactical:
#         f.write("%s\n" % item)
# f.write("Kelime SAyısı:\n")
# f.write(str(tactical_count))
# f.close()
#
# f = open("operationalWords.txt", "w")
# f.write("Bulunan Kelimeler:\n")
# for item in dictOfElemsOperational:
#         f.write("%s\n" % item)
# f.write("Kelime SAyısı:\n")
# f.write(str(operational_count))
# f.close()

f = open("bag_of_words.txt", encoding="utf-8")
data = f.read().lower()

scores = {
    "Stratejik": {"organization", "direction", "decision", "choice", "vision", "risk"},
    "Taktiksel": {"control", "objective", "finance", "marketing"},
    "Operasyonel": {"execution", "operation", "production", "solution"}
}

res = {"Stratejik": {"count": 0}, "Taktiksel": {"count":0}, "Operasyonel": {"count":0}}

for (key, value) in scores.items():
    for word in value:
        res[key]["count"] += data.count(word)
        if res[key].get(word):
            res[key][word] += data.count(word)
        else:
            res[key][word] = data.count(word)

with open("result.txt", "w") as f:
    print(res, file=f)