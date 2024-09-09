from django.shortcuts import render
from django.http import JsonResponse
import json
import nltk
from nltk.tokenize import sent_tokenize

# Ensure NLTK data is downloaded
nltk.download('punkt')

def fast_reading_view(request):
    # Render the main page for faster reading with word chunking
    return render(request, 'chunker/fast_reading.html')

def chunk_text(request):
    if request.method == 'POST':
        try:
            # Load and parse JSON data from request body
            data = json.loads(request.body)
            text = data.get('text', '')

            # Tokenize text into sentences
            sentences = sent_tokenize(text)

            # Example logic for processing sentences into chunks
            # Adjust chunking logic based on your needs
            chunks = [sentences[i:i+3] for i in range(0, len(sentences), 3)]

            # Prepare response data
            response_data = {'chunks': [' '.join(chunk) for chunk in chunks]}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
