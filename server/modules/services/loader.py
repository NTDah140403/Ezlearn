# import spacy
import pkg_resources
# from langchain_groq import ChatGroq
from transformers import AutoTokenizer,AutoModel,AutoModelForSeq2SeqLM,pipeline,RobertaForQuestionAnswering,RobertaTokenizer,pipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_openai  import OpenAI
from config import settings
from langchain_google_genai import GoogleGenerativeAI

# from modules.services.seq2mcq_generator import mcq

# cached_path = pkg_resources.resource_filename('modules', 'pretrain_models')


# roberta_tokenizer = RobertaTokenizer.from_pretrained("deepset/roberta-base-squad2",cache_dir=cached_path)
# roberta_model = RobertaForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2",cache_dir=cached_path)


# phoBert_tokenizer = AutoTokenizer.from_pretrained('vinai/phobert-base',cache_dir=cached_path)
# phoBert_model = AutoModel.from_pretrained('vinai/phobert-base',cache_dir=cached_path)

# phoWhisper_transcriber = pipeline("automatic-speech-recognition", 
#                                   model=pkg_resources.resource_filename('modules', 'pretrain_models/PhoWhisper-small'), 
#                                   device=0)
# mbart_tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-cnn',cache_dir=cached_path)
# mbart_model = AutoModelForSeq2SeqLM.from_pretrained('facebook/bart-large-cnn',cache_dir=cached_path)

# envit5_tokenizer = AutoTokenizer.from_pretrained('VietAI/envit5-translation',cache_dir=cached_path)
# envit5_model = AutoModelForSeq2SeqLM.from_pretrained('VietAI/envit5-translation',cache_dir=cached_path)

# sentence_tokenizer = spacy.load('en_core_web_sm')

# Bert_tokenizer = AutoTokenizer.from_pretrained('google-bert/bert-base-uncased',cache_dir=cached_path)
# Bert_model = AutoModel.from_pretrained('google-bert/bert-base-uncased',cache_dir=cached_path)

# mcq_generator = mcq()

# llm = ChatGroq(
#     model="Llama3-8b-8192",
#     api_key="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",
#     temperature=0.6,
#     max_tokens=1000,
#     timeout=None,
#     max_retries=2
# )


llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=settings.GOOGLE_API_KEY,
    temperature=0.9,
    max_tokens=1000,
    timeout=None,
    max_retries=2
)





embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-l6-v2",
)

