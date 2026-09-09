def find_runner_up(scores):
    
    unique_scores = list(set(scores)) # set() removes duplicate scores 
    unique_scores.sort(reverse=True) # sort(reverse=True) puts highest scores first 

    return unique_scores[1] # → index [1] gives the runner-up