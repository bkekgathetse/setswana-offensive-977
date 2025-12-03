# Data Statement (v1.0.0)
- Language: Setswana (BW/ZA/NA)
- Size: 977 instances (477 offensive, 500 non-offensive)
- Splits: 80/20 holdout (tag-free, unaugmented); 5-fold CV on 80%
- Annotation: offensive/non-offensive + trigger spans; κ=0.86
- Risks: explicit language; no PII
- Licenses: CC BY 4.0 (data), Apache-2.0 (code)
- Intended use: research on offensive-language detection & forensic NLP

DATA STATEMENT FOR SETSWANA OFFENSIVE LANGUAGE DATASET

The Setswana Offensive language content comprises of labels/annotations on approximately 1500 instances collected from both offensive and non-offensive sources in live settings such as social media, political debates, and lexicographic sources. This dataset has not been publicly made available, due to privacy concerns in line with Data Protection Act of Botswana, 2018.

A.	CURATION RATIONALE 

This dataset was curated in support of research for the detection of offensive, abusive, and hate-related expressions in the Setswana language, especially in social media and online communication. A representative population sample of Botswana and surrounding regions where Setswana is predominantly spoken was considered. Through this initiative, the primary objective is to enable creation of machine learning models for detection of non-technical cybercrime, such as cyberbullying, harassment, hate speech, and other forms of online aggression. The data were gathered to address the scarcity of annotated corpora for African languages and to contribute toward the creation of culturally and linguistically grounded digital forensic tools for low-resource languages.

A.	LANGUAGE VARIETY  
The dataset consists mainly of standard Setswana (TN), which tends to be used in Botswana. In addition to that, there are other varieties used socially online.

These include:
•	Colloquial Setswana which draws on youth slang (code-switching between Tswana-English);
•	Regional dialects, specifically those found in Southern Botswana (Ngwaketse, Kgatleng, and Central Districts), 
•	Code-mixing between English and other languages like Sepedi or Sesotho can also be observed. The phenomenon represents typical bilingual behavior online.

B.	SPEAKER DEMOGRAPHIC 

The corpus represents written texts produced in Facebook public posts as well as comments between native/fluent speakers in Setswana between 2021 and 2024. Although individual demographic metadata cannot be obtained because of ethical anonymization, the estimated user base includes:

•	Geographic Region: Primarily Botswana. It also includes small populations from South Africa’s province of Northwest.

•	Gender representation: Mixed gender representation, with positions reflecting both male and female modes of discourse.

•	Age group: Approximately aged 18-45 Years. Identifying with the age group that uses social media. In preprocessing steps to comply with privacy requirements set in Botswana’s Data Protection Act (2018), identifying information (names, residence, or handles) was removed or anonymized.

C.	ANNOTATOR DEMOGRAPHIC

Three linguists who are fluent in Setswana, and one cybersecurity expert affiliated with Botswana Accountancy College (BAC), undertook the task of annotating.

•	Proficiency in native languages: The annotators are native speakers of Setswana.

•	Annotation expertise:  Each individual has education in computational linguistics or related expertise involving offending or forensic linguistics.

•	Annotation framework: The guidelines used to annotate are adapted based on standard categorizations for abusive language (Waseem & Hovy, 2016; Founta et al.,2018), considered to cater to regional idiosyncrasies of the Consensus procedure. Disagreements between the individual annotations are resolved using majority voting after consultation. Periodically, calibration sessions are conducted.

D.	SPEECH SITUATION

All data were written, not spoken. Texts were extracted from public online interactions, including:
•	Comments and replies under public Facebook posts, 
•	Excerpts from online discussion forums and pages, capturing spontaneous, user-generated discourse. The communicative context often reflects informal social interactions, arguments, humour, or heated exchanges typical of online communities. The offensive instances include direct insults, tribal/ethnic slurs, gender-based derogation, and general profanity, often used for ridicule or confrontation.

E.	TEXT CHARACTERISTICS
•	Medium: Public social media posts and comments.
•	Modality: Written, informal digital text.
•	Token count: ~15,000 tokens (approx.).
•	Sentence count: 956 text samples (477 offensive, 500 non-offensive).
•	Annotation labels: Binary (0 = non-offensive, 1 = offensive).
•	Offensive categories: Profanity, hate speech, gender discrimination, harassment, and demeaning references.
•	Preprocessing: Texts were normalized for case and spacing, anonymized, tokenized using RoBERTa’s Byte-Pair Encoding (BPE), and augmented with semantic trigger annotations.
F.	RECORDING QUALTILY – N/A
Not applicable, as the dataset contains text, not speech or audio recordings.

G.	OTHER 
Ethical clearance for data handling and anonymization was obtained in line with institutional research ethics protocols at Botswana Accountancy College. All data were collected from publicly accessible sources; no private or direct-message content was included.

The dataset is intended strictly for academic and research purposes and is not publicly released in raw form due to data protection and sensitivity considerations, though derived embeddings and summary statistics are available upon request.

H.	PROVENANCE APPENDIX

Attribute	Description
Data source	Public Facebook posts and comments (2021–2024)
Collection method	Manual collection using search keywords and offensive trigger terms; followed by anonymization and curation
Annotation process	Three native Setswana annotators; binary labeling scheme (offensive/non-offensive); inter-annotator agreement > 0.85
Data storage	Secure institutional repository (BAC cloud drive, encrypted access)
Preprocessing tools	Python 3.10, Pandas, Regex, HuggingFace Tokenizers
Intended use	
•	To enable creation of machine learning models for detection of non-technical cybercrime, such as cyberbullying, harassment, hate speech, and other forms of online aggression. 
•	Fine-tuning and evaluation of Setswana transformer models for offensive language detection and digital forensic analysis.
Version	v1.2 (March 2025 release)

Curator contact	Mopati Bernedict Kekgathetse, 
University of Pretoria, 
Department of Computer Science, 
Pretoria, South Africa.
