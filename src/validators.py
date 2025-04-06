from bert_score import score

def validate_summary(summary, original_text):
    P, R, F1 = score([summary], [original_text], lang="en")
    return round(F1.item(), 3)
