import pandas as pd
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from rouge import Rouge
from collections import Counter
import math

# Function to calculate BLEU-3 score for each pair
def calculate_bleu3(reference, generated):
    smoothing = SmoothingFunction().method1
    return sentence_bleu([reference.split()], generated.split(), weights=(0, 0, 1, 0), smoothing_function=smoothing)

def calculate_rouge(reference, generated):
    rouge = Rouge()
    return rouge.get_scores(generated, reference, avg=True)

def tokenize_code(code):
    return code.split()

def ngram_precision(reference, candidate, n):
    reference_ngrams = Counter([tuple(reference[i:i+n]) for i in range(len(reference)-n+1)])
    candidate_ngrams = Counter([tuple(candidate[i:i+n]) for i in range(len(candidate)-n+1)])
    
    overlap = sum((candidate_ngrams & reference_ngrams).values())
    total = sum(candidate_ngrams.values())
    
    if total == 0:
        return 0
    return overlap / total

def brevity_penalty(reference, candidate):
    ref_len = len(reference)
    cand_len = len(candidate)
    
    if cand_len > ref_len:
        return 1
    else:
        return math.exp(1 - ref_len / cand_len)

def compute_codebleu(reference_code, candidate_code, n=4):
    reference_tokens = tokenize_code(reference_code)
    candidate_tokens = tokenize_code(candidate_code)
    
    precision_scores = [ngram_precision(reference_tokens, candidate_tokens, i) for i in range(1, n+1)]
    geometric_mean_precision = math.exp(sum(math.log(p) for p in precision_scores if p > 0) / n)
    
    bp = brevity_penalty(reference_tokens, candidate_tokens)
    
    return bp * geometric_mean_precision

def rq1_metrics(path):
    # Load the CSV file
    file_path = path
    data = pd.read_csv(file_path)

    # Extract the original and generated texts
    generated_texts = data['Output Code'].tolist()
    reference_texts = data['Original Code'].tolist()

    # Apply the BLEU-3 score calculation for each pair
    data['BLEU-3'] = [calculate_bleu3(ref, gen) for ref, gen in zip(reference_texts, generated_texts)]
    data['CodeBLEU'] = [compute_codebleu(ref, gen) for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge 1-r'] = [calculate_rouge(ref, gen)["rouge-1"]["r"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge 1-p'] = [calculate_rouge(ref, gen)["rouge-1"]["p"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge 1-f'] = [calculate_rouge(ref, gen)["rouge-1"]["f"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge 2-r'] = [calculate_rouge(ref, gen)["rouge-2"]["r"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge 2-p'] = [calculate_rouge(ref, gen)["rouge-2"]["p"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge 2-f'] = [calculate_rouge(ref, gen)["rouge-2"]["f"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge L-r'] = [calculate_rouge(ref, gen)["rouge-l"]["r"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge L-p'] = [calculate_rouge(ref, gen)["rouge-l"]["p"] for ref, gen in zip(reference_texts, generated_texts)]
    data['Rouge L-f'] = [calculate_rouge(ref, gen)["rouge-l"]["f"] for ref, gen in zip(reference_texts, generated_texts)]


    # Print the DataFrame with BLEU-3 scores
    print(data)
    # Save the results to the same CSV file
    data.to_csv(file_path, index=False)