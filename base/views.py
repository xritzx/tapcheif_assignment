from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django import forms
from django.http import HttpResponse
from django.conf import settings

import os
from .inverted_index import Database, InvertedIndex
from .forms import TextForm
import json
import PyPDF2 



db = Database()
inv_index = InvertedIndex(db)

def index(request):
    global inv_index

    if request.method == 'POST':
        text_form = TextForm(request.POST)

        if text_form.is_valid():
            passage = ""
            if 'pdf_file' in request.FILES:
                pdf = request.FILES['pdf_file']
                fileSys = FileSystemStorage()
                filename = fileSys.save(pdf.name, pdf)
                url = fileSys.url(filename)
                path = os.path.join(settings.MEDIA_ROOT, filename)
                pdfFileObj = open(path, 'rb') 
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
                for i in range(pdfReader.numPages):
                    passage += pdfReader.getPage(i).extractText()
                pdfFileObj.close()
            else:
                passage = text_form.cleaned_data["text"]
            inv_index.reset()
            documents = passage.splitlines()
            for i in range(len(documents)):
                inv_index.invertify_document({"id": i, "text": documents[i]})

        response = render(request, 'index.html', {'text_form': text_form, 'passage':passage})
        response.set_cookie('passage', passage)
        response.set_cookie('inv_index', inv_index)
        return response

    else:
        passage = request.COOKIES['passage'] if 'passage' in request.COOKIES else " "
        text_form = TextForm()
        return render(request, 'index.html', {'text_form': text_form, 'passage':passage})

def search(request, text):
    global inv_index
    docs = inv_index.search(text)
    documents = []
    print(docs)
    if(docs!=-1):
        for doc in docs:
            documents.append(
                {'text': str(db.read(doc.doc_id)['text']),
                 'id': str(doc.doc_id+1),
                 'freq':str(doc.frequency)})
    else:
        documents.append("No such word is found !")
    return render(request, 'list_documents.html', {'ten_documents': documents})
