from promptflow import tool


@tool
def chain_poll_post_process(cp1: str, cp2: str, cp3: str) -> float:
    
    cp_results = [cp1, cp2, cp3]
    coded_cp = []
    
    # Code chain poll results
        # yes = 1, no = 0, other = discarded
    for score in cp_results:
        if score.lower() == "yes":
            coded_cp.append(1)
        elif score.lower() == "no":
            coded_cp.append(0)

    # Average valid cp scores
    result = sum(coded_cp) / len(coded_cp)

    return round(result, 2)
