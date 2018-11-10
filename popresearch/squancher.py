from textblob import TextBlob


class Squancher(object):

    def squanch(self, sentence):

        if not isinstance(sentence, str) or sentence == '':
            return ''

        sent = TextBlob(sentence)
        processed = []
        for word, tag in sent.tags:
            if tag.startswith('VB'):
                processed.append('squanch')
            else:
                processed.append(word)
        return ' '.join(processed)
