from torch.nn.functional import cosine_similarity

def get_similarity_score(embed1, embed2):
    return float(cosine_similarity(embed1, embed2, dim=0))