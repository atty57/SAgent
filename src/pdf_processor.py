from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

class PDFProcessor:
    def __init__(self):
        self.embedding_model = SentenceTransformer("sentence-t5-base")

    def process_pdf(self, file_path):
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def chunk_content(self, text, max_chunks=5):
        sentences = text.split(". ")
        embeddings = self.embedding_model.encode(sentences)
        n_clusters = min(len(sentences) // 50, max_chunks)
        if n_clusters < 2: n_clusters = 2
        kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(embeddings)
        clusters = kmeans.labels_
        chunks = []
        for i in range(n_clusters):
            grouped = [sentences[j] for j in range(len(sentences)) if clusters[j] == i]
            cluster_text = ". ".join(grouped)
            if cluster_text.strip():
                chunks.append({"id": i, "text": cluster_text})
        return chunks
