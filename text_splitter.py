import multitasking

from sentiment_ranking import score_paragraph

@multitasking.task
def score(chunk_data,index):
    out = score_paragraph(chunk_data)
    print(" processing ===> ",index)
    return out
if __name__ == "__main__":
    with open("randomparas.txt","r", encoding="utf-8") as f:
        huge_text = f.read()

        chunks = huge_text.split("\n") # splitting the huge text to paragraphs
        for i,chunk in enumerate(chunks):
            #print(f"Para{i} , Score is {score_paragraph(chunk)}")
            score(chunk,i)
multitasking.wait_for_tasks()