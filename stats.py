def word_count(text):
    words = text.split()
    return len(words)

def characters(text):
    lower_text = text.lower()
    seperated_characters = list(lower_text)
    counts = dict()
    for i in seperated_characters:
        counts[i] = counts.get(i, 0) + 1
    return counts

def sort_on(items):
    return items["num"]

def report(counts):
    report_list = []
    # loop to place key and value pairs within a list of dictionaries
    for key, value in counts.items(): 
        if key.isalpha()==True:
            report_list.append(
                {
                "char":key, "num":value
                }
            )
    # sort the list greatest to least "num"
    report_list.sort(reverse=True, key=sort_on)

    return report_list