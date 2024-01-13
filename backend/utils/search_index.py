from nltk.stem import PorterStemmer


def search(query, index):
    matches = []
    for pdf, page_index in index.items():
        for page, keywords in page_index.items():
            average_score = 0
            found_keywords = []
            for keyword in query.split():
                # stem the keyword
                keyword = PorterStemmer().stem(keyword)
                if keyword in keywords:
                    average_score += keywords[keyword]
                    found_keywords.append(keyword)
                else:
                    average_score += 0
            average_score /= len(query.split())

            matches.append(
                {
                    "pdf": pdf,
                    "page": page,
                    "average_score": average_score,
                    "keywords": found_keywords,
                }
            )

    # sort matches by number of keywords found and then by average score
    matches.sort(
        key=lambda match: (len(match["keywords"]), match["average_score"]), reverse=True
    )

    # remove matches with average score of 0
    matches = [
        match
        for match in matches
        if int(match["average_score"]) > 0 and \
            len(match["keywords"]) >= len(query.split())
    ]

    # group matches by pdf
    pdfs = {}
    for match in matches:
        pdf = match["pdf"]
        if pdf not in pdfs:
            pdfs[pdf] = []
        pdfs[pdf].append(match)

    return pdfs


def print_matches(matches, search_description):
    print(f"Matches for '{search_description}':")
    for match in matches:
        print(
            f"File: {match['pdf']}, Page: {match['page']}, "
            f"Keywords Found: {match['keywords']}, "
            f"Score: {match['average_score']}"
        )
