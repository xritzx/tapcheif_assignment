import re

class Database:
    """
    Temp DB for Basic CRUD
    """
    def __init__(self):
        self.db = dict()

    def read(self, id):
        return self.db.get(id, None)
    
    def create(self, document):
        return self.db.update({document["id"]: document})

    def delete(self, document):
        return self.db.pop(document["id"], None)

    def __repr__(self):
        return str(self.__dict__)
    

class InvertedIndex:
    """
    Inverted Index implementation with
    basic features as required
    """
    def __init__(self, db):
        self.index = dict()
        self.db = db
        
    def invertify_document(self, document):
        # Document recieved is adictionary of the paragraph with an id
        doc = re.sub(r"[^a-zA-Z0-9]+", ' ', document['text']).lower() # Meh, we need to remove 'special' characters
        words = doc.split(' ')
        wrappers_dict = dict()
        
        for word in words:
            word_frequency = wrappers_dict[word].frequency if word in wrappers_dict else 0
            wrappers_dict[word] = Wrapper(document["id"], word_frequency + 1)
            
 
        updated_data = { key: [wrapper] if key not in self.index else self.index[key] + [wrapper]
                            for (key, wrapper) in wrappers_dict.items() }

        self.index.update(updated_data) # Updating the Inverted Index Dictionary
        self.db.create(document) # Store the document to temp database
        return self
    
    def search(self, word):
        """
        To search and return 10 documents
        """
        return self.index[word][:10] if word in self.index else -1

    def reset(self):
        """
        To remove the computed Inverted Index
        incase of updates.
        """
        self.index.clear()
        self.db.db.clear()
       
    def __repr__(self):
        return str(self.index)

class Wrapper:
    """
    Representaion of document ID mapping to
    frequency of occurence.
    """
    def __init__(self, doc_id, frequency):
        self.doc_id = doc_id
        self.frequency = frequency
        
    def __repr__(self):
        return str(self.__dict__)

