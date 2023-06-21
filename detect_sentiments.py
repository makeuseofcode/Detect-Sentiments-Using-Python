from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *

def clearAll():
    negativeField.delete(0, END)
    neutralField.delete(0, END)
    positiveField.delete(0, END)
    overallField.delete(0, END)
    textArea.delete(1.0, END)

def detect_sentiment():
    sentence = textArea.get("1.0", "end")
    sentiment_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sentiment_obj.polarity_scores(sentence)
    string = str(sentiment_dict['neg'] * 100)
    negativeField.insert(10, string)
    string = str(sentiment_dict['neu'] * 100)
    neutralField.insert(10, string)
    string = str(sentiment_dict['pos'] * 100)
    positiveField.insert(10, string)
    if sentiment_dict['compound'] >= 0.05:
        string = "Positive"
    elif sentiment_dict['compound'] <= - 0.05:
        string = "Negative"
    else:
        string = "Neutral"
    overallField.insert(10, string)

if __name__ == "__main__":
    gui = Tk()
    gui.config(background="#A020f0")
    gui.title("VADER Sentiment Analyzer")
    gui.geometry("400x700")
    enterText = Label(gui, text="Enter Your Sentence: ",font="arial 15 bold",bg="#A020f0")
    negative = Label(gui, text="Negative Percentage: ", font="arial 15",bg="#A020f0")
    neutral = Label(gui, text="Nuetral Percentage: ", font="arial 15",bg="#A020f0")
    positive = Label(gui, text="Positive Percentage: ", font="arial 15",bg="#A020f0")
    overall = Label(gui, text="Overall Sentence is: ", font="arial 15",bg="#A020f0")
    textArea = Text(gui, height=5, width=25, font="arial 15",  bg="#cf9fff")
    check = Button(gui, text="Check Sentiment", bg="#e7305b", font=("arial", 12, "bold"), command=detect_sentiment)
    clear = Button(gui, text="Clear", bg="#e7305b", font=("arial", 12, "bold"), command=clearAll)
    Exit = Button(gui, text="Exit", bg="#e7305b", font=("arial", 12, "bold"), command=exit)

    negativeField = Entry(gui, font="arial 15")
    neutralField = Entry(gui, font="arial 15")
    positiveField = Entry(gui, font="arial 15")
    overallField = Entry(gui, font="arial 15")
    
    enterText.grid(row=0, column=2,pady=15)
    textArea.grid(row=1, column=2, padx=60, pady=10, sticky=W)
    check.grid(row=2, column=2, pady=10)
    negative.grid(row=3, column=2, pady=10)
    neutral.grid(row=5, column=2, pady=10)
    positive.grid(row=7, column=2, pady=10)
    overall.grid(row=9, column=2,pady=5)
    negativeField.grid(row=4, column=2)
    neutralField.grid(row=6, column=2)
    positiveField.grid(row=8, column=2)
    overallField.grid(row=10, column=2, pady=10)
    clear.grid(row=11, column=2, pady=10)
    Exit.grid(row=12, column=2, pady=10)
    gui.mainloop()
